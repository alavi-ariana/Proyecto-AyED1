import csv
import json
import os
from typing import List

def leer_libros() -> List:
    """ Lectura del archivo CSV que contiene la información de cada libro.
    Returns:
        - List: Una lista de diccionarios donde cada diccionario representa un libro con detalles
                como 'isbn-13', 'title', 'author', 'genre', y 'stock'.
    """
    directorio = os.getcwd()
    file_libros = os.path.join(
        directorio, "Biblioteca", "CSV", "books.csv"
        )
    try:
        with open (file_libros, newline='', encoding='UTF-8') as libros:
            lector = csv.DictReader(libros)
            datos = [linea for linea in lector]
    except FileNotFoundError:
        print("Error: No se encontró el archivo csv.")
        return []
    except csv.Error as e:
        print(f"Error al leer el archivo CSV: {e}")
        return []

    return datos

def leer_prestamos() -> List:
    """ Lectura del archivo json que contiene información sobre libros prestados.
    Returns:
        - List: Una lista de diccionarios donde cada diccionario representa un registro un libro
                prestado. Cada diccionario contiene detalles relacionados con el libro prestado,
                como el 'isbn-13' y 'quien lo retira'.
    """
    directorio = os.getcwd()
    file_prestamos = os.path.join(
        directorio, "Biblioteca", "JSON", "prestamos.json"
        )
    try:
        with open (file_prestamos, 'r', encoding='UTF-8') as prestamos:
            lector = json.load(prestamos)
            datos = [linea for linea in lector]
    except FileNotFoundError:
        print(f'El archivo {file_prestamos} no se encontró.')
        return []
    except json.JSONDecodeError:
        print(f'Error al decodificar el archivo JSON en {file_prestamos}.')
        return []

    return datos

"""def leer_usuarios() -> List:
    Lectura del archivo donde se guardan los usuarios registrados.
    Returns:
        - List: Una lista de diccionarios donde cada diccionario representa un usuario registrado.
                Cada diccionario contiene el dni junto el nombre.
    
    directorio = os.getcwd()
    file_usuarios = os.path.join(
        directorio, "Biblioteca", "JSON", "usuarios.json"
    )
    try:
        with open (file_usuarios, 'r', encoding='UTF-8') as usuarios:
            lector = json.load(usuarios)
            datos = [linea for linea in lector]
    except FileNotFoundError:
        print(f'El archivo {file_usuarios} no se encontró.')
        with open(file_usuarios, 'w', encoding='UTF-8') as usuarios:
            json.dump([usuarios, indent=4, ensure_ascii=False])
        return []
    except json.JSONDecodeError:
        print(f'Error al decodificar el archivo JSON en {file_usuarios}.')
        return []

    return datos
"""