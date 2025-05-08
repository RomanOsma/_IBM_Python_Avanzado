class Libro:
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero


if __name__ == '__main__':
    libro = Libro('titulo','autor','genero')
    # libro.titulo = 'titulo2'  # esto marca error
    print(f'Accedemos a la propiedad de titulo: {libro.titulo}')