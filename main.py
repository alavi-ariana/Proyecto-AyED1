"""
Esto es un programa de gestion de una biblioteca.
"""
import json
import csv


                        #ESCRITURA Y LECTURA - JSON Y CSV
def read_json(ruta):
    """
    Lee un archivo JSON y devuelve su contenido como un objeto de Python (lista o diccionario).
    IMPORTANTE/PENTIENDE - Archivo JSON pendiente a escribir.
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def read_csv(ruta):
    """
    lee un archivo CSV y devuelve su contenido como una lista de diccionarios.
    IMPORTANTE/PENDIENTE - Revisar archivo CSV.
    """
    books = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            books.append(fila)
        return books


                        #MENU PRINCIPAL
def choice_menu():
    """
    Funcion que muestra las opciones para el usuario.
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
    Funcion del menu principal que controla el flujo del programa.
    """
    book = read_csv("datos/archivos_csv/books.csv")
    borrowed_book = read_json("datos/archivos_json/stock.json")
    review = read_json("datos/archivos_json/review.json")

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
