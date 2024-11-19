import os
from typing import List, Dict
from tabulate import tabulate


def clear_screen() -> None:
    """
    Limpia la pantalla para mejorar la visualizacion.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    os.system("cls" if os.name == "nt" else "clear")


def visualizacion_menu_principal() -> None:
    """
    Muestra el menu principal.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    menu = [["1. Buscar libros", "2. Devolver Libros", "3. Salir del programa"]]
    titulo = "MENU PRINCIPAL"
    print(titulo.center(65, " "))
    print("=" * 65)
    print(
        tabulate(menu, tablefmt="fancy_grid", colalign=("center", "center", "center"))
    )
    print("=" * 65)


def visualizacion_submenu_buscar_libro() -> None:
    """
    Muestra el submenu para buscar libros.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    submenu = [
        [
            "1. Buscar por titulo",
            "2. Buscar por autor",
            "3. Buscar por genero",
            "4. Volver al menu principal",
        ]
    ]
    titulo = "BUSCAR LIBRO"
    print(titulo.center(100, " "))
    print("=" * 100)
    print(
        tabulate(
            submenu,
            tablefmt="fancy_grid",
            colalign=("center", "center", "center", "center"),
        )
    )
    print("=" * 100)


def visualizacion_menu_libro_encontrado(libro: dict) -> None:
    """
    Muestra el menú de interacción para un libro específico.
    - Argumentos:
        - libro (dict): Diccionario con los detalles del libro seleccionado.
    - Retorna:
        - None
    """
    menu = [["1. Pedir prestado", "2. Ver reviews", "3. Volver al menú principal"]]
    titulo = f"{libro['title']} - {libro['author']}"
    print(titulo.center(65, " "))
    print("=" * 65)
    print(
        tabulate(menu, tablefmt="fancy_grid", colalign=("center", "center", "center"))
    )
    print("=" * 65)


def visualizacion_generos(generos: List[str], max_columnas: int = 4) -> None:
    """
    Muestra los generos disponibles en un formato tabular numerado.
    - Argumentos:
        - generos (List[str]): Lista de generos disponibles.
        - max_columnas (int): Número máximo de columnas para el formato tabular.
    - Retorna:
        - None
    """
    # Enumerar los generos para que el usuario vea el número
    enumerados = [f"{i + 1}. {genero}" for i, genero in enumerate(generos)]

    # Crear un único bloque de datos para la tabla en una sola línea
    tabla = [enumerados]

    # Imprimir el menú con los géneros numerados en una línea continua
    print("\n" + "GENEROS".center(107, " "))
    print("=" * 107)
    print(tabulate(tabla, tablefmt="fancy_grid", numalign="center"))
    print("=" * 107)


def visualizar_coincidencias(coincidencias: List[Dict]) -> None:
    """
    Visualiza las coincidencias encontradas en formato tabular.
    - Argumentos:
        - coincidencias (List[Dict]): Lista de diccionarios que representan los libros encontrados.
    - Retorna:
        - None
    """
    if coincidencias:
        # Agregar números para enumerar las coincidencias
        tabla = [
            [i + 1, libro["title"], libro["author"], libro["genre"]]
            for i, libro in enumerate(coincidencias)
        ]
        print("\nLibros encontrados:")
        print(
            tabulate(
                tabla,
                headers=["#", "Título", "Autor", "Género"],
                tablefmt="fancy_grid",
                colalign=("center", "center", "center"),
            )
        )
    else:
        print("No se encontraron libros que coincidan con la búsqueda.")


def visualizar_prestamo_libro(libro: Dict) -> None:
    """
    Muestra la información detallada sobre un libro en formato tabular.
    - Argumentos:
        - libro (Dict): Diccionario con los detalles del libro.
    - Retorna:
        - None
    """
    mensaje = [
        ["Libro", libro["title"]],
        ["Autor", libro["author"]],
        ["Género", libro["genre"]],
    ]
    print(
        tabulate(
            mensaje,
            headers=["Detalle", "Información"],
            tablefmt="fancy_grid",
            colalign=("left", "center"),
        )
    )
