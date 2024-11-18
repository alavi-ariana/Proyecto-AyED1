from funciones import auxiliar
from typing import Dict

def solicitar_dni() -> str:
    """
    Solicita el DNI del usuario.
    - Argumentos:
        - Ninguno
    - Retorna:
        - str: El DNI del usuario.
    """
    while True:
        dni = input("Ingrese el DNI del cliente: ")
        if len(dni) == 8 and dni.isdigit():
            return dni
        print("Error. DNI invalido.")

def devolver_libro() -> None:
    """
    Gestiona la devolucion de un libro.
    - Argumentos:
        - Ninguno
    - Retorna:
        - None
    """
    dni = solicitar_dni()
    prestamos = auxiliar.leer_json('Biblioteca/JSON/prestamos.json')  # Usar la funcion auxiliar
    
    # Filtrar los prestamos por DNI
    prestamos_usuario = [p for p in prestamos if p['dni'] == dni]
    if not prestamos_usuario:
        print("No se encontraron libros prestados para este DNI.")
        return

    # Mostrar libros prestados al usuario
    print("\nLibros prestados:")
    for i, prestamo in enumerate(prestamos_usuario, 1):
        print(f"{i}. ISBN-13: {prestamo['isbn-13']}")
    
    # Seleccionar libro para devolver
    try:
        num_libro = int(input("\nIngrese el numero del libro que desea devolver: "))
        if not (1 <= num_libro <= len(prestamos_usuario)):
            raise ValueError
    except ValueError:
        print("Error. Numero de libro no valido.")
        return
    
    # Devolver el libro
    libro_devuelto = prestamos_usuario[num_libro - 1]
    prestamos = [p for p in prestamos if not (p['dni'] == dni and p['isbn-13'] == libro_devuelto['isbn-13'])]
    auxiliar.guardar_json('Biblioteca/JSON/prestamos.json', prestamos)  # Usar la funcion auxiliar para guardar
    print(f"El libro con ISBN-13 '{libro_devuelto['isbn-13']}' ha sido devuelto exitosamente.")
    
    # Gestionar la review
    gestionar_review(libro_devuelto)

def gestionar_review(libro_devuelto: Dict) -> None:
    """
    Gestiona el ingreso de una review para el libro devuelto.
    - Argumentos:
        - libro_devuelto (Dict): Diccionario con la informacion del libro devuelto.
    - Retorna:
        - None
    """
    op = input("¿Desea dejar una review del libro? (s/n): ").lower()
    if op == 's':
        review = input("Escriba su review: ")
        if review:
            # Usar la funcion auxiliar para leer y guardar reviews
            reviews = auxiliar.leer_json('Biblioteca/JSON/reviews.json')
            
            isbn_13 = libro_devuelto['isbn-13']
            if isbn_13 in reviews:
                reviews[isbn_13].append(review)
            else:
                reviews[isbn_13] = [review]

            # Guardar las reviews actualizadas
            auxiliar.guardar_json('Biblioteca/JSON/reviews.json', reviews)
            
            print("¡Gracias por dejar su review!")
        else:
            print("Error. La review no puede estar vacia.")


