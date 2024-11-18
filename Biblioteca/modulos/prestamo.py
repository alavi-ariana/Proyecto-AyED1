import os
from funciones import funciones
from modulos.busqueda import seleccion_libro  # librería
from typing import Dict
from modulos import formateo

ruta_usuarios = os.path.join("Biblioteca", "JSON", "usuarios.json")
ruta_prestamos = os.path.join("Biblioteca", "JSON", "prestamos.json")
ruta_libros = os.path.join("Biblioteca", "CSV", "books.csv")


def validar_o_registrar_usuario(dni: str) -> bool:
    """
    Verifica si un usuario ya esta registrado. Si no lo esta, lo registra.
    - Argumentos:
        - dni: El DNI del usuario.
    - Retorna:
        - bool: True si el usuario fue validado o registrado correctamente.
    """
    # Validación de que el DNI tenga exactamente 8 dígitos numéricos
    while not (dni.isdigit() and len(dni) == 8):
        print("El documento debe ser de 8 digitos. Intente de nuevo.")
        dni = input("Ingresa tu DNI: ").strip()  # Solicita el DNI hasta que sea válido

    try:
        # Carga los usuarios desde el archivo JSON
        usuarios = funciones.leer_usuarios()

        # Verifica si el usuario ya existe
        if any(u["dni"] == dni for u in usuarios):
            print("Usuario encontrado.")
            return True

        # Si el usuario no esta registrado, se registra
        nombre = input("Ingresa tu nombre: ").strip()
        apellido = input("Ingresa tu apellido: ").strip()

        # Añade el nuevo usuario al diccionario
        usuarios.append({"dni": dni, "nombre": nombre, "apellido": apellido})

        # Guarda nuevamente el archivo JSON
        funciones.guardar_json(
            os.path.join(os.getcwd(), "Biblioteca", "JSON", "usuarios.json"),
            usuarios,
        )  # Se guarda como lista de diccionarios
        print("¡Usuario registrado exitosamente!")
        return True

    except FileNotFoundError:
        print(f"Error: El archivo {ruta_usuarios} no se encuentra. Verifique la ruta.")
    except Exception as e:
        print(f"Error inesperado al procesar el usuario: {str(e)}")

    return False


def obtener_usuario_por_dni(dni: str) -> Dict:
    """
    Obtiene un usuario por su DNI desde el archivo de usuarios.
    - Argumentos:
        - dni: El DNI del usuario.
    - Retorna:
        - Dict: El diccionario del usuario si se encuentra, o None si no se encuentra.
    """
    try:
        usuarios = funciones.leer_usuarios()  # Leer usuarios como lista de diccionarios
        # Verifica si el DNI existe dentro de los usuarios cargados
        usuario = next((u for u in usuarios if u["dni"] == dni), None)
        
        if usuario is None:
            print(f"...Usuario con DNI N° {dni} no encontrado.")
        return usuario

    except FileNotFoundError:
        print(f"Error: El archivo {ruta_usuarios} no se encuentra. Verifique la ruta.")
    except Exception as e:
        print(f"Error inesperado al obtener el usuario: {str(e)}")

    return None


def prestar_libro(libro: Dict) -> None:
    """
    Solicita un prestamo de libro, validando al usuario y verificando la disponibilidad del libro.
    Esta version asume que el libro ya esta seleccionado.
    - Argumentos:
        - libro: Diccionario con los detalles del libro seleccionado.
    - Retorna:
        - Ninguno
    """
    try:
        dni = input("Ingresa tu DNI: ")  # Solicita el DNI del usuario
        usuario = obtener_usuario_por_dni(dni)

        # Si el usuario no es encontrado, intenta registrar el usuario
        if not usuario:
            if not validar_o_registrar_usuario(dni):
                return  # Si el usuario no se pudo registrar, termina la funcion

            # Después de registrar al usuario, buscamos al usuario directamente
            usuario = obtener_usuario_por_dni(dni)

        # Verificacion si el usuario no ha sido encontrado incluso después del registro
        if not usuario:
            print("No se pudo registrar el usuario correctamente.")
            return

        formateo.visualizar_prestamo_libro(libro)
        respuesta = (
            input(
                f"\n¿Deseas llevarte el libro prestado {usuario['nombre']} {usuario['apellido']}? (Y/N): "
            )
            .strip()
            .upper()
        )

        if respuesta != "Y":
            return  # Si el usuario no quiere el libro, termina

        # Verifica la disponibilidad segun el stock y los prestamos actuales
        prestamos = funciones.leer_json(
            ruta_prestamos
        )  # Carga los prestamos existentes
        prestamos_actuales = sum(
            1 for p in prestamos if p["isbn-13"] == libro["isbn-13"]
        )

        if prestamos_actuales < int(libro["stock"]):
            # Registra el prestamo
            prestamos.append({"isbn-13": libro["isbn-13"], "dni": dni})
            funciones.guardar_json(
                ruta_prestamos, prestamos
            )  # Guarda los prestamos actualizados
            print(
                f"El libro '{libro['title']}' ha sido prestado exitosamente a {usuario['nombre']} {usuario['apellido']}."
            )
        else:
            print(f"No hay ejemplares disponibles del libro '{libro['title']}'.")

    except FileNotFoundError:
        print(f"Error: El archivo {ruta_prestamos} no se encuentra. Verifique la ruta.")
    except ValueError as ve:
        print(f"Error de valor: {str(ve)}")
    except Exception as e:
        print(f"Error inesperado al procesar el préstamo del libro: {str(e)}")
