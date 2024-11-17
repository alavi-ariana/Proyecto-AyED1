import re
import time
import os
from typing import List
from funciones import funciones as funciones

def search_(buscar: str, opcion: str) -> List:
    """ Busca libros basados en un termino de busqueda y una opción.
    Args:
        - buscar (str): El termino a buscar en la opción especifica.
        - opcion (str): El espacio a buscar en los libros (e.g., 'title', 'author').
    Returns:
        - list: Una lista de diccionarios donde cada diccionario representa un libro
            que coincide con el término a buscar. Cada diccionario contiene los detalles
            del libro, como título, autor, etc"""
    libros = funciones.leer_libros()

    pattern = re.compile(re.escape(buscar), re.IGNORECASE)
    return [libro for libro in libros if pattern.search(libro[opcion])]

def busqueda_titulo(title: str) -> List[str]:
    """Retorna una lista de nombres de libros que coinciden con la busqueda proporcionada.
        Args:
            - title: tiene que ser un string.
        Returns:
            - list: contiene elementos string.
    """
    return search_(title, 'title')

def imprimir_coincidencias(coincidencias: List[str]) -> None:
    """ Imprime en pantalla (dependiendo de cuántos items contiene coincidencias) 
        los items en coincidencias.
        Args:
            - coincidencias: una lista con elementos str.
        Returns:
            - None
    """
    if len(coincidencias) > 1:
        for i, libro in enumerate(coincidencias, 1):
            print(f"{i}. {libro['title']} - {libro['author']} - {coincidencias[0]['isbn-13']}")
    elif len(coincidencias) == 1:
        print(f"{coincidencias[0]['title']} - {coincidencias[0]['author']}")
    else:
        print("El libro no fue encontrado.")
        time.sleep(0.75)

def seleccion_libro(coincidencias: List[str]) -> str:
    """Se le solicita al usuario que seleccione un libro, de esa selección se busca en los indices
    de coincidencias y retorna la información del libro.
        Args:
            - coincidencias: lista con elementos tipo string.
        Returns:
            - str: la información del libro.
    """
    seleccion = input("Seleccione su libro: ").strip()
    try:
        if not seleccion.isdigit():
            raise ValueError("Debe ingresar un número entero.")
        return coincidencias[int(seleccion) - 1]
    except ValueError as e:
        print(e)
    except IndexError:
        print("Libro no se encuentra entre las opciones.")

def ver_reviews(libro):
    directorio = os.getcwd()
    file_path = os.path.join(directorio, 'Biblioteca', 'JSON', 'reviews.json')
    datos = funciones.leer_json(file_path)
    #print(libro['title'])
    if datos:
        encontrado = False
        for book, info in datos.items():
            if book.lower().strip() == libro['title'].lower().strip():
                encontrado = True
                reviews = info.get('reviews', [])
                print(f"{libro['title']}")
                for review in reviews:
                    print(f'"- {review}"')
                break
        if not encontrado:
            print("El libro no tiene reviews.")
    else:
        print("No hay reviews en la base de datos.")