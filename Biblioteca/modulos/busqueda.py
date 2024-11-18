import re
import time
import os
from funciones import funciones
from typing import List, Dict
from tabulate import tabulate

def search_(buscar: str, opcion: str) -> List[Dict]:
    """
    Busca libros basados en un termino de busqueda y una opcion.
    - Argumentos:
        - buscar (str): El termino a buscar en la opcion especificada.
        - opcion (str): El campo en el que se realiza la busqueda (e.g., 'title', 'author').
    - Retorna:
        - List[Dict]: Lista de diccionarios que representan los libros que coinciden con la busqueda.
    """
    libros = funciones.leer_libros()

    if not libros or opcion not in libros[0]:
        print(f"Error: La clave '{opcion}' no existe en los datos de los libros o los libros no se cargaron correctamente.")
        return []

    pattern = re.compile(re.escape(buscar), re.IGNORECASE)
    return [libro for libro in libros if pattern.search(libro[opcion])]

def busqueda_titulo(title: str) -> List[Dict]:
    """
    Busca libros por titulo.
    - Argumentos:
        - title (str): El titulo a buscar.
    - Retorna:
        - List[Dict]: Lista de diccionarios que representan los libros encontrados.
    """
    return search_(title, 'title')

from tabulate import tabulate

def imprimir_coincidencias(coincidencias: List[Dict]) -> None:
    """
    Imprime las coincidencias encontradas en una lista.
    - Argumentos:
        - coincidencias (List[Dict]): Lista de diccionarios que representan los libros encontrados.
    - Retorna:
        - None
    """
    if len(coincidencias) > 1:
        print("\nLibros encontrados:")
        tabla = [[libro['title'], libro['author'], libro['genre']] for libro in coincidencias]
        print(tabulate(tabla, headers=["Título", "Autor", "Género"], tablefmt="fancy_grid", colalign=("center", "center", "center")))
    elif len(coincidencias) == 1:
        libro = coincidencias[0]
        print(tabulate([[libro['title'], libro['author'], libro['genre']]], headers=["Título", "Autor", "Género"], tablefmt="fancy_grid", colalign=("center", "center", "center")))
    else:
        print("El libro no fue encontrado.")
        time.sleep(0.75)

def seleccion_libro(coincidencias: List[Dict]) -> Dict:
    """
    Permite al usuario seleccionar un libro de las coincidencias.
    - Argumentos:
        - coincidencias (List[Dict]): Lista de diccionarios que representan los libros encontrados.
    - Retorna:
        - Dict: Diccionario con la informacion del libro seleccionado.
    """
    while True:
        seleccion = input("\nSeleccione el numero del libro: ").strip()
        try:
            if not seleccion.isdigit():
                raise ValueError("Debe ingresar un numero entero.")
            indice = int(seleccion) - 1
            if indice < 0 or indice >= len(coincidencias):
                raise IndexError("Numero fuera de rango.")
            return coincidencias[indice]
        except (ValueError, IndexError) as e:
            print(e)

def ver_reviews(libro: Dict) -> None:
    """
    Muestra las reviews asociadas a un libro especifico.
    - Argumentos:
        - libro (Dict): Diccionario con la informacion del libro.
    - Retorna:
        - None
    """
    directorio = os.getcwd()
    file_path = os.path.join(directorio, 'Biblioteca', 'JSON', 'reviews.json')
    datos = funciones.leer_json(file_path)
    isbn = libro.get('isbn-13')

    if datos and isbn in datos:
        reviews = datos[isbn].get('reviews', [])
        print(f"\nReviews para el libro '{libro['title']}':")
        if reviews:
            for review in reviews:
                print(f"- {review}")
        else:
            print("Este libro no tiene reviews.")
    else:
        print("Este libro no tiene reviews o no se encontro en la base de datos.")
