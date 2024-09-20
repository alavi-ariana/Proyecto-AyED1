<<<<<<< HEAD
=======
<<<<<<< HEAD
"""MENÚ PRINCIPAL"""

import os
from tabulate import tabulate


def clear_screen():
    """Esta funcion limpia la pantalla a medida que el usuario navega entre las opciones."""
    os.system("cls" if os.name == "nt" else "clear")
    return None


def mostrar_menu_principal():
=======
>>>>>>> main
"""PROGRAMA PRINCIPAL"""
import os
import auxiliar as auxi
from tabulate import tabulate

def clear_screen() -> None:
    """Esta funcion limpia la pantalla a medida que el usuario navega entre las opciones."""
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu_principal() -> None:
<<<<<<< HEAD
=======
>>>>>>> 655e7d194e1291c1b7891eef86a63bb101ccb743
>>>>>>> main
    """Muestra el menú principal."""
    menu = [["1. Buscar libros", "2. Devolver Libros", "3. Salir del programa"]]
    titulo = "MENÚ PRINCIPAL"
    print(titulo.center(65, " "))
    print("=" * 65)
    print(tabulate(menu, tablefmt="fancy_grid", colalign=("center", "center", "center")))
    print("=" * 65)
<<<<<<< HEAD
    return None

def mostrar_submenu_buscar_libro() -> None:
    """Muestra el submenú para buscar libros."""
    submenu = [["1. Buscar por título","2. Buscar por autor","3. Buscar por género","4. Volver al menú principal",]]
=======
<<<<<<< HEAD
    return None


def mostrar_submenu_buscar_libro():
    """Muestra el submenú para buscar libros."""
    submenu = [
        [
            "1. Buscar por tí1tulo",
=======


def mostrar_submenu_buscar_libro() -> None:
    """Muestra el submenú para buscar libros."""
    submenu = [
        [
            "1. Buscar por título",
>>>>>>> 655e7d194e1291c1b7891eef86a63bb101ccb743
            "2. Buscar por autor",
            "3. Buscar por género",
            "4. Volver al menú principal",
        ]
    ]
>>>>>>> main
    titulo = "BUSCAR LIBRO"
    print(titulo.center(100, " "))
    print("=" * 100)
    print(tabulate(submenu,tablefmt="fancy_grid",colalign=("center", "center", "center", "center"),))
    print("=" * 100)
<<<<<<< HEAD
    return None




def main_menu() -> None:
=======
<<<<<<< HEAD
    return None


def main_menu():
=======

def main_menu() -> None:
>>>>>>> 655e7d194e1291c1b7891eef86a63bb101ccb743
>>>>>>> main
    """Esta funcion controla el flujo del programa."""
    while True:
        clear_screen()
        mostrar_menu_principal()
<<<<<<< HEAD
        choice = input("\nSeleccione una opción: ")
=======
<<<<<<< HEAD
        choice = input("\n...Seleccione una opción: ")
=======
        choice = input("\nSeleccione una opción: ")
>>>>>>> 655e7d194e1291c1b7891eef86a63bb101ccb743
>>>>>>> main
        match choice:
            case "1":  # BUSCAR LIBRO
                while True:
                    clear_screen()
                    mostrar_submenu_buscar_libro()
<<<<<<< HEAD
=======
<<<<<<< HEAD
                    choice = input("\n...Seleccione una opción: ")
                    match choice:
                        case "1":  # Busqueda de libros por titulo
                            pass
                        case "2":  # Busqueda de libros por autor
                            pass
=======
>>>>>>> main
                    choice = input("\nSeleccione una opción: ")
                    clear_screen()
                    match choice:

                        case "1":  # Busqueda de libros por titulo
                            title_op = input("Ingrese el título del libro a buscar: ")
                            coincidencias = auxi.search(title_op, 'title')
                            if len(coincidencias) > 1:
                                for i, libro in enumerate(coincidencias, 1):
                                    print(f"{i}. {libro['title']} - {libro['author']}")
                            elif len(coincidencias) == 1:
                                print(f"{coincidencias[0]['title']} - {coincidencias[0]['author']}")
                            else:
                                print("El libro no fue encontrado.")
                            sub_choice = input("\nPresione ENTER para continuar o 4 para volver al menú principal: ")
                            if sub_choice == "4":
                                break

                        case "2":  # Busqueda de libros por autor
                            author_op = input("Ingrese el autor a buscar: ")
                            coincidencias = auxi.search(author_op, 'author')
                            if len(coincidencias) > 0:
                                print(f"{coincidencias[0]['author'].upper()}")
                                for libro in coincidencias:
                                    print(f"- {libro['title']}")
                            else:
                                print("No hubo coincidencias.")
                            sub_choice = input("\nPresione ENTER para continuar o 4 para volver al menú principal: ")
                            if sub_choice == "4":
                                break
<<<<<<< HEAD

=======
>>>>>>> 655e7d194e1291c1b7891eef86a63bb101ccb743
>>>>>>> main
                        case "3":  # Busqueda de libros por genero
                            pass

                        case "4":  # Volver al menu principal
                            break
                        
                        case _:
                            clear_screen()
                            input("Opción no válida, intente de nuevo. Presione ENTER para continuar.")
                            continue
            case "2":  # DEVOLVER LIBRO
                pass  # Validar input de documento de usuario

            case "3":  # SALIR DEL PROGRAMA
                clear_screen()
                print("¡Adiós!")
                break

            case _:
                clear_screen()
                input("Opción no válida, intente de nuevo. Presione ENTER para continuar.")
                continue
<<<<<<< HEAD
=======
<<<<<<< HEAD
    return None
=======
>>>>>>> 655e7d194e1291c1b7891eef86a63bb101ccb743
>>>>>>> main


if __name__ == "__main__":
    main_menu()
