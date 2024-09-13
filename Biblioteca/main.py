"""MENÚ PRINCIPAL"""

import os
from tabulate import tabulate


def clear_screen():
    """Esta funcion limpia la pantalla a medida que el usuario navega entre las opciones."""
    os.system("cls" if os.name == "nt" else "clear")
    return None


def mostrar_menu_principal():
    """Muestra el menú principal."""
    menu = [["1. Buscar libros", "2. Devolver Libros", "3. Salir del programa"]]
    titulo = "MENÚ PRINCIPAL"
    print(titulo.center(65, " "))
    print("=" * 65)
    print(
        tabulate(menu, tablefmt="fancy_grid", colalign=("center", "center", "center"))
    )
    print("=" * 65)
    return None


def mostrar_submenu_buscar_libro():
    """Muestra el submenú para buscar libros."""
    submenu = [
        [
            "1. Buscar por tí1tulo",
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
    return None


def main_menu():
    """Esta funcion controla el flujo del programa."""

    while True:
        clear_screen()
        mostrar_menu_principal()
        choice = input("\n...Seleccione una opción: ")
        match choice:
            case "1":  # BUSCAR LIBRO
                while True:
                    clear_screen()
                    mostrar_submenu_buscar_libro()
                    choice = input("\n...Seleccione una opción: ")
                    match choice:
                        case "1":  # Busqueda de libros por titulo
                            pass
                        case "2":  # Busqueda de libros por autor
                            pass
                        case "3":  # Busqueda de libros por genero
                            pass
                        case "4":  # Volver al menu principal
                            break
                        case _:
                            clear_screen()
                            input(
                                "Opción no válida, intente de nuevo. Presione ENTER para continuar."
                            )
                            continue
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
    return None


if __name__ == "__main__":
    main_menu()
