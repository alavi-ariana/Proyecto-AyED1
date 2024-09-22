"""PROGRAMA PRINCIPAL"""
import os
import re
import auxiliar as auxi
from tabulate import tabulate

def clear_screen() -> None:
    """ Esta funcion limpia la pantalla a medida que el usuario navega entre las opciones.
        Returns: 
            - None
    """
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu_principal() -> None:
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


def mostrar_submenu_buscar_libro() -> None:
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

def libro_titulo(title):
    """lol"""
    coincidencias = auxi.search(title, 'title')
    if len(coincidencias) > 1:
        for i, libro in enumerate(coincidencias, 1):
            print(f"{i}. {libro['title']} - {libro['author']}")
    elif len(coincidencias) == 1:
        print(f"{coincidencias[0]['title']} - {coincidencias[0]['author']}")
    else:
        print("El libro no fue encontrado.")

def libro_autor(author):
    """lol"""
    coincidencias = auxi.search(author, 'author')
    if len(coincidencias) > 0:
        print(f"{coincidencias[0]['author'].upper()}")
        for libro in coincidencias:
            print(f"- {libro['title']}")
    else:
        print("No hubo coincidencias.")

def libro_genero():
    """lol"""
    libros = auxi.leer_libros()
    generos = set(dato['genre'] for dato in libros)
    for genero in generos:
        print(genero)

    genero_op = input("Elija un género: ")

    patron = re.compile(genero_op, re.IGNORECASE)

    genero_coincidencia = [genero for genero in generos if patron.search(genero)]

    if genero_coincidencia:
        genero_op = genero_coincidencia[0]
        libros_filtrados = [libro for libro in libros if libro['genre'] == genero_op]
        print(f"LIBROS EN EL GENERO{genero_op.upper()}")
        for libro in libros_filtrados:
            print(f"{libro['title']} - {libro['author']}")
        input()
    else:
        print("GÉNERO NO ENCONTRADO")
        input()

def buscar_libro():
    """lol"""
    while True:
        clear_screen()
        mostrar_submenu_buscar_libro()
        libro = input("\nSeleccione una opción: ")
        clear_screen()
        match libro:
            case "1":  # Busqueda de libros por titulo
                title_op = input("Ingrese el título del libro a buscar: ")
                libro_titulo(title_op)
            case "2":  # Busqueda de libros por autor
                author_op = input("Ingrese el autor a buscar: ")
                libro_autor(author_op)
            case "3":  # Busqueda de libros por genero
                libro_genero()
            case "4":  # Volver al menu principal
                break
            case _:
                clear_screen()
                input(
                    "Opción no válida, intente de nuevo. Presione ENTER para continuar."
                )
                continue



if __name__ == "__main__":
    while True:
        clear_screen()
        mostrar_menu_principal()
        choice = input("\nSeleccione una opción: ")
        match choice:
            case "1":  # BUSCAR LIBRO
                buscar_libro()
            case "2":  # DEVOLVER LIBRO
                pass  # Validar input de documento de usuario
            case "3":  # SALIR DEL PROGRAMA
                clear_screen()
                print("¡Adiós!")
                break
            case _:
                clear_screen()
                input(
                    "Opción no válida, intente de nuevo. Presione ENTER para continuar."
                )
                continue
