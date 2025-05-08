# Creamos un objeto de tipo biblioteca
from biblioteca import Biblioteca
from libro import Libro

bibliotecaMexico = Biblioteca('Biblioteca España')

# Agregar algunos libros
libro1 = Libro('El Alquimista', 'Paulo Cohelo', 'Ficción')
libro2 = Libro('1984', 'George Orwell', 'Ficción')
libro3 = Libro('El código Da Vinci', 'Dan Brown', 'Misterio')
libro4 = Libro('Rayuela', 'Julio Cortázar', 'Novela')
libro5 = Libro('Verónica decide morir', 'Paulo Cohelo', 'Ficción')

# Agregar los libros a la biblioteca
bibliotecaMexico.agregar_libro(libro1)
bibliotecaMexico.agregar_libro(libro2)
bibliotecaMexico.agregar_libro(libro3)
bibliotecaMexico.agregar_libro(libro4)
bibliotecaMexico.agregar_libro(libro5)

# Nombre de la biblioteca
print(f'*** Bienvenidos a la {bibliotecaMexico.nombre} ***')

# Buscar libros por autor
print(f'\nLibros de Paulo Cohelo: ')
bibliotecaMexico.buscar_libros_por_autor('Paulo Cohelo')

# Buscar libros por género
print(f'\nLibros de Ficción: ')
bibliotecaMexico.buscar_libros_por_genero('Ficción')

# Buscar libros por género
print(f'\nLibros de Misterio: ')
bibliotecaMexico.buscar_libros_por_genero('Misterio')

# Buscar libros por género
print(f'\nLibros de Novela: ')
bibliotecaMexico.buscar_libros_por_genero('Novela')

# Mostrar todos los libros de la biblioteca
bibliotecaMexico.mostrar_todos_los_libros()

# Obtener el numero total de empleados de la empresa creada
print(f'\nTotal de Libros en la Biblioteca: {Libro.obtener_total_libros()}')


