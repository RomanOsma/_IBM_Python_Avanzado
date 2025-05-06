from pelicula import Pelicula
from servicio_peliculas import ServicioPeliculas


class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def mostrar_menu(self):
        print('*** App Catálogo Películas ***')
        while True:
            try:
                print(f'''Opciones:
                1. Agregar Película
                2. Listar Películas
                3. Eliminar catálogo de películas
                4. Salir''')
                opcion = int(input('Escribe tu opción (1-4): '))
                if opcion == 1:
                    nombre_pelicula = input('Dame el nombre de la película: ')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print('Salimos del programa...')
                    break
                else:
                    print('Opción inválida, Introduce un valor entre 1 y 4.')
            except ValueError:
                print('Error: Introduce un número válido.')
            except Exception as e:
                print(f'Ocurrió un error: {e}')


if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.mostrar_menu()