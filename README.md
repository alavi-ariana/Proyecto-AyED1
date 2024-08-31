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
1) Biblioteca. (mostrar disponibilidad del libro, el rating, reviews)
   
        a. Ver libros por género. ("quiero buscar en la sección fantasy")
            se muestran todos los libros pertenecientes del género.
            input = ingrese su libro de interes (-1 para salir)
    
        b. Ver libros por autor. ("quiero libros de j. k. rowling")
            se muestran todos los libros pertenecientes al autor.
            input = ingrese su libro de interes (-1 para salir)
    
        c. Busqueda de libro (mediante título) ("quiero buscar el libro 'harry potter'")
            si se encuentra el libro se mostrará la disponibilidad, el rating y reviews.

3) Prestamo de libros.
   
    a. Pedir prestado un libro. (se puede pedir 1 libro por cada ejecución del programa)

        I. Buscar por género.
        II. Buscar por autor.
        III. Buscar libro.
   una vez seleccionado el libro si tiene disponibilidad de stock se realiza la prestación del libro
   
    b. Devolver un libro. (se devuelve 1 libro por cada ejecución del programa)
   
   se muestran los libros prestados junto con su código.
   
   input = ingrese el código del libro a devolver
   
   se le suma al stock del libro.

5) Dejar una review.

        input = nombre del libro (-1 para salir)
    se le muestra un mensaje de "¿es este el libro que busca? SÍ / NO" caso de que sea sí:
   
        mensaje = opinión del libro
        puntuación = del 1 al 5
   
    caso contrario se vuelve a pedir nombre del libro.


Para usar:

    import csv
    import json
    import os
    import random
    import re
    from functools import reduce
    from typing import List
