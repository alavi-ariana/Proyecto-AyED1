## Descripcion de Codigo

### Flujo del Programa

- Inicio: El programa comienza ejecutando la funcion main_menu().
- Menu Principal: Se muestra el menu principal con opciones para buscar libros, devolver libros o salir del programa.
- Buscar Libros: Si el usuario selecciona la opcion de buscar libros, se muestra un submenu con opciones para buscar por titulo, autor, genero o volver al menu principal.
- Prestamo de libros: Si el usuario encuentra el libro que buscaba, lo puede pedir prestado (a implementar).
- Registro de usuario: Registra documento del usuario y libro prestado. (a implementar)
- Devolver Libros: Si el usuario selecciona la opcion de devolver libros, se ejecuta el codigo correspondiente (a implementar).
- Salir del Programa: Si el usuario selecciona la opcion de salir, el programa termina con un mensaje de despedida.
- Validacion de Opciones: Si el usuario ingresa una opcion no valida, se muestra un mensaje de error y se solicita una nueva entrada.


## Programa Principal

- main_menu():
    Descripcion: Controla el flujo del programa, mostrando el menu principal y los submenus segun la opcion seleccionada por el usuario.

    Implementacion: Utiliza un bucle while para mantener el programa en ejecucion hasta que el usuario decida salir.
                    Utiliza la estructura match para manejar las opciones seleccionadas.
                    Buscar Libros: Permite buscar libros por titulo, autor o genero utilizando la funcion search del modulo auxiliar.
                    Devolver Libros: (Aun no implementado en el codigo compartido).
                    Salir del Programa: Finaliza la ejecucion del programa.


- clear_screen():
    
    Descripcion: Esta funcion limpia la pantalla de la consola del usuario mientras navega entre las opciones del menu.
    
    Implementacion: Utiliza el comando cls para Windows y clear para otros sistemas operativos.


- mostrar_menu_principal():

    Descripcion: Muestra el menu principal con las opciones disponibles.

    Implementacion: Utiliza la biblioteca tabulate para formatear el menu.


- mostrar_submenu_buscar_libro():

    Descripcion: Muestra el submenu para buscar libros con opciones para buscar por titulo, autor, genero o volver al menu principal.

    Implementacion: Utiliza la biblioteca tabulate para formatear el submenu.


## Funciones Auxiliares

- leer_prestamos():
            
    Descripcion: Lee un archivo JSON que contiene informacion sobre prestamos de libros y devuelve el contenido como una lista de diccionarios.
    
    Implementacion: Obtiene el directorio actual.
                    Construye la ruta del archivo prestamos.json.
                    Intenta abrir y leer el archivo JSON.
                    Si el archivo no se encuentra o hay un error de decodificacion, imprime un mensaje de error.
                    Devuelve una lista de diccionarios con los datos leidos.


- leer_libros():

    Descripcion: Lee un archivo CSV que contiene informacion sobre libros y devuelve el contenido como una lista de diccionarios.

    Implementacion: Obtiene el directorio actual.
                    Construye la ruta del archivo books.csv.
                    Intenta abrir y leer el archivo CSV.
                    Si el archivo no se encuentra o hay un error al leer el CSV, imprime un mensaje de error.
                    Devuelve una lista de diccionarios con los datos leidos.


- search(buscar: str, opcion: str):

    Descripcion: Busca libros basados en un termino de busqueda y una opcion especifica (como titulo o autor).
    
    Implementacion: Llama a la funcion leer_libros para obtener la lista de libros.
                    Crea un patron de busqueda usando expresiones regulares.
                    Busca coincidencias en el campo especificado (opcion) de cada libro.
                    Devuelve una lista de libros que coinciden con el término de busqueda.