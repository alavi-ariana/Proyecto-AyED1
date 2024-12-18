import os
import json
import time
from funciones import funciones
from modulos import menues

def solicitar_dni() -> str:
    '''
    Solicita el DNI de un cliente y valida que cumpla con los requisitos

    Pre:
        No recibe ningún parámetro
    Post:
        Devuelve el DNI válido del cliente, en caso contrario muestra un mensaje de error
    '''

    funciones.clear_screen()
    while True:
        dni = input("Ingrese el DNI del cliente: ").strip()

        if not dni.isdigit():
            print("Error: El DNI debe contener solo números.\n")
        elif len(dni) != 8:
            print("Error: El DNI debe tener exactamente 8 dígitos.\n")
        elif dni == "":
            print("Error: El DNI no puede estar vacío.\n")
        else:
            return dni

def mostrar_libros(libros: list) -> None:
    '''
    Muestra en pantalla los libros prestados

    Pre:
        libros (list): Una lista de diccionarios con información de los libros prestados
    Post.
        No retorna ningún valor, pero imprime en pantalla los títulos de los libros junto con la fecha de préstamo
    '''

    print("Libros prestados:")
    for i, libro in enumerate(libros, 1):
        print(f"{i}. {libro['title']} - Fecha de préstamo: {libro['fecha_de_prestamo']}")

def seleccionar_libro(libros: list) -> None:
    '''
    Solicita al usuario seleccionar un libro de la lista de libros prestados

    Pre:
        libros (list): Una lista de libros prestados
    Post:
        Devuelve el número del libro seleccionado por el usuario. Si el número es invákido, solicita al usuario que ingrese un número válido
    '''

    while True:
        try:
            num_libro = int(input("\nIngrese el número del libro que desea devolver: "))
            if num_libro >= 1 and num_libro <= len(libros):
                return num_libro
            else:
                print("Error: El número no corresponde a ningún libro. Inténtelo nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def guardar_prestamos(prestamos: dict) -> None:
    '''
    Guarda la información actualizada de los préstamos en el archivo 'prestamos.json'
    
    Pre:
        prestamos (dict): Un diccionario con la información de los préstamos
    Post:
        Guarda los datos de los préstamos en el archivo. Si ocurre un error, muestra su mensaje correspondiente
    '''

    directorio = os.getcwd()
    file_prestamos = os.path.join(directorio, "Biblioteca", "JSON", "prestamos.json")
    try:
        with open(file_prestamos, 'w', encoding='utf-8') as arch_prestamos:
            json.dump(prestamos, arch_prestamos, indent=4)
    except FileNotFoundError:
        print(f'Error: No se encontró el archivo {file_prestamos}.')
    except json.JSONDecodeError:
        print(f'Error al decodificar el archivo JSON en {file_prestamos}.')
    except Exception as e:
        print(f"Error desconocido al guardar el archivo {file_prestamos}: {e}")

def gestionar_review(libro_devuelto: dict) -> None:
    '''
    Gestiona la solicitud de una review del libro devuelto

    Pre:
        libro_devuelto (dict): Un diccionario que contiene el libro devuelto (con su título)
    Post:
        Si se deja una review, se guarda en el archivo 'reviews.json'. Si ocurre un error al guardar o leer el archivo, se muestra un mensaje de error
    '''

    while True:
        op = input("¿Desea dejar una review del libro? (s/n): ").lower().strip()
        if op == 's':
            review = input("\nEscriba su review: ").strip()
            if review:
                try:
                    with open('Biblioteca/JSON/reviews.json', 'r', encoding='utf-8') as leer_reviews:
                        try:
                            reviews = json.load(leer_reviews)
                        except json.JSONDecodeError:
                            reviews = {}
                except FileNotFoundError:
                    reviews = {}
                except Exception as e:
                    print(f"Error desconocido al leer el archivo: {e}")
                    reviews = {}

                titulo_libro = libro_devuelto['title']
                if titulo_libro in reviews:
                    reviews[titulo_libro]['reviews'].append(review)
                else:
                    reviews[titulo_libro] = {'reviews': [review]}

                try:
                    with open('Biblioteca/JSON/reviews.json', 'w', encoding='utf-8') as escribir_reviews:
                        json.dump(reviews, escribir_reviews, indent=4)
                    print("\n¡Gracias por dejar su review!")
                    break
                except FileNotFoundError:
                    print(f"Error: No se encontró el archivo.")
                except json.JSONDecodeError:
                    print(f"Error al decodificar el archivo JSON.")
                except Exception as e:
                    print(f"Error desconocido al guardar las reviews: {e}")
            else:
                print("Error: La review no puede estar vacía.")
        elif op == 'n':
            break
        else:
            print("Error: Elija una opción válida (s/n).\n")


def devolver_libro() -> None:
    '''
    Permite al cliente devolver un libro previamente prestado

    Pre:
        No recibe ningún parámetro
    Post:
        Guarda la información actualizada. Muestra mensajes de error en caso de que no se puedan devolver libros
    '''

    funciones.clear_screen()
    dni = solicitar_dni()
    prestamos = funciones.leer_prestamos()

    prestamo = prestamos.get(dni)
    if prestamo:
        libros_prestados = prestamo.get('libros_prestados', [])

        if libros_prestados:
            funciones.clear_screen()
            mostrar_libros(libros_prestados)
            num_libro = seleccionar_libro(libros_prestados)

            if num_libro:
                libro_devuelto = libros_prestados.pop(num_libro - 1)
                prestamos[dni]['cantidad_libros_prestados'] -= 1
                guardar_prestamos(prestamos)
                funciones.clear_screen()
                print(f"El libro '{libro_devuelto['title']}' ha sido devuelto exitosamente.")
                gestionar_review(libro_devuelto)
            else:
                print("Error: Número de libro no válido.")
        else:
            print("Error: Este DNI no tiene libros prestados.")
    else:
        print("Error: No se encontraron libros prestados para este DNI.")
    time.sleep(1.50)
    funciones.clear_screen()