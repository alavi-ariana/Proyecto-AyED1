import re
import time
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

def busqueda_titulo(title: str):
    coincidencias = search_(title, 'title')
    if len(coincidencias) > 1:
        for i, libro in enumerate(coincidencias, 1):
            print(f"{i}. {libro['title']} - {libro['author']} - {coincidencias[0]['isbn-13']}")
    elif len(coincidencias) == 1:
        print(f"{coincidencias[0]['title']} - {coincidencias[0]['author']}")
    else:
        print("El libro no fue encontrado.")
        time.sleep(0.75)

#def seleccion_libro():