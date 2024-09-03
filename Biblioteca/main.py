"""
Esto es un programa para la gestion de una biblioteca.
"""
import json
import csv



                            #ESCRITURA Y LECTURA - JSON Y CSV
def read_json(ruta):
    """
    Lee un archivo JSON y devuelve su contenido como un objeto (lista o diccionario).

    Pre:
        - ruta (str): La ruta del archivo JSON a leer.

    Post:
        - dict/list: El contenido del archivo JSON como diccionario o lista.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo {ruta} no se encontró.")
    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar el archivo JSON {ruta}.")
    return None


def read_csv(ruta):
    """
    lee un archivo CSV y devuelve su contenido como una lista de diccionarios.

    Pre:
        - ruata (str): La ruta del archivo CSV a leer.

    Post:
        -list: Una lista de diccionarios donde cada diccionario representa una fila del archivo CSV.
    """
    books = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                books.append(fila)
    except FileNotFoundError:
        print(f"Error: El archivo {ruta} no se encontró.")
    except csv.Error:
        print(f"Error: No se pudo leer el archivo CSV {ruta}")
    return books



                            #MENU PRINCIPAL
def choice_menu():
    """
    Funcion que muestra las opciones del menu principal para el usuario.
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
    Controla el flujo del programa mostrando el menu principal y 
    ejecutando las opciones seleccionadas por el usuario.
    """
    books = read_csv("datos/archivos_csv/books.csv")
    borrowed_books = read_json("datos/archivos_json/stock.json")
    reviews = read_json("datos/archivos_json/review.json")

    while True:

        choice_menu()
        choice = input("...Seleccione una opción: ")
        match choice:
            case "1":
                view_books_by_genre(books)
            case "2":
                view_books_by_author(books)
            case "3":
                search_book_by_title(books)
            case "4":
                borrow_book(books, borrowed_books)
                #Funcion - Escritura csv ?
            case "5":
                return_book(borrowed_books)
                #Funcion - Escritura json ?
            case "6":
                leave_review(reviews)
                #Funcion - Escritura json ?
            case "7":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
    return None



                            #FUNCIONES DE CADA OPCION DEL MENU PRINCIPAL
def view_books_by_genre(books):
    """
    Muestra los libros disponibles por género.
    """

def view_books_by_author(books):
    """
    Muestra los libros disponibles por autor.
    """

def search_book_by_title(books):
    """
    Busca un libro por su título y muestra la información correspondiente.
    """

def borrow_book(books, burrowed_books):
    """
    Permite al usuario pedir prestado un libro.
    """

def return_book(burrowed_books):
    """
    Permite al usuario devolver un libro prestado.
    """

def leave_review(reviews):
    """
    Permite al usuario dejar una reseña para un libro.
    """


if __name__ == "__main__":
    main_menu()
