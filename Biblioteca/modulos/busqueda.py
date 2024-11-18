import re
import time
import os
from typing import List
from funciones import funciones

def search_(buscar: str, opcion='title') -> List:
    """ Busca libros basados en un termino de busqueda y una opción.
    Args:
        - buscar (str): El termino a buscar en la opción especifica.
        - opcion (str): El espacio a buscar en los libros (e.g., 'title', 'author').
    Returns:
        - list: Una lista de diccionarios donde cada diccionario representa un libro
            que coincide con el término a buscar. Cada diccionario contiene los detalles
            del libro, como título, autor, etc"""
    libros = funciones.leer_libros()
    if not libros:
        raise ValueError("La lista de libros está vacia o no se pudo leer.")
    if not all(opcion in libro for libro in libros):
        raise ValueError(f"La opción '{opcion}' no es válida en los datos de libros.")

    buscar_normalizado = re.sub(r'[^a-zA-Z0-9\s]', '', buscar.lower().strip())
    pattern = re.compile(re.escape(buscar_normalizado), re.IGNORECASE)
    resultados = [
        libro for libro in libros
        if pattern.search(re.sub(r'[^a-zA-Z0-9\s]', '', libro[opcion].lower().strip()))
        ]
    return resultados

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
        print(f"1. {coincidencias[0]['title']} - {coincidencias[0]['author']}")
    else:
        print("El libro no fue encontrado.")
        time.sleep(0.75)

def imprimir_generos() -> List[str]:
    libros = funciones.leer_libros()
    generos = list(set(dato['genre'] for dato in libros))
    for i, genero in enumerate(generos, 1):
        print(f"{i}. {genero}")
    return generos

def busqueda_genero(genero_op) -> List:
    libros = funciones.leer_libros()
    genero_op = genero_op.lower().strip()
    return [libro for libro in libros if libro['genre'].lower().strip() == genero_op]

def seleccion_genero(generos):
    genero_op = input("Seleccione el género: ").strip()
    try:
        if not genero_op.isdigit():
            raise ValueError("Debe ingresar un número entero.")
        indice = int(genero_op)
        if indice < 1 or indice > len(generos):
            raise IndexError("La opción no se encuentre entre los géneros.")
        return generos[indice - 1]
    except ValueError as e:
        print(e)
        return None
    except IndexError as e:
        print(e)
        return None

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
        seleccion = int(seleccion)
        if seleccion < 1 or seleccion > len(coincidencias):
            raise IndexError("La opción no se encuentra entre los libros.")
        return coincidencias[seleccion - 1]
    except ValueError as e:
        print(e)
        return None
    except IndexError as e:
        print(e)
        return None

def ver_reviews(libro: str) -> None:

    if libro is None:
        print("No se seleccionó un libro válido.")
        return

    directorio = os.getcwd()
    file_path = os.path.join(directorio, 'Biblioteca', 'JSON', 'reviews.json')
    datos = funciones.leer_json(file_path)

    if datos:
        titulo_libro = libro['title'].lower().strip()
        encontrado = False

        for book, info in datos.items():
            if book.lower().strip() == titulo_libro:
                encontrado = True
                reviews = info.get('reviews', [])
                if reviews:
                    print(f"Reviews para '{libro['title']}':")
                    for review in reviews:
                        print(f'"  - {review}"')
                else:
                    print(f"El libro {libro['title']} no tiene reviews.")
                break
        if not encontrado:
            print("El libro no tiene reviews.")
    else:
        print("No hay reviews en la base de datos.")

