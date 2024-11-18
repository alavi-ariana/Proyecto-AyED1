import os
import time
from tabulate import tabulate
from modulos import busqueda, devolucion, prestamo

def menu_principal() -> None:
    """
    Muestra el menu principal del sistema y permite navegar entre las opciones.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    clear_screen()
    while True:
        visualizacion_menu_principal()
        choice = input("\nSeleccione una opcion: ")
        match choice:
            case "1":  # Buscar libro
                buscar_libro()
            case "2":  # Devolver libro
                clear_screen()
                devolucion.devolver_libro()
                input("\nPresione Enter para continuar...")
            case "3":  # Salir del programa
                clear_screen()
                print("¡Adios!")
                break
            case _:
                clear_screen()
                print("Opcion no valida, intente de nuevo.")
                time.sleep(0.75)
                clear_screen()

def clear_screen() -> None:
    """
    Limpia la pantalla para mejorar la visualizacion.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    os.system("cls" if os.name == "nt" else "clear")

def visualizacion_menu_principal() -> None:
    """
    Muestra el menu principal.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    menu = [["1. Buscar libros", "2. Devolver Libros", "3. Salir del programa"]]
    titulo = "MENU PRINCIPAL"
    print(titulo.center(65, " "))
    print("=" * 65)
    print(
        tabulate(menu, tablefmt="fancy_grid", colalign=("center", "center", "center"))
    )
    print("=" * 65)

def visualizacion_submenu_buscar_libro() -> None:
    """
    Muestra el submenu para buscar libros.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    submenu = [
        [
            "1. Buscar por titulo",
            "2. Buscar por autor",
            "3. Buscar por genero",
            "4. Volver al menu principal",
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

def menu_busqueda(libro: dict) -> None:
    """
    Muestra las opciones disponibles despues de buscar un libro.
    - Argumentos:
        - libro (dict): Diccionario con los detalles del libro seleccionado.
    - Retorna:
        - None
    """
    opciones = [
        "Pedir prestado",
        "Ver reviews",
        "Volver al menu principal",
    ]
    while True:
        clear_screen()
        print(f"Libro seleccionado: {libro['title']} - {libro['author']}")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        seleccion = input("\nSeleccione una opcion: ")
        match seleccion:
            case "1":  # Pedir prestado
                clear_screen()
                prestamo.prestar_libro(libro)
                input("\nPresione Enter para continuar...")
                break
            case "2":  # Ver reviews
                clear_screen()
                busqueda.ver_reviews(libro)
                input("\nPresione Enter para continuar...")
            case "3":  # Volver
                clear_screen()
                break
            case _:
                print("Opcion no valida, intente de nuevo.")
                time.sleep(0.75)

def buscar_libro() -> None:
    """
    Gestiona la busqueda de libros y permite interactuar con los resultados.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    while True:
        clear_screen()
        visualizacion_submenu_buscar_libro()
        op = input("Seleccione una opcion: ")
        match op:
            case "1":  # Buscar por titulo
                clear_screen()
                title_op = input("Ingrese el nombre del libro a buscar: ")
                coincidencias = busqueda.busqueda_titulo(title_op)
                if not coincidencias:
                    print("No se encontraron coincidencias. Intente de nuevo.")
                    time.sleep(1.5)
                    continue
                busqueda.imprimir_coincidencias(coincidencias)
                libro = busqueda.seleccion_libro(coincidencias)
                if libro:
                    menu_busqueda(libro)
            case "2":  # Buscar por autor
                clear_screen()
                author_op = input("Ingrese el autor a buscar: ")
                coincidencias = busqueda.search_(author_op, 'author')
                if not coincidencias:
                    print("No se encontraron coincidencias. Intente de nuevo.")
                    time.sleep(1.5)
                    continue
                busqueda.imprimir_coincidencias(coincidencias)
                libro = busqueda.seleccion_libro(coincidencias)
                if libro:
                    menu_busqueda(libro)
            case "3":  # Buscar por genero
                clear_screen()
                genre_op = input("Ingrese el genero a buscar: ")
                coincidencias = busqueda.search_(genre_op, 'genre')
                if not coincidencias:
                    print("No se encontraron coincidencias. Intente de nuevo.")
                    time.sleep(1.5)
                    continue
                busqueda.imprimir_coincidencias(coincidencias)
                libro = busqueda.seleccion_libro(coincidencias)
                if libro:
                    menu_busqueda(libro)
            case "4":  # Volver al menu principal
                clear_screen()
                break
            case _:
                print("Opcion no valida, intente de nuevo.")
                time.sleep(0.75)

