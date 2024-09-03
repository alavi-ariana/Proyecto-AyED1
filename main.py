def choice_menu(): #Menu estandar, posibles modificaciones a futuro.
    print("\nMenú Principal:")
    print("1. Ver libros por género")
    print("2. Ver libros por autor")
    print("3. Buscar libro por título")
    print("4. Pedir prestado un libro")
    print("5. Devolver un libro")
    print("6. Dejar una review")
    print("7. Salir")
    return None

def main_menu():

    while True:

        choice_menu()
        choice = input("...Seleccione una opción: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            break
        else: 
            print("Opción no válida. Intente de nuevo.")
    return None


if __name__ == "__main__":
    main_menu()

