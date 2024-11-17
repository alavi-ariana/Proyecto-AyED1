### Proyecto para parcial 1 y parcial 2, que debemos defender en la entrega final.

## Integrantes del equipo:
- Serena puertas
- Juana Lopez
- Keila Gimenez
- Ariana Luna

## Tema del proyecto:
Sistema de gestión de biblioteca.

# Biblioteca:
- Libros (.csv): 
    Hay distintos géneros para seleccionar y dependiendo de qué selecciona se muestran los libros pertenecientes a él.
    Se puede seleccionar la opción de ver toda la libreria.
    La busqueda de cada libro se puede hacer mediante el género o el autor. 
    isbn para la devolución del libros.
    Regex para géneros y nombres del libro.
- Disponibilidad de libro: Disponible: se puede pedir prestado / No disponible: no se puede pedir; dependiendo del stock de cada libro.

# Sistema:
Un único usuario que administra (El recepcionista de la biblioteca)
- un .json para poner los libros que se van pidiendo y la cantidad de stock restante
- un .json con el nombre del libro y su puntuación.

# Menu:
1) Buscar libro.
    1) Género
    2) Título
    3) Autor

    Las 3 muestran los libros que coinciden con la busqueda y los muestran enúmerados para que puedas elegir el libro, se muestran las siguientes opciones.
    1) Pedir prestado
        Se solicita dni para ver si está registrado, caso contrario se guarda en el csv. Se guarda el timestamp del momento de pedir el libro para llevar un seguimiento de la devolución.
        Si se tiene demora en la devolución de algun libro, no se le deja pedir más libros prestados.
    2) Ver reviews
    
2) Devolver libro.
    Se solicita dni para ver los libros que tiene para devolver.
    Una vez devuelto tiene la opción de si quiere dejar una review o no.
3) Salir del programa.

Para usar:

    import csv
    import json
    import os
    import random
    import re
    import time
    from functools import reduce
    from typing import List, Dict, Tuple

## Información util.
