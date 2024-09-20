"""Funciones para la lectura y escritura de los archivos JSON y CSV"""

import json
import csv


def leer_csv(nombre_archivo):
    """Lee un archivo CSV y devuelve una lista de diccionarios."""
    with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)
