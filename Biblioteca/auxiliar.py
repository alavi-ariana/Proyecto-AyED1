"""Modulo de funciones auxiliares"""
import csv
import json
import os
import re

def leer_prestamos() -> list:
    """ 
    Lee el archivo JSON que contiene informacion sobre los prestamos de libros y
    devuelve el contenido como una lista de diccionarios.

    Post:
        -list: Una lista de diccionarios donde cada diccionario representa
        un registro de prestamo de libro. Cada diccionario contiene detalles 
        relacionados con el prestamo: 'isbn-13', 'borrower' y'borrowed_date'.
    """
    directorio = os.getcwd()
    file_prestamos = os.path.join(directorio, "Biblioteca", "JSON", "prestamos.json")
    datos_leidos = []
    try:
        with open (file_prestamos, 'r', encoding='UTF-8') as prestamos:
            datos = json.load(prestamos)
            for linea in datos:
                datos_leidos.append(linea)
    except FileNotFoundError:
        print(f'El archivo {file_prestamos} no se encontró.')
    except json.JSONDecodeError:
        print(f'Error al decodificar el archivo JSON en {file_prestamos}.')
    return datos_leidos

def leer_libros() -> list:
    """
    Lee un archivo CSV que contiene informacion sobre los libros y 
    devuelve el contenido como una lista de diccionarios.

    Post:
        -list: Una lista de diccionarios donde cada diccionario representa un
        libro con los detalles como: 'isbn-13', 'title', 'author', 'genre' y 'stock'. 
        Cada diccionario corresponde a una fila en el archivo CSV.
        
        """
    directorio = os.getcwd()
    file_libros = os.path.join(directorio, "Biblioteca", "CSV", "books.csv")
    libros_leidos = []
    try:
        with open (file_libros, newline='', encoding='UTF-8') as libros:
            lector = csv.DictReader(libros)
            for linea in lector:
                libros_leidos.append(linea)
    except FileNotFoundError:
        print("Error: No se encontró el archivo csv.")
    except csv.Error as e:
        print(f"Error al leer el archivo CSV: {e}")
    return libros_leidos

def search(buscar: str, opcion: str) -> list:
    """
    Busca libros segun lo que el usuario seleccione: Por autor, genero o titulo.

    Pre:
        -buscar (str): Opcion de busqueda que selecciono el usuario.
        -opcion (str): El campo en el que buscar dentro de los registros de libros.

    Post:
        -list: Una lista de diccionarios donde cada diccionario representa un 
        libro que coincide con el término de búsqueda en el campo especificado. 
        Cada diccionario de libro contiene los detalles del libro como 'title', 'author', etc.
    """
    libros = leer_libros()
    pattern = re.compile(re.escape(buscar), re.IGNORECASE)
    coincidencias = []
    for libro in libros:
        if pattern.search(libro[opcion]):
            coincidencias.append(libro)
    return coincidencias
