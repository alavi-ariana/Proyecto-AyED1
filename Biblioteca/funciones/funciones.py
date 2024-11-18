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

def leer_prestamos() -> dict:
    '''
    Lee el archivo de préstamos y devuelve los datos de los préstamos registrados

    Pre:
        No recibe ningún parámetro
    Post:
        Devuelve un diccionario con los datos de los préstamos, en caso contrario se muestra el error correspondiente o se crea el archivo
    '''
    directorio = os.getcwd()
    file_prestamos = os.path.join(directorio, "Biblioteca", "JSON", "prestamos.json")
    datos_leidos = {}
    try:
        with open(file_prestamos, 'r', encoding='UTF-8') as prestamos:
            try:
                datos_leidos = json.load(prestamos)
            except json.JSONDecodeError:
                print(f"Error al decodificar el archivo JSON en {file_prestamos}")
                with open(file_prestamos, 'w', encoding='utf-8') as prestamos:
                    json.dump(datos_leidos, prestamos, indent=4)
    except FileNotFoundError:
        with open(file_prestamos, 'w', encoding='utf-8') as prestamos:
            json.dump(datos_leidos, prestamos, indent=4)
        print(f"El archivo {file_prestamos} no existía. Se creó uno nuevo.")
    except Exception as e:
        print(f"Error desconocido al leer el archivo {file_prestamos}: {e}")
    return datos_leidos

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

def leer_json(file_path):
    try:
        with open(file_path, 'rt', encoding='UTF-8') as lectura_json:
            datos = json.load(lectura_json)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

    return datos