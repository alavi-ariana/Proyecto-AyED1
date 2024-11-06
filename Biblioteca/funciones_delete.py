def libro_titulo(title: str) -> List:
    """Busca libros que coinciden con un título dado.
        Args:
        - title(str): el título a buscar en los libros.
        Returns:
        - List: si se encuentran libros retorna una lista con los libros que coinciden con el 
        título dado.
    """
    coincidencias = auxi.search_(title, 'title')
    if len(coincidencias) > 1:
        for i, libro in enumerate(coincidencias, 1):
            print(f"{i}. {libro['title']} - {libro['author']} - {coincidencias[0]['isbn-13']}")
    elif len(coincidencias) == 1:
        print(f"{coincidencias[0]['title']} - {coincidencias[0]['author']}")
    else:
        print("El libro no fue encontrado.")
        time.sleep(0.75)

def libro_autor(author: str) -> List:
    """Busca libros que coinciden con un autor dado.
        Args:
        - author(str): el autor a buscar en los libros.
        Returns:
        - List: si se encuentran libros retorna una lista con los libros que coinciden con el 
        autor dado."""
    coincidencias = auxi.search_(author, 'author')
    if len(coincidencias) > 0:
        print(f"{coincidencias[0]['author'].upper()}")
        for libro in coincidencias:
            print(f"- {libro['title']}")
    else:
        print("No hubo coincidencias.")
        time.sleep(0.75)

def libro_genero() -> List:
    """Busca libros que coinciden con un género dado.
        Returns:
        - List: si se encuentran libros retorna una lista con los libros que coinciden con el 
        género dado."""
    libros = auxi.leer_libros()
    generos = set(dato['genre'] for dato in libros)
    for genero in generos:
        print(genero)

    genero_op = input("Elija un género: ")

    patron = re.compile(genero_op, re.IGNORECASE)

    genero_coincidencia = [genero for genero in generos if patron.search(genero)]

    if genero_coincidencia:
        genero_op = genero_coincidencia[0]
        libros_filtrados = [libro for libro in libros if libro['genre'] == genero_op]
        clear_screen()
        print(f"LIBROS EN EL GENERO{genero_op.upper()}")
        for libro in libros_filtrados:
            print(f"{libro['title']} - {libro['author']}")
    else:
        print("GÉNERO NO ENCONTRADO")
        time.sleep(0.75)

def prestamo(dni, isbn):
    pass


def buscar_prestar(dni) -> None:
    """Opción que ejecuta las demás opciones de busqueda.
        Returns:
        - None
    """
    usuarios = auxi.leer_usuarios()

    if dni not in usuarios['dni']:
        nombre = input("Ingrese su nombre: ")
        usuario = {
            'nombre': nombre,
            'dni': dni
        }
        usuarios.dump(usuario)

    while True:
        #clear_screen()
        mostrar_submenu_buscar_libro()
        busqueda = input("\nSeleccione una opción: ")
        #clear_screen()
        match busqueda:
            case "1":  # Busqueda de libros por titulo
                title_op = input("Ingrese el título del libro a buscar: ")
                libro_titulo(title_op)
                opcion = "title"
            case "2":  # Busqueda de libros por autor
                author_op = input("Ingrese el autor a buscar: ")
                libro_autor(author_op)
                opcion = "author"
            case "3":  # Busqueda de libros por genero
                libro_genero()
                opcion = "genre"
            case "4":  # Volver al menu principal
                break
            case _:
                clear_screen()
                print(
                    "Opción no válida, intente de nuevo."
                )
                #time.sleep(0.75)
                continue

        seleccion_op = input("Libro seleccionado: ")
        resultado = auxi.search(seleccion_op, opcion)
        if resultado:
            print(f"{resultado[0]['title']} - {resultado[0]['author']} - {resultado[0]['isbn-13']}")
            prestar = input("¿Desea pedir prestado este libro? Y / N : ").upper()
            if prestar == "Y":
                isbn = resultado[0]['isbn-13']
                prestamo(dni, isbn)
                print(f"{isbn} - hello, world")
        else:
            print("No se encontró el libro.")
    
