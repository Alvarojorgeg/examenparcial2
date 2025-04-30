class Employee:
    def __init__(self, nombre):
        self.nombre = nombre

    def registrar_usuario(self, nombre_usuario, lista_usuarios):
        nuevo = User(nombre_usuario)
        lista_usuarios.append(nuevo)
        return nuevo

    def agregar_libro(self, titulo, autor, genero, lista_libros):
        from clases.book import Book
        libro = Book(titulo, autor, genero)
        lista_libros.append(libro)
        return libro
