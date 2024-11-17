import os
import json

def solicitar_dni():
    while True:
        dni = input("Ingrese el DNI del cliente: ")
        if len(dni) == 8 and dni.isdigit():
            return dni
        else:
            print("Error. DNI inválido.")

def leer_prestamos():
    directorio = os.getcwd()
    file_prestamos = os.path.join(
        directorio, "Biblioteca", "JSON", "prestamos.json"
        )
    datos_leidos = {}
    try:
        with open(file_prestamos, 'r', encoding='UTF-8') as prestamos:
            datos_leidos = json.load(prestamos)
    except FileNotFoundError:
        print(f'El archivo {file_prestamos} no se encontró.')
    except json.JSONDecodeError:
        print(f'Error al decodificar el archivo JSON en {file_prestamos}.')
    return datos_leidos

def mostrar_libros(libros):
    print("\nLibros prestados:")
    for i, libro in enumerate(libros, 1):
        print(f"{i}. {libro['title']} - Fecha de préstamo: {libro['fecha_de_prestamo']}")

def seleccionar_libro(libros):
    try:
        num_libro = int(input("\nIngrese el número del libro que desea devolver: "))
        if num_libro >= 1 and num_libro <= len(libros):
            return num_libro
    except ValueError:
        return None

def guardar_prestamos(prestamos):
    directorio = os.getcwd()
    file_prestamos = os.path.join(
        directorio, "Biblioteca", "JSON", "prestamos.json"
        )
    try:
        with open(file_prestamos, 'w', encoding='utf-8') as arch_prestamos:
            json.dump(prestamos, arch_prestamos, indent=4)
    except FileNotFoundError:
        print(f'El archivo {file_prestamos} no se encontró.')
    except json.JSONDecodeError:
        print(f'Error al decodificar el archivo JSON en {file_prestamos}.')

def gestionar_review(libro_devuelto):
    op = input("¿Desea dejar una review del libro? (s/n): ").lower()
    if op == 's':
        review = input("Escriba su review: ")
        if review:
            try:
                with open('Biblioteca/JSON/reviews.json', 'r+', encoding='utf-8') as leer_reviews:
                    try:
                        reviews = json.load(leer_reviews)
                    except json.JSONDecodeError:
                        reviews = {}
            except FileNotFoundError:
                reviews = {}

            titulo_libro = libro_devuelto['title']
            if titulo_libro in reviews:
                reviews[titulo_libro]['reviews'].append(review)
            else:
                reviews[titulo_libro] = {'reviews': [review]}

            with open('Biblioteca/JSON/reviews.json', 'w', encoding='utf-8') as escribir_reviews:
                json.dump(reviews, escribir_reviews, indent=4)

            print("¡Gracias por dejar su review!")
        else:
            print("Error. La review no puede estar vacía.")

def devolver_libro():
    dni = solicitar_dni()
    prestamos = leer_prestamos()

    if dni in prestamos:
        prestamo = prestamos[dni]
        libros_prestados = prestamo.get('libros_prestados', [])

        if libros_prestados:
            mostrar_libros(libros_prestados)
            num_libro = seleccionar_libro(libros_prestados)

            if num_libro is not None:
                libro_devuelto = libros_prestados.pop(num_libro - 1)
                prestamos[dni]['cantidad_libros_prestados'] -= 1
                guardar_prestamos(prestamos)
                print(f"El libro '{libro_devuelto['title']}' ha sido devuelto exitosamente.")
                gestionar_review(libro_devuelto)
            else:
                print("Error. Número de libro no válido.")
        else:
            print("Error. Este DNI no tiene libros prestados.")
    else:
        print("Error. No se encontraron libros prestados para este DNI.")

    