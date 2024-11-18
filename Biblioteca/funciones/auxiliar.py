import csv
import json
import os
from typing import List

def leer_libros() -> List:
    """
    Lectura del archivo CSV que contiene la informacion de cada libro.
    - Argumentos:
        - Ninguno
    - Retorna:
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
        print("Error: No se encontro el archivo csv.")
        return []
    except csv.Error as e:
        print(f"Error al leer el archivo CSV: {e}")
        return []

    return datos

def leer_usuarios() -> List:
    """
    Lectura del archivo JSON donde se guardan los usuarios registrados.
    - Argumentos:
        - Ninguno
    - Retorna:
        - List: Una lista de diccionarios con la informacion de los usuarios.
    """
    directorio = os.getcwd()
    file_usuarios = os.path.join(directorio, "Biblioteca", "JSON", "usuarios.json")
    
    # Verifica si el archivo existe, si no lo crea
    if not os.path.exists(file_usuarios):
        print(f"El archivo {file_usuarios} no existe, se creara uno nuevo.")
        with open(file_usuarios, 'w', encoding='UTF-8') as usuarios:
            json.dump([], usuarios, indent=4, ensure_ascii=False)
        return []  # Devuelve lista vacía porque no hay usuarios registrados aún
    
    try:
        with open(file_usuarios, 'r', encoding='UTF-8') as usuarios:
            datos = json.load(usuarios)
    except json.JSONDecodeError:
        # Si el archivo tiene un formato incorrecto, lo inicializamos con una lista vacía
        print(f"Error al decodificar el archivo JSON en {file_usuarios}. Inicializando archivo.")
        with open(file_usuarios, 'w', encoding='UTF-8') as usuarios:
            json.dump([], usuarios, indent=4, ensure_ascii=False)
        datos = []
    return datos

def leer_json(file_path: str) -> List:
    """
    Lee un archivo JSON y devuelve su contenido como una lista.
    - Argumentos:
        - file_path: Ruta del archivo JSON a leer.
    - Retorna:
        - List: El contenido del archivo JSON, o una lista vacia si ocurre un error.
    """
    try:
        with open(file_path, 'r', encoding='UTF-8') as lectura_json:
            datos = json.load(lectura_json)
    except FileNotFoundError:
        # Si el archivo no existe, devuelve una lista vacia
        print(f"El archivo {file_path} no existe, se creara uno nuevo.")
        return []  # Retorna una lista vacia si el archivo no existe
    except json.JSONDecodeError:
        # Si hay un error en el formato del JSON, devuelve una lista vacia
        print(f"Error al decodificar el archivo JSON en {file_path}. Inicializando archivo.")
        # Si el archivo esta danado o tiene un formato incorrecto, lo inicializamos con un array vacio
        with open(file_path, 'w', encoding='UTF-8') as archivo:
            json.dump([], archivo, indent=4)
        return []  # Retorna una lista vacia despues de inicializar el archivo vacio
    return datos

def guardar_json(file_path: str, datos: List) -> None:
    """
    Guarda los datos (ya sean listas o diccionarios) en un archivo JSON.
    - Argumentos:
        - file_path: Ruta donde se guardara el archivo JSON.
        - datos: Los datos a guardar en el archivo JSON.
    - Retorna:
        - Ninguno
    """
    try:
        with open(file_path, 'w', encoding='UTF-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar el archivo {file_path}: {e}")

def leer_prestamos() -> List:
    """
    Lectura del archivo JSON que contiene los prestamos de libros.
    - Argumentos:
        - Ninguno
    - Retorna:
        - List: Una lista de diccionarios que representa los prestamos registrados.
    """
    directorio = os.getcwd()
    file_prestamos = os.path.join(directorio, "Biblioteca", "JSON", "prestamos.json")
    try:
        with open(file_prestamos, 'r', encoding='UTF-8') as prestamos_file:
            return json.load(prestamos_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna una lista vacia si el archivo no existe o hay un error al leerlo
    
def guardar_prestamos(prestamos: List) -> None:
    """
    Guarda los prestamos en el archivo JSON.
    - Argumentos:
        - prestamos: Lista de diccionarios con los prestamos a guardar.
    - Retorna:
        - Ninguno
    """
    directorio = os.getcwd()
    file_prestamos = os.path.join(directorio, "Biblioteca", "JSON", "prestamos.json")
    with open(file_prestamos, 'w', encoding='utf-8') as prestamos_file:
        json.dump(prestamos, prestamos_file, indent=4)
