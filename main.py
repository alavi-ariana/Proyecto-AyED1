"""
Esto es un programa de gestion de una biblioteca.
"""
def choice_menu():
    """
    Opciones del menu.
    """
    print("\nMenú Principal:")
    print("1. Ver libros por género")
    print("2. Ver libros por autor")
    print("3. Buscar libro por título")
    print("4. Pedir prestado un libro")
    print("5. Devolver un libro")
    print("6. Dejar una review")
    print("7. Salir del programa")
    return None

def main_menu():
    """
    Menu principal.
    """
    while True:

        choice_menu()
        choice = input("...Seleccione una opción: ")
        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
    return None


if __name__ == "__main__":
    main_menu()
    