"""Este progama realiza la gestión de una biblioteca, donde deja visualizar los libros y la información de ellos, 
pedir prestado y devolver libros, y dejar una reseña a un libro."""
import csv
import json
import os

def opciones() -> None:
    for indice, item in enumerate(opt):
        print(f"{indice + 1}: {item}")

def validar(item, lista):
    return item in lista

def show_biblioteca():
    for indice, item in enumerate(biblioteca):
        print(f"{indice + 1}: {item}")




def main() -> None:
    while True:
        opciones()
        op = input("Ingrese su opción: ")
        match op:
            case "1":
                show_biblioteca()
                library_op = int(input("Ingrese su opción: "))
                match library_op:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case _:
                        print("Opción inválida.")
            case "2":
                pass
            case "3":
                pass
            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida.")


opt = [
    "Biblioteca",
    "Prestamo de libros",
    "Dejar reseña de libros",
    "Salir",
]

biblioteca = [
            "Ver libros por género",
            "Ver libros por autor",
            "Buscar libro por título",]
main()
#End-of-file (EOF)