class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_libros_por_autor(self, autor):
        for libro in self._libros:
            if libro.autor == autor:
                self.mostrar_libro(libro)

    def mostrar_libro(self, libro):
        print(f'Libro -> Titulo: {libro.titulo}, Autor: {libro.autor}, '
              f'Género: {libro.genero} ')
