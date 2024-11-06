"""Module docstring"""
import os
import time
from tabulate import tabulate
from modulos import busqueda

def menu_principal() -> None:
    """Dosctring"""
    clear_screen()
    while True:
        visualizacion_menu_principal()
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
                print(
                    "Opción no válida, intente de nuevo."
                )
                time.sleep(0.75)
                clear_screen()
                continue


def clear_screen() -> None:
    """ Esta funcion limpia la pantalla a medida que el usuario navega entre las opciones.
        Returns: 
            - None
    """
    os.system("cls" if os.name == "nt" else "clear")

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

def menu_busqueda():
    opciones = ["Pedir prestado",
                "Ver reviews",
                "Volver al menú principal",]
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")




def buscar_libro():
    while True:
        clear_screen()
        visualizacion_submenu_buscar_libro()
        op = input("Seleccione una opción: ")
        match op:
            case "1":
                clear_screen()
                title_op = input("Ingrese el nombre del libro a buscar: ")
                busqueda.busqueda_titulo(title_op)
                seleccion = input("Seleccione su libro: ")
                
            case "2":
                clear_screen()
            case "3":
                clear_screen()
            case "4":
                clear_screen()
                break
            case _:
                clear_screen()
                print(
                    "Opción no válida, intente de nuevo."
                )
                time.sleep(0.75)
                clear_screen()