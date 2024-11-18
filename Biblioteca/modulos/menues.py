import time
from modulos import busqueda, devolucion, prestamo, formateo


def menu_principal() -> None:
    """
    Muestra el menu principal del sistema y permite navegar entre las opciones.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    formateo.clear_screen()
    while True:
        formateo.visualizacion_menu_principal()
        choice = input("\nSeleccione una opcion: ")
        match choice:
            case "1":  # Buscar libro
                menu_buscar_libro()
            case "2":  # Devolver libro
                formateo.clear_screen()
                devolucion.devolver_libro()
                input("\nPresione Enter para continuar...")
            case "3":  # Salir del programa
                formateo.clear_screen()
                print("¡Adios!")
                break
            case _:
                formateo.clear_screen()
                print("Opcion no valida, intente de nuevo.")
                time.sleep(0.75)
                formateo.clear_screen()


def menu_buscar_libro() -> None:
    """
    Gestiona la busqueda de libros y permite interactuar con los resultados.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    while True:
        formateo.clear_screen()
        formateo.visualizacion_submenu_buscar_libro()
        choice = input("\nSeleccione una opcion: ")
        match choice:
            case "1":  # Buscar por titulo
                formateo.clear_screen()
                title_op = input("Ingrese el nombre del libro a buscar: ")
                coincidencias = busqueda.busqueda_titulo(title_op)
                if not coincidencias:
                    print("No se encontraron coincidencias. Intente de nuevo.")
                    time.sleep(1.5)
                    continue
                busqueda.imprimir_coincidencias(coincidencias)
                libro = busqueda.seleccion_libro(coincidencias)
                if libro:
                    menu_libro_encontrado(libro)
            case "2":  # Buscar por autor
                formateo.clear_screen()
                author_op = input("Ingrese el autor a buscar: ")
                coincidencias = busqueda.search_(author_op, "author")
                if not coincidencias:
                    print("No se encontraron coincidencias. Intente de nuevo.")
                    time.sleep(1.5)
                    continue
                busqueda.imprimir_coincidencias(coincidencias)
                libro = busqueda.seleccion_libro(coincidencias)
                if libro:
                    menu_libro_encontrado(libro)
            case "3":  # Buscar por genero
                formateo.clear_screen()
                coincidencias = busqueda.buscar_por_genero()
                if not coincidencias:
                    print("No se encontraron libros para el género seleccionado.")
                    time.sleep(1.5)
                    continue
                busqueda.imprimir_coincidencias(coincidencias)
                libro = busqueda.seleccion_libro(coincidencias)
                if libro:
                    menu_libro_encontrado(libro)
            case "4":  # Volver al menu principal
                formateo.clear_screen()
                break
            case _:
                print("Opcion no valida, intente de nuevo.")
                time.sleep(0.75)


def menu_libro_encontrado(libro: dict) -> None:
    """
    Muestra las opciones disponibles despues de buscar un libro.
    - Argumentos:
        - libro (dict): Diccionario con los detalles del libro seleccionado.
    - Retorna:
        - None
    """
    while True:
        formateo.clear_screen()
        formateo.visualizacion_menu_libro_encontrado(libro)
        seleccion = input("\nSeleccione una opción: ")
        match seleccion:
            case "1":  # Pedir prestado
                formateo.clear_screen()
                prestamo.prestar_libro(libro)
                input("\nPresione Enter para continuar...")
                break
            case "2":  # Ver reviews
                formateo.clear_screen()
                busqueda.ver_reviews(libro)
                input("\nPresione Enter para continuar...")
            case "3":  # Volver
                formateo.clear_screen()
                break
            case _:
                print("Opción no válida, intente de nuevo.")
                time.sleep(0.75)
