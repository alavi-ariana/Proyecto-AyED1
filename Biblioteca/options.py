"""Funciones para cada una de las opciones del menu principal"""

from read_write import leer_csv


def buscar_por_titulo(libros, titulo):
    """Busca libros por título."""
    return [libro for libro in libros if titulo.lower() in libro["title"].lower()]


def buscar_por_autor(libros, autor):
    """Busca libros por autor."""
    return [libro for libro in libros if autor.lower() in libro["author"].lower()]


def buscar_por_genero(libros, genero):
    """Busca libros por género."""
    return [libro for libro in libros if genero.lower() in libro["genre"].lower()]


def buscar_libros(libros):
    """Permite al usuario buscar libros por título, autor o género."""
    print("Seleccione el criterio de búsqueda:")
    print("1. Título")
    print("2. Autor")
    print("3. Género")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        resultados = buscar_por_titulo(libros, titulo)
    elif opcion == "2":
        autor = input("Ingrese el autor del libro: ")
        resultados = buscar_por_autor(libros, autor)
    elif opcion == "3":
        genero = input("Ingrese el género del libro: ")
        resultados = buscar_por_genero(libros, genero)
    else:
        print("Opción no válida.")
        return

    if resultados:
        print("Libros encontrados:")
        for libro in resultados:
            print(
                f"ISBN: {libro['isbn-13']}, Título: {libro['title']}, Autor: {libro['author']}, Género: {libro['genre']}, Stock: {libro['stock']}"
            )
    else:
        print("No se encontraron libros que coincidan con el criterio de búsqueda.")


ruta_books_csv = r"C:\Users\User\Desktop\NOTAS\THONNY - VS CODE\Algoritmo y Estructura de Datos II\PROYECTO_AyED1\Biblioteca\CSV\books.csv"
libros = leer_csv(ruta_books_csv)


buscar_libros(libros)
