### Descripcion de Codigo

## Flujo del Programa

- Inicio: El programa comienza ejecutando la funcion main_menu().
- Menu Principal: Se muestra el menu principal con opciones para buscar libros, devolver libros o salir del programa.
- Buscar Libros: Si el usuario selecciona la opcion de buscar libros, se muestra un submenu con opciones para buscar por titulo, autor, genero o volver al menu principal (a implementar).
- Devolver Libros: Si el usuario selecciona la opcion de devolver libros, se ejecuta el codigo correspondiente (a implementar).
- Salir del Programa: Si el usuario selecciona la opcion de salir, el programa termina con un mensaje de despedida.
- Validacion de Opciones: Si el usuario ingresa una opcion no valida, se muestra un mensaje de error y se solicita una nueva entrada.

## Funciones

- clear_screen():
    
    Descripcion: Esta funcion limpia la pantalla de la consola del usuario mientras navega entre las opciones del menu.
    
    Implementacion: Utiliza el comando cls para Windows y clear para otros sistemas operativos.

- mostrar_menu_principal():

    Descripcion: Muestra el menu principal con las opciones disponibles.

    Implementacion: Utiliza la biblioteca tabulate para formatear el menu.

- mostrar_submenu_buscar_libro():

    Descripcion: Muestra el submenu para buscar libros con opciones para buscar por titulo, autor, genero o volver al menu principal.

    Implementacion: Utiliza la biblioteca tabulate para formatear el submenu.

- main_menu():

    Descripcion: Controla el flujo del programa, mostrando el menu principal y los submenus segun la opcion seleccionada por el usuario.

    Implementacion: Utiliza un bucle while para mantener el programa en ejecucion hasta que el usuario decida salir. Utiliza la estructura match para manejar las opciones seleccionadas.
