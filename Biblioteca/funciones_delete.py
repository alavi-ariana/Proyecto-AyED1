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
    
