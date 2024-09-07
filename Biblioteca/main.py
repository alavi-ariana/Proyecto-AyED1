"""MENÚ PRINCIPAL"""


def main_menu():
    "Esta funcion controla el flujo del programa"

    while True:
        print("\nMENÚ PRINCIPAL")
        for key in ["1", "2"]:
            print(f"{key}: {main_choices[key]}")

        choice = input("...Seleccione una opción: ")
        match choice:

            case "1":
                sub_opciones = ["1.1", "1.2", "1.3", "1.4"]
                for key in sub_opciones:
                    print(f"{key}: {main_choices[key]}")

                choice = input("...Seleccione una opción: ")
                match choice:
                    case "1.1":  # Busqueda de libros por titulo
                        pass
                    case "1.2":  # Busqueda de libros por autor
                        pass
                    case "1.3":  # Busqueda de libros por genero
                        pass
                    case "1.4":  # Volver al menu principal
                        return

            case "2":
                pass

            case _:
                print("\n...Opción no válida, intente de nuevo.")
                continue

    return None


main_choices = {
    "1": "Buscar libro",
    "1.1": "Buscar por titulo",
    "1.2": "Buscar por autor",
    "1.3": "Buscar por genero",
    "1.4": "Volver al menu principal",
    "2": "Devolver libro",
}

if __name__ == "__main__":
    main_menu()
