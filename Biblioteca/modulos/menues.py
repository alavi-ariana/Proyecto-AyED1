"""Module docstring"""
import os
import time
from tabulate import tabulate
from modulos import busqueda
from funciones import funciones

def menu_principal() -> None:
    """Dosctring"""
    funciones.clear_screen()
    while True:
        visualizacion_menu_principal()
        choice = input("\nSeleccione una opción: ")
        match choice:
            case "1":  # BUSCAR LIBRO
                buscar_libro()
            case "2":  # DEVOLVER LIBRO
                pass  # Validar input de documento de usuario
            case "3":  # SALIR DEL PROGRAMA
                funciones.clear_screen()
                print("¡Adiós!")
                break
            case _:
                funciones.clear_screen()
                print(
                    "Opción no válida, intente de nuevo."
                )
                time.sleep(0.75)
                funciones.clear_screen()
                continue

def visualizacion_menu_principal() -> None:
    """ Muestra el menú principal.
        Returns:
            - None
    """
    menu = [["1. Buscar libros", "2. Devolver Libros", "3. Salir del programa"]]
    titulo = "MENÚ PRINCIPAL"
    print(titulo.center(65, " "))
    print("=" * 65)
    print(
        tabulate(menu, tablefmt="fancy_grid", colalign=("center", "center", "center"))
    )
    print("=" * 65)

def visualizacion_submenu_buscar_libro() -> None:
    """ Muestra el submenú para buscar libros.
        Returns:
            - None
    """
    submenu = [
        [
            "1. Buscar por título",
            "2. Buscar por autor",
            "3. Buscar por género",
            "4. Volver al menú principal",
        ]
    ]
    titulo = "BUSCAR LIBRO"
    print(titulo.center(100, " "))
    print("=" * 100)
    print(
        tabulate(
            submenu,
            tablefmt="fancy_grid",
            colalign=("center", "center", "center", "center"),
        )
    )
    print("=" * 100)

def menu_busqueda() -> None:
    opciones = ["Pedir prestado",
                "Ver reviews",
                "Volver al menú principal",]
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")


def buscar_libro() -> None:
    while True:
        funciones.clear_screen()
        visualizacion_submenu_buscar_libro()
        op = input("Seleccione una opción: ")
        match op:
            case "1": #Busqueda por título
                funciones.clear_screen()
                title_op = input("Ingrese el nombre del libro a buscar: ")
                coincidencias = busqueda.search_(title_op, 'title')
                if not coincidencias:
                    print("NO HUBO COINCIDENCIAS.")
                    time.sleep(0.75)
                    buscar_libro()
                busqueda.imprimir_coincidencias(coincidencias)
                libro = busqueda.seleccion_libro(coincidencias)
                while libro:
                    seleccion = input("DESEA VER REVIEWS O PEDIR PRESTADO EL LIBRO ('r' para reviews, 'p' para prestamo, 'e' para salir): ")
                    if seleccion.lower() == "e":
                        break
                    elif seleccion.lower() == "r":
                        busqueda.ver_reviews(libro)
                    elif seleccion.lower() == "p":
                        pass #ACA VA PEDIR PRESTAMO
                    else:
                        print("Debe seleccionar una opción válida.")
                time.sleep(0.75)
            case "2": #Busqueda por autor
                funciones.clear_screen()
                author_op = input("Ingrese el nombre del autor a buscar: ")
                coincidencias = busqueda.search_(author_op, 'author')
                if not coincidencias:
                    print("NO HUBO COINCIDENCIAS.")
                    time.sleep(0.75)
                    buscar_libro()
                busqueda.imprimir_coincidencias(coincidencias)
                libro = busqueda.seleccion_libro(coincidencias)
                while libro:
                    seleccion = input("DESEA VER REVIEWS O PEDIR PRESTADO EL LIBRO ('r' para reviews, 'p' para prestamo, 'e' para salir): ")
                    if seleccion.lower() == "e":
                        break
                    elif seleccion.lower() == "r":
                        busqueda.ver_reviews(libro)
                    elif seleccion.lower() == "p":
                        pass #ACA VA PEDIR PRESTAMO
                    else:
                        print("Debe seleccionar una opción válida.")
                time.sleep(0.75)
            case "3": #Busqueda por género
                funciones.clear_screen()
                generos = busqueda.imprimir_generos()
                genero_op = busqueda.seleccion_genero(generos)
                coincidencias = busqueda.busqueda_genero(genero_op)
                if not coincidencias:
                    print("No se encontraron libros en este género.")
                print(f"\nLIBROS EN EL GÉNERO {genero_op.upper()}:")
                busqueda.imprimir_coincidencias(coincidencias)
                for i, libro in enumerate(coincidencias, 1):
                    print(f"{i}. {libro['title']} - {libro['author']}")
                libro = busqueda.seleccion_libro(coincidencias)
                while libro:
                    seleccion = input("DESEA VER REVIEWS O PEDIR PRESTADO EL LIBRO ('r' para reviews, 'p' para prestamo, 'e' para salir): ")
                    if seleccion.lower() == "e":
                        break
                    elif seleccion.lower() == "r":
                        busqueda.ver_reviews(libro)
                    elif seleccion.lower() == "p":
                        pass #ACA VA PEDIR PRESTAMO
                    else:
                        print("Debe seleccionar una opción válida.")
            case "4": #Volver al menú principal
                funciones.clear_screen()
                break
            case _:
                funciones.clear_screen()
                print(
                    "Opción no válida, intente de nuevo."
                )
                time.sleep(0.75)
                funciones.clear_screen()
