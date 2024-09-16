"""Programa para armar funciones que se van a utilizar en el programa principal."""
import csv
import json
import os
import re

def leer_prestamos() -> list:
    """ Reads the JSON file containing information about borrowed books and 
        returns it as a list of dictionaries.

    Returns:
        list: A list of dictionaries where each dictionary represents a borrowed book record. Each
            dictionary contains details related to the book loan, such as 'isbn-13', 'borrower', and
            'borrowed_date'."""
    directorio = os.getcwd()
    file_prestamos = os.path.join(
        directorio, "Proyecto-AyED1", "Biblioteca", "JSON", "prestamos.json"
        )
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
    """ Reads the CSV file containing book information and returns it as a list of dictionaries.

    Returns:
        list: A list of dictionaries where each dictionary represents a book with details such as
            'isbn-13', 'title', 'author', 'genre', and 'stock'. Each dictionary corresponds to
            a row in the CSV file."""
    directorio = os.getcwd()
    file_libros = os.path.join(
        directorio, "Proyecto-AyED1", "Biblioteca", "CSV", "books.csv"
        )
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
    """ Search for books based on a given search term and option.

    Args:
        buscar (str): The search term to look for in the specified option.
        opcion (str): The field to search within the book records (e.g., 'title', 'author').

    Returns:
        list: A list of dictionaries where each dictionary represents a book
            that matches the search term in the specified field. Each book dictionary
            contains the details of the book, such as 'title', 'author', etc."""
    libros = leer_libros()

    pattern = re.compile(re.escape(buscar), re.IGNORECASE)
    coincidencias = []
    for libro in libros:
        if pattern.search(libro[opcion]):
            coincidencias.append(libro)

    return coincidencias
