from clases.book_genre import BookGenre

class Book:
    def __init__(self, titulo, autor, genero: BookGenre):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._disponible = True

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_genero(self):
        return self._genero

    def is_available(self):
        return self._disponible

    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True
        return False

    def devolver(self):
        self._disponible = True
