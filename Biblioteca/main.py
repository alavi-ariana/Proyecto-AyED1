"""Ejecución del programa."""
import modulos.menues as menues
from funciones import funciones

if __name__ == "__main__":
    try:
        menues.menu_principal()
    except KeyboardInterrupt:
        funciones.clear_screen()
        print("BYE!")

# End-of-file (EOF)
