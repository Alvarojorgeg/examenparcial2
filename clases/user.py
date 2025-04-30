class User:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def tomar_prestado(self, libro):
        if libro.is_available():
            libro.prestar()
            self.historial.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self.historial:
            libro.devolver()
            return True
        return False
