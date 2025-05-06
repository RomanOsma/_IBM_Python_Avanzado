"""
Este módulo proporciona un tutorial completo sobre Programación Orientada a Objetos
en Python, abarcando conceptos fundamentales con ejemplos claros y explicaciones.

Temas cubiertos:
- Clases y Objetos
- Constructores y Métodos de Instancia
- Encapsulamiento y Modificadores de Acceso
- Atributos y Métodos de Clase
- Herencia y Polimorfismo
- Clase Object y Representación de Objetos
"""


# =============================================================================
# SECCIÓN 1: INTRODUCCIÓN A CLASES Y OBJETOS
# =============================================================================

def seccion_1_intro_clases_y_objetos():
    """
    Introducción al concepto de clases y objetos en Python.

    Una clase es un plano para crear objetos, definiendo atributos y métodos.
    Un objeto es una instancia de una clase.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 1: INTRODUCCIÓN A CLASES Y OBJETOS")
    print("=" * 80)

    # Definición básica de clase
    print("\n1.1: Definición Básica de Clase")
    print("-" * 40)

    class Persona:
        """
        Una clase simple que representa a una persona con información básica.
        Esta es la forma más básica de definir una clase en Python.
        """

        # Método para inicializar los atributos del objeto
        def __init__(self):
            self.apellido = None
            self.nombre = None

        def inicializar_persona(self, nombre, apellido):
            """Inicializa los atributos de la persona."""
            # Creamos los atributos de la clase
            self.nombre = nombre
            self.apellido = apellido

        # Método para mostrar información de la persona
        def mostrar_contacto(self):
            """Muestra la información de la persona."""
            print(f'''Persona: 
Nombre: {self.nombre} 
Apellido: {self.apellido}''')

    # Crear y usar objetos
    print("\nEjemplo - Creando objetos de la clase Persona:")

    # Primer objeto
    persona1 = Persona()  # Crea un objeto vacío en memoria
    persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_contacto()

    # Segundo objeto
    persona2 = Persona()
    persona2.inicializar_persona('Ian', 'Sanchez')
    persona2.mostrar_contacto()

    print("\nConceptos clave:")
    print("- Una clase se define usando la palabra clave 'class' seguida del nombre de la clase")
    print("- Los métodos son funciones definidas dentro de una clase")
    print("- 'self' se refiere a la instancia actual de la clase")
    print("- Los objetos se crean (instancian) llamando al nombre de la clase como una función")
    print("- Cada objeto tiene su propio conjunto de atributos")

    print("\nAlternativa - Enfoque tradicional vs. Orientado a Objetos:")
    print("En lugar de usar POO, podríamos usar diccionarios para almacenar datos:")

    # Enfoque alternativo usando diccionarios
    contacto1 = {'nombre': 'Layla', 'apellido': 'Acosta'}
    contacto2 = {'nombre': 'Ian', 'apellido': 'Sanchez'}

    def mostrar_contacto_dict(contacto):
        print(f"Persona: \nNombre: {contacto['nombre']} \nApellido: {contacto['apellido']}")

    print("\nUsando diccionarios:")
    mostrar_contacto_dict(contacto1)
    mostrar_contacto_dict(contacto2)

    print("\nVentajas de POO sobre diccionarios:")
    print("- Los métodos están asociados directamente con los datos")
    print("- Mayor encapsulamiento y organización del código")
    print("- Facilita la reutilización y extensión del código")


# =============================================================================
# SECCIÓN 2: CONSTRUCTORES EN PYTHON
# =============================================================================

def seccion_2_constructores():
    """
    Demuestra el uso de constructores en clases de Python.

    El método __init__ es un método especial que se llama automáticamente
    cuando se crea un objeto. Se utiliza para inicializar los atributos del objeto.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 2: CONSTRUCTORES EN PYTHON")
    print("=" * 80)

    print("\n2.1: Usando el Constructor __init__")
    print("-" * 40)

    class Persona:
        """
        Una clase que representa a una persona con un constructor adecuado.
        """

        # Constructor (método __init__)
        def __init__(self, nombre, apellido):
            """
            Inicializa un nuevo objeto Persona.

            Args:
                nombre (str): Nombre de la persona
                apellido (str): Apellido de la persona
            """
            # Creamos los atributos de la clase
            self.nombre = nombre
            self.apellido = apellido

        def mostrar_contacto(self):
            """Muestra la información de la persona."""
            print(f'''Persona: 
Nombre: {self.nombre} 
Apellido: {self.apellido}''')

    # Crear objetos usando el constructor
    print("\nEjemplo - Creando objetos usando el constructor:")

    # El constructor (__init__) se llama automáticamente
    persona1 = Persona('Layla', 'Acosta')
    persona1.mostrar_contacto()

    # Segundo objeto
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar_contacto()

    print("\n2.2: Gestión de Memoria en Objetos de Python")
    print("-" * 40)

    # Mostrando direcciones de memoria
    class PersonaMemoria:
        """Demuestra gestión de memoria con objetos Python."""

        def __init__(self, nombre, apellido):
            """Inicializa objeto con nombre y apellido."""
            self.nombre = nombre
            self.apellido = apellido

        def mostrar_contacto(self):
            """Muestra información y direcciones de memoria."""
            print(f'''Persona: 
Nombre: {self.nombre} 
Apellido: {self.apellido}''')
            print(f'Dir. mem self: {id(self)}')
            print(f'Dir. mem hex self: {hex(id(self))}')

    # Crear objetos y mostrar direcciones de memoria
    print("\nEjemplo - Direcciones de memoria de objetos:")

    persona1 = PersonaMemoria('Layla', 'Acosta')
    persona1.mostrar_contacto()
    print(f'Dir. mem persona1: {id(persona1)}')
    print(f'Dir. mem hex persona1: {hex(id(persona1))}')

    print()
    persona2 = PersonaMemoria('Ian', 'Sanchez')
    persona2.mostrar_contacto()
    print(f'Dir. mem persona2: {id(persona2)}')
    print(f'Dir. mem hex persona2: {hex(id(persona2))}')

    print("\nConceptos clave:")
    print("- __init__ es un método especial que se llama cuando se crea un objeto")
    print("- 'self' representa la instancia de la clase y debe ser el primer parámetro")
    print("- Cada objeto tiene una dirección de memoria única")
    print("- id() devuelve la dirección de memoria como un entero")
    print("- hex() convierte el entero a hexadecimal")


# =============================================================================
# SECCIÓN 3: EJEMPLO PRÁCTICO - CLASE ARITMÉTICA
# =============================================================================

def seccion_3_clase_aritmetica():
    """
    Demuestra un ejemplo práctico del uso de clases con una clase Aritmética.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 3: EJEMPLO PRÁCTICO - CLASE ARITMÉTICA")
    print("=" * 80)

    print("\n3.1: Clase Aritmética Básica")
    print("-" * 40)

    class Aritmetica:
        """
        Una clase que realiza operaciones aritméticas básicas.
        """

        def __init__(self, operando1, operando2):
            """Inicializa con dos operandos."""
            self.operando1 = operando1
            self.operando2 = operando2

        def sumar(self):
            """Suma los dos operandos e imprime el resultado."""
            resultado = self.operando1 + self.operando2
            print(f'Resultado suma: {resultado}')

        def restar(self):
            """Resta el segundo operando del primero e imprime el resultado."""
            resultado = self.operando1 - self.operando2
            print(f'Resultado resta: {resultado}')

        def multiplicar(self):
            """Multiplica los dos operandos e imprime el resultado."""
            resultado = self.operando1 * self.operando2
            print(f'Resultado multiplicación: {resultado}')

        def dividir(self):
            """Divide el primer operando por el segundo e imprime el resultado."""
            if self.operando2 == 0:
                print('Error: División por cero')
                return
            resultado = self.operando1 / self.operando2
            print(f'Resultado división: {resultado}')

    # Ejemplo de uso
    print("\nEjemplo - Usando la clase Aritmética:")
    print("Creando aritmetica1 = Aritmetica(5, 7)")
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()

    # Segundo objeto
    print("\nCreando aritmetica2 = Aritmetica(12, 16)")
    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.multiplicar()
    aritmetica2.dividir()

    print("\n3.2: Parámetros Flexibles del Constructor")
    print("-" * 40)

    class AritmeticaFlexible:
        """
        Una clase aritmética con parámetros de constructor flexibles.
        """

        def __init__(self, operando1=None, operando2=None):
            """
            Inicializa con operandos opcionales.

            Args:
                operando1: Primer operando (por defecto: None)
                operando2: Segundo operando (por defecto: None)
            """
            self.operando1 = operando1
            self.operando2 = operando2

        def sumar(self):
            """Suma los dos operandos e imprime el resultado."""
            if self.operando1 is None or self.operando2 is None:
                print("Error: Se requieren dos operandos para sumar")
                return
            resultado = self.operando1 + self.operando2
            print(f'Resultado suma: {resultado}')

        def restar(self):
            """Resta el segundo operando del primero e imprime el resultado."""
            if self.operando1 is None or self.operando2 is None:
                print("Error: Se requieren dos operandos para restar")
                return
            resultado = self.operando1 - self.operando2
            print(f'Resultado resta: {resultado}')

        def multiplicar(self):
            """Multiplica los dos operandos e imprime el resultado."""
            if self.operando1 is None or self.operando2 is None:
                print("Error: Se requieren dos operandos para multiplicar")
                return
            resultado = self.operando1 * self.operando2
            print(f'Resultado multiplicación: {resultado}')

        def dividir(self):
            """Divide el primer operando por el segundo e imprime el resultado."""
            if self.operando1 is None or self.operando2 is None:
                print("Error: Se requieren dos operandos para dividir")
                return
            if self.operando2 == 0:
                print('Error: División por cero')
                return
            resultado = self.operando1 / self.operando2
            print(f'Resultado división: {resultado}')

    # Ejemplos de uso de constructor flexible
    print("\nEjemplo - Uso de constructor flexible:")

    print("\nPrimer objeto (con dos operandos):")
    aritmetica1 = AritmeticaFlexible(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()

    print("\nSegundo objeto (con dos operandos):")
    aritmetica2 = AritmeticaFlexible(12, 16)
    aritmetica2.sumar()
    aritmetica2.restar()

    print("\nTercer objeto (con un operando):")
    aritmetica3 = AritmeticaFlexible(4)
    aritmetica3.sumar()  # Esto mostrará un error
    aritmetica3.operando2 = 7  # Asignar segundo operando después de la creación
    aritmetica3.sumar()  # Ahora funciona

    print("\nCuarto objeto (sin operandos):")
    aritmetica4 = AritmeticaFlexible()
    aritmetica4.operando1 = 2  # Asignar primer operando
    aritmetica4.operando2 = 3  # Asignar segundo operando
    aritmetica4.sumar()  # Ahora funciona

    print("\nConceptos clave:")
    print("- Las clases pueden implementar métodos para operaciones específicas")
    print("- Los parámetros del constructor pueden tener valores predeterminados")
    print("- Los atributos pueden establecerse o modificarse después de la creación del objeto")
    print("- Agregar validación ayuda a prevenir errores")

    print("\nComparación con funciones regulares:")
    print("La misma tarea usando funciones regulares:")

    def sumar_funcion(a, b):
        return a + b

    def restar_funcion(a, b):
        return a - b

    print(f"sumar_funcion(5, 7) = {sumar_funcion(5, 7)}")
    print(f"restar_funcion(5, 7) = {restar_funcion(5, 7)}")

    print("\nVentajas de usar una clase:")
    print("- Mantiene los operandos y las operaciones juntos")
    print("- Permite reutilizar los mismos operandos para múltiples operaciones")
    print("- Es más fácil extender con nuevas operaciones")


# =============================================================================
# SECCIÓN 4: ENCAPSULAMIENTO EN PYTHON
# =============================================================================

def seccion_4_encapsulamiento():
    """
    Demuestra conceptos de encapsulamiento en Python.

    El encapsulamiento es el principio de agrupar datos y métodos que trabajan en esos
    datos dentro de una unidad (clase) y restringir el acceso a algunos de los componentes
    del objeto.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 4: ENCAPSULAMIENTO EN PYTHON")
    print("=" * 80)

    print("\n4.1: Modificadores de Acceso en Python")
    print("-" * 40)

    class Coche:
        """
        Una clase que representa un coche, demostrando modificadores de acceso.

        En Python, tenemos convenciones para modificadores de acceso:
        - Público: nombres normales de atributos ( self.nombre)
        - Protegido: prefijo de un guion bajo (self._nombre)
        - Privado: prefijo de dos guiones bajos (self.__nombre)
        """

        def __init__(self, marca, modelo, color):
            self.marca = marca  # Atributo público
            self._modelo = modelo  # Atributo protegido (convención)
            self.__color = color  # Atributo privado

        def conducir(self):
            """Muestra información sobre el coche que se está conduciendo."""
            print(f'''Conduciendo el coche: 
            Marca: {self.marca} 
            Modelo: {self._modelo} 
            Color: {self.__color}'''
                )

    # Ejemplo de modificadores de acceso
    print("\nEjemplo - Modificadores de acceso:")

    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()

    # Modificando atributos con diferentes niveles de acceso
    print("\nModificando atributos:")
    coche1.marca = 'Toyota 2'  # Público - acceso directo
    print(f"Cambió atributo público: coche1.marca = 'Toyota 2'")

    coche1._modelo = 'Yaris 2'  # Protegido - desaconsejado pero posible
    print(f"Cambió atributo protegido: coche1._modelo = 'Yaris 2' (no recomendado)")

    # Atributo privado - no se puede acceder directamente
    print("Intentando modificar atributo privado: coche1.__color = 'Azul 2'")
    try:
        print(f"Nota: {coche1.__dict__}")
        coche1.__color = 'Azul 2'  # Esto no modifica el atributo original
        print("Nota: Esto crea un nuevo atributo pero no cambia el privado")
        print(f"Nota: {coche1.__dict__}")
    except Exception as e:
        print(f"Error: {e}")

    # Name mangling - accediendo al atributo privado (no recomendado)
    print("\nAccediendo al atributo privado mediante name mangling (no recomendado):")
    coche1._Coche__color = 'Azul 3'
    print(f"coche1._Coche__color = 'Azul 3'")

    coche1.conducir()

    print("\n4.2: Métodos Getter y Setter (Encapsulamiento)")
    print("-" * 40)

    class CocheEncapsulado:
        """
        Una clase coche con encapsulamiento apropiado usando métodos getter y setter.
        """

        def __init__(self, marca, modelo, color):
            self._marca = marca
            self._modelo = modelo
            self._color = color

        def conducir(self):
            """Muestra información sobre el coche que se está conduciendo."""
            print(f'''Conduciendo el coche: 
            Marca: {self._marca} 
            Modelo: {self._modelo} 
            Color: {self._color}''')

        # Métodos getter y setter para marca
        def get_marca(self):
            """Obtiene la marca del coche."""
            return self._marca

        def set_marca(self, marca):
            """Establece la marca del coche."""
            self._marca = marca

        # Métodos getter y setter para modelo
        def get_modelo(self):
            """Obtiene el modelo del coche."""
            return self._modelo

        def set_modelo(self, modelo):
            """Establece el modelo del coche."""
            self._modelo = modelo

        # Métodos getter y setter para color
        def get_color(self):
            """Obtiene el color del coche."""
            return self._color

        def set_color(self, color):
            """Establece el color del coche."""
            self._color = color

    # Ejemplo de uso de métodos getter y setter
    print("\nEjemplo - Usando métodos getter y setter:")

    coche1 = CocheEncapsulado('Toyota', 'Yaris', 'Azul')
    coche1.conducir()

    print("\nUsando métodos getter:")
    print(f"Marca: {coche1.get_marca()}")
    print(f"Modelo: {coche1.get_modelo()}")
    print(f"Color: {coche1.get_color()}")

    print("\nUsando métodos setter:")
    coche1.set_marca("Toyota 2")
    coche1.set_modelo("Yaris 2")
    coche1.set_color("Azul 2")
    print("\nDespués de cambios:")
    coche1.conducir()

    # Otro ejemplo de encapsulamiento
    print("\n4.3: Clase Aritmética Encapsulada")
    print("-" * 40)

    class AritmeticaEncapsulada:
        """
        Una clase aritmética con encapsulamiento apropiado.
        """

        def __init__(self, operando1=None, operando2=None):
            self._operando1 = operando1
            self._operando2 = operando2

        def sumar(self):
            """Suma los dos operandos e imprime el resultado."""
            if self._operando1 is None or self._operando2 is None:
                print("Error: Se requieren dos operandos para sumar")
                return
            resultado = self._operando1 + self._operando2
            print(f'Resultado suma: {resultado}')
            return resultado

        def restar(self):
            """Resta el segundo operando del primero e imprime el resultado."""
            if self._operando1 is None or self._operando2 is None:
                print("Error: Se requieren dos operandos para restar")
                return
            resultado = self._operando1 - self._operando2
            print(f'Resultado resta: {resultado}')
            return resultado

        # Métodos getter y setter para cada atributo
        def get_operando1(self):
            """Obtiene el primer operando."""
            return self._operando1

        def set_operando1(self, operando1):
            """Establece el primer operando."""
            self._operando1 = operando1

        def get_operando2(self):
            """Obtiene el segundo operando."""
            return self._operando2

        def set_operando2(self, operando2):
            """Establece el segundo operando."""
            self._operando2 = operando2

    # Ejemplo de uso de la clase encapsulada
    print("\nEjemplo - Usando la clase Aritmética encapsulada:")

    aritmetica1 = AritmeticaEncapsulada(5, 7)
    print(f"Valor operando1: {aritmetica1.get_operando1()}")
    print(f"Valor operando2: {aritmetica1.get_operando2()}")
    aritmetica1.sumar()
    aritmetica1.restar()

    # Modificando operandos
    print("\nModificando operandos:")
    aritmetica1.set_operando1(10)
    aritmetica1.set_operando2(3)
    print(f"Nuevos valores - operando1: {aritmetica1.get_operando1()}, operando2: {aritmetica1.get_operando2()}")
    aritmetica1.sumar()
    aritmetica1.restar()

    print("\nVentajas del encapsulamiento:")
    print("- Protección de datos - previene modificaciones indeseadas")
    print("- Control sobre cómo se accede y modifica cada atributo")
    print("- Posibilidad de agregar validación en los setters")
    print("- Posibilidad de cambiar la implementación interna sin afectar al código cliente")


# =============================================================================
# SECCIÓN 5: PROPIEDADES EN PYTHON
# =============================================================================

def seccion_5_propiedades():
    """
    Demuestra el uso de propiedades en Python.

    Las propiedades proporcionan una forma de usar métodos getter y setter con una
    sintaxis más natural, utilizando el decorador @property.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 5: PROPIEDADES EN PYTHON")
    print("=" * 80)

    print("\n5.1: Propiedades de Solo Lectura")
    print("-" * 40)

    class Libro:
        """
        Una clase que representa un libro con propiedades.
        """

        def __init__(self, titulo, autor, genero):
            self._titulo = titulo
            self._autor = autor
            self._genero = genero

        @property
        def titulo(self):
            """Obtiene el título del libro."""
            return self._titulo

        @property
        def autor(self):
            """Obtiene el autor del libro."""
            return self._autor

        @property
        def genero(self):
            """Obtiene el género del libro."""
            return self._genero

    # Ejemplo de uso de propiedades
    print("\nEjemplo - Usando propiedades:")

    libro = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
    print(f"Título: {libro.titulo}")
    print(f"Autor: {libro.autor}")
    print(f"Género: {libro.genero}")

    print("\nIntentando modificar una propiedad de solo lectura:")
    try:
        libro.titulo = "Otro título"  # Esto provocará un error
    except AttributeError as e:
        print(f"Error: {e}")

    print("\n5.2: Propiedades Modificables")
    print("-" * 40)

    class LibroMutable:
        """
        Una clase que representa un libro con propiedades que pueden ser modificadas.
        """

        def __init__(self, titulo, autor, genero):
            self._titulo = titulo
            self._autor = autor
            self._genero = genero

        @property
        def titulo(self):
            """Obtiene el título del libro."""
            return self._titulo

        @titulo.setter
        def titulo(self, titulo):
            """Establece el título del libro."""
            if not titulo:
                raise ValueError("El título no puede estar vacío")
            self._titulo = titulo

        @property
        def autor(self):
            """Obtiene el autor del libro."""
            return self._autor

        @autor.setter
        def autor(self, autor):
            """Establece el autor del libro."""
            if not autor:
                raise ValueError("El autor no puede estar vacío")
            self._autor = autor

        @property
        def genero(self):
            """Obtiene el género del libro."""
            return self._genero

        @genero.setter
        def genero(self, genero):
            """Establece el género del libro."""
            if not genero:
                raise ValueError("El género no puede estar vacío")
            self._genero = genero

    # Ejemplo de uso de propiedades modificables
    print("\nEjemplo - Usando propiedades modificables:")

    libro_mutable = LibroMutable("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
    print(f"Título original: {libro_mutable.titulo}")

    libro_mutable.titulo = "El amor en los tiempos del cólera"
    libro_mutable.autor = "Gabriel García Márquez"
    libro_mutable.genero = "Novela romántica"

    print(f"Nuevo título: {libro_mutable.titulo}")
    print(f"Autor: {libro_mutable.autor}")
    print(f"Género: {libro_mutable.genero}")

    print("\nIntentando establecer un valor inválido:")
    try:
        libro_mutable.titulo = ""  # Esto provocará un error
    except ValueError as e:
        print(f"Error: {e}")

    print("\n5.3: Sistema de Biblioteca")
    print("-" * 40)

    class Biblioteca:
        """
        Una clase que representa una biblioteca que contiene libros.
        """

        def __init__(self, nombre):
            self._nombre = nombre
            self._libros = []

        def agregar_libro(self, libro):
            """Agrega un libro a la biblioteca."""
            self._libros.append(libro)

        def buscar_libros_por_autor(self, autor):
            """Busca libros por autor."""
            print(f"\nLibros del autor '{autor}':")
            encontrados = False
            for libro in self._libros:
                if libro.autor == autor:
                    self.mostrar_libro(libro)
                    encontrados = True
            if not encontrados:
                print(f"No se encontraron libros del autor '{autor}'")
            return encontrados

        def buscar_libros_por_genero(self, genero):
            """Busca libros por género."""
            print(f"\nLibros del género '{genero}':")
            encontrados = False
            for libro in self._libros:
                if libro.genero == genero:
                    self.mostrar_libro(libro)
                    encontrados = True
            if not encontrados:
                print(f"No se encontraron libros del género '{genero}'")
            return encontrados

        def mostrar_todos_los_libros(self):
            """Muestra todos los libros de la biblioteca."""
            print(f"\nTodos los libros de la biblioteca {self.nombre}:")
            if not self.libros:
                print("No hay libros en la biblioteca")
                return
            for libro in self.libros:
                self.mostrar_libro(libro)

        def mostrar_libro(self, libro):
            """Muestra la información de un libro."""
            print(f"Libro -> Título: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}")

        @property
        def nombre(self):
            """Obtiene el nombre de la biblioteca."""
            return self._nombre

        @property
        def libros(self):
            """Obtiene la lista de libros de la biblioteca."""
            return self._libros

    # Ejemplo de uso del sistema de biblioteca
    print("\nEjemplo - Sistema de Biblioteca:")

    biblioteca = Biblioteca("Biblioteca Municipal")

    # Agregar libros
    libro1 = LibroMutable("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
    libro2 = LibroMutable("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela romántica")
    libro3 = LibroMutable("El código Da Vinci", "Dan Brown", "Thriller")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Buscar libros
    biblioteca.mostrar_todos_los_libros()
    biblioteca.buscar_libros_por_autor("Gabriel García Márquez")
    biblioteca.buscar_libros_por_genero("Thriller")

    print("\nVentajas de usar propiedades:")
    print("- Sintaxis más natural y pythónica")
    print("- Control sobre el acceso y la modificación de atributos")
    print("- Posibilidad de agregar validación y lógica a las propiedades")
    print("- Compatibilidad con la API de atributos públicos")


# =============================================================================
# SECCIÓN 6: ATRIBUTOS Y MÉTODOS DE CLASE
# =============================================================================

def seccion_6_atributos_y_metodos_clase():
    """
    Demuestra atributos y métodos de clase en Python.

    Los atributos de clase se comparten entre todas las instancias de una clase.
    Los métodos de clase operan en la clase misma, no en las instancias.
    Los métodos estáticos no operan en la clase ni en sus instancias.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 6: ATRIBUTOS Y MÉTODOS DE CLASE")
    print("=" * 80)

    print("\n6.1: Atributos de Clase")
    print("-" * 40)

    class Persona:
        """
        Una clase que demuestra atributos de clase.
        """
        # Atributo de clase
        atributo_clase = 0

        def __init__(self, atributo_instancia):
            # Atributo de instancia
            self.atributo_instancia = atributo_instancia

    # Uso de atributos de clase
    print("\nEjemplo - Atributos de clase:")

    print(f"Atributo de Clase = {Persona.atributo_clase}")

    # Modificamos el atributo de clase
    Persona.atributo_clase = 10
    print(f"Atributo de Clase modificado = {Persona.atributo_clase}")

    # Creamos objetos
    persona1 = Persona(15)
    print(f"Atributo de Clase desde persona1: {persona1.atributo_clase}")
    print(f"Atributo de instancia desde persona1: {persona1.atributo_instancia}")

    persona2 = Persona(30)
    print(f"Atributo de Clase desde persona2: {persona2.atributo_clase}")
    print(f"Atributo de instancia desde persona2: {persona2.atributo_instancia}")

    # Modificamos el atributo de clase a través de una instancia
    persona1.atributo_clase = 20
    print(f"\nDespués de persona1.atributo_clase = 20:")
    print(f"Atributo de Clase: {Persona.atributo_clase}")  # Sigue siendo 10
    print(f"atributo_clase en persona1: {persona1.atributo_clase}")  # Es 20
    print(f"atributo_clase en persona2: {persona2.atributo_clase}")  # Sigue siendo 10

    print("\nNota: Al asignar un valor a persona1.atributo_clase, se crea un nuevo atributo de instancia")
    print("      que oculta el atributo de clase con el mismo nombre.")

    print("\n6.2: Contador de Objetos")
    print("-" * 40)

    class PersonaContador:
        """
        Una clase que cuenta el número de instancias creadas.
        """
        # Atributo de clase para contar instancias
        contador_personas = 0

        def __init__(self, nombre, apellido):
            # Incrementamos el contador cada vez que se crea una instancia
            PersonaContador.contador_personas += 1
            self.id = PersonaContador.contador_personas
            self.nombre = nombre
            self.apellido = apellido

        def mostrar_persona(self):
            """Muestra la información de la persona."""
            print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")

    # Ejemplo de contador de objetos
    print("\nEjemplo - Contador de objetos:")

    persona1 = PersonaContador('Gerardo', 'Perez')
    persona1.mostrar_persona()

    persona2 = PersonaContador('Daniel', 'Sanchez')
    persona2.mostrar_persona()

    print(f"Contador objetos Persona: {PersonaContador.contador_personas}")

    # Crear más objetos
    persona3 = PersonaContador('Ana', 'Garcia')
    persona4 = PersonaContador('Luis', 'Martinez')

    print(f"Contador después de crear más objetos: {PersonaContador.contador_personas}")

    print("\n6.3: Métodos Estáticos y de Clase")
    print("-" * 40)

    class PersonaMetodos:
        """
        Una clase que demuestra métodos estáticos y de clase.
        """
        # Atributo de clase para contar instancias
        contador_personas = 0

        def __init__(self, nombre, apellido):
            # Incrementamos el contador cada vez que se crea una instancia
            PersonaMetodos.contador_personas += 1
            self.id = PersonaMetodos.contador_personas
            self.nombre = nombre
            self.apellido = apellido

        def mostrar_persona(self):
            """Muestra la información de la persona."""
            print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")

        @staticmethod
        def get_contador_personas_estatico():
            """
            Método estático para obtener el número de personas.

            Este método no recibe 'self' o 'cls' como su primer parámetro.
            Es una función regular que pertenece al espacio de nombres de la clase.
            """
            print('Método estático')
            return PersonaMetodos.contador_personas

        @classmethod
        def get_contador_personas_clase(cls):
            """
            Método de clase para obtener el número de personas.

            Este método recibe la clase misma como su primer parámetro.
            Puede acceder a atributos de clase a través del parámetro 'cls'.
            """
            print('Método de clase')
            return cls.contador_personas

    # Ejemplo de métodos estáticos y de clase
    print("\nEjemplo - Métodos estáticos y de clase:")

    persona1 = PersonaMetodos('Gerardo', 'Perez')
    persona1.mostrar_persona()

    persona2 = PersonaMetodos('Daniel', 'Sanchez')
    persona2.mostrar_persona()

    # Formas de acceder al contador de personas
    print(f"\nContador objetos Persona (directamente): {PersonaMetodos.contador_personas}")
    print(f"Contador objetos Persona (método estático): {PersonaMetodos.get_contador_personas_estatico()}")
    print(f"Contador objetos Persona (método de clase): {PersonaMetodos.get_contador_personas_clase()}")

    # También pueden ser llamados desde instancias
    print(f"\nLlamando métodos desde una instancia:")
    print(f"Contador objetos Persona (método estático): {persona1.get_contador_personas_estatico()}")
    print(f"Contador objetos Persona (método de clase): {persona1.get_contador_personas_clase()}")

    print("\nDiferencias entre métodos estáticos y de clase:")
    print("- Métodos estáticos (@staticmethod): No reciben ni 'self' ni 'cls'")
    print("  * Útiles para funciones de utilidad relacionadas con la clase")
    print("  * No tienen acceso a la instancia ni a la clase")
    print("- Métodos de clase (@classmethod): Reciben 'cls' como primer parámetro")
    print("  * Pueden acceder a atributos de clase y modificarlos")
    print("  * Útiles para métodos de fábrica y operaciones que afectan a toda la clase")
    print("  * Pueden ser usados para crear instancias alternativas")


# =============================================================================
# SECCIÓN 7: MÓDULOS Y PAQUETES
# =============================================================================

def seccion_7_modulos_y_paquetes():
    """
    Demuestra cómo organizar clases en módulos y paquetes.

    Esta sección explica el concepto de módulos y paquetes en Python
    y cómo se utilizan para organizar clases relacionadas.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 7: MÓDULOS Y PAQUETES")
    print("=" * 80)

    print("\n7.1: Organización de Código")
    print("-" * 40)

    print("En Python, podemos organizar nuestro código en:")
    print("1. Módulos: Archivos .py individuales")
    print("2. Paquetes: Directorios que contienen módulos y un archivo __init__.py")

    print("\nEjemplo de estructura de un proyecto:")
    print("""
sistema_empleados/
    __init__.py
    empleado.py
    empresa.py
    EjemploEjemplo.py
    """)

    print("\nContenido del archivo empleado.py:")
    print("""
class Empleado:
    contador_empleados = 0

    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleados += 1

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados
    """)

    print("\nContenido del archivo empresa.py:")
    print("""
from sistema_empleados.empleado import Empleado

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_numero_empleados_departamento(self, departamento):
        contador_empleados_por_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados_por_departamento += 1
        return contador_empleados_por_departamento
    """)

    print("\nContenido del archivo Ejemplo.py:")
    print("""
from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa

# Crear una empresa
empresa = Empresa("TechCorp")

# Contratar empleados
empresa.contratar_empleado("Juan Perez", "Desarrollo")
empresa.contratar_empleado("Ana Garcia", "Desarrollo")
empresa.contratar_empleado("Luis Rodriguez", "Marketing")

# Obtener información
print(f"Total de empleados: {Empleado.obtener_total_empleados()}")
print(f"Empleados en Desarrollo: {empresa.obtener_numero_empleados_departamento('Desarrollo')}")
    """)

    print("\nVentajas de usar módulos y paquetes:")
    print("- Organización clara del código")
    print("- Reutilización de código en diferentes proyectos")
    print("- Evita conflictos de nombres (namespace)")
    print("- Mejora la mantenibilidad del código")


# =============================================================================
# SECCIÓN 8: HERENCIA Y POLIMORFISMO
# =============================================================================

def seccion_8_herencia_y_polimorfismo():
    """
    Demuestra herencia y polimorfismo en Python.

    La herencia permite que una clase herede atributos y métodos de otra clase.
    El polimorfismo permite que objetos de diferentes clases sean tratados como objetos de una superclase común.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 8: HERENCIA Y POLIMORFISMO")
    print("=" * 80)

    print("\n8.1: Herencia Básica")
    print("-" * 40)

    class Animal:
        """Clase base para todos los animales."""

        def comer(self):
            """Todos los animales comen."""
            print("Como muchas veces al día")

        def dormir(self):
            """Todos los animales duermen."""
            print("Duermo muchas horas")

    class Perro(Animal):
        """Un perro es un animal que puede ladrar."""

        def hacer_sonido(self):
            """Los perros ladran."""
            print("Puedo ladrar")

    # Ejemplo de herencia básica
    print("\nEjemplo - Herencia básica:")

    perro = Perro()
    print("Llamando a métodos heredados:")
    perro.comer()
    perro.dormir()

    print("\nLlamando a método propio:")
    perro.hacer_sonido()

    print("\n8.2: Sobreescritura de Métodos")
    print("-" * 40)

    class AnimalConSonido:
        """Clase base para animales que hacen sonidos."""

        def comer(self):
            """Todos los animales comen."""
            print("Como muchas veces al día")

        def dormir(self):
            """Todos los animales duermen."""
            print("Duermo muchas horas")

        def hacer_sonido(self):
            """Implementación base de hacer sonido."""
            print("Hago un sonido genérico")

    class PerroConSonido(AnimalConSonido):
        """Un perro que sobreescribe el método hacer_sonido."""

        def hacer_sonido(self):
            """Los perros ladran, sobreescribiendo el sonido genérico."""
            print("¡Guau guau!")

    class GatoConSonido(AnimalConSonido):
        """Un gato que sobreescribe el método hacer_sonido."""

        def hacer_sonido(self):
            """Los gatos maúllan, sobreescribiendo el sonido genérico."""
            print("¡Miau miau!")

    # Ejemplo de sobreescritura de métodos
    print("\nEjemplo - Sobreescritura de métodos:")

    animal = AnimalConSonido()
    perro = PerroConSonido()
    gato = GatoConSonido()

    print("Animal genérico:")
    animal.hacer_sonido()

    print("\nPerro:")
    perro.hacer_sonido()

    print("\nGato:")
    gato.hacer_sonido()

    print("\n8.3: Herencia Múltiple")
    print("-" * 40)

    class Terrestre:
        """Un animal que vive en tierra."""

        def caminar(self):
            """Los animales terrestres pueden caminar."""
            print("Puedo caminar en tierra")

    class Acuatico:
        """Un animal que vive en agua."""

        def nadar(self):
            """Los animales acuáticos pueden nadar."""
            print("Puedo nadar en agua")

    class Anfibio(Terrestre, Acuatico):
        """Un anfibio que vive tanto en tierra como en agua."""

        def respirar(self):
            """Los anfibios pueden respirar en múltiples entornos."""
            print("Puedo respirar en tierra y agua")

    # Ejemplo de herencia múltiple
    print("\nEjemplo - Herencia múltiple:")

    rana = Anfibio()
    print("Rana (anfibio):")
    rana.caminar()  # De Terrestre
    rana.nadar()  # De Acuatico
    rana.respirar()  # De Anfibio

    print("\n8.4: Polimorfismo")
    print("-" * 40)

    class AnimalPolimorfico:
        """Clase base para animales con comportamiento polimórfico."""

        def __init__(self, nombre):
            self.nombre = nombre

        def hacer_sonido(self):
            """Implementación base, para ser sobreescrita."""
            raise NotImplementedError("Las subclases deben implementar este método")

    class PerroPolimorfico(AnimalPolimorfico):
        """Un perro con comportamiento polimórfico."""

        def hacer_sonido(self):
            """Los perros ladran."""
            return f"{self.nombre} dice: ¡Guau guau!"

    class GatoPolimorfico(AnimalPolimorfico):
        """Un gato con comportamiento polimórfico."""

        def hacer_sonido(self):
            """Los gatos maúllan."""
            return f"{self.nombre} dice: ¡Miau miau!"

    class PatoPolimorfico(AnimalPolimorfico):
        """Un pato con comportamiento polimórfico."""

        def hacer_sonido(self):
            """Los patos graznan."""
            return f"{self.nombre} dice: ¡Cuá cuá!"

    def hacer_sonar_animal(animal):
        """
        Hace que un animal suene, independientemente de su tipo concreto.

        Esta función demuestra polimorfismo - funciona con cualquier objeto
        que tenga un método hacer_sonido, independientemente de su clase.
        """
        print(animal.hacer_sonido())

    # Ejemplo de polimorfismo
    print("\nEjemplo - Polimorfismo:")

    animales = [
        PerroPolimorfico("Fido"),
        GatoPolimorfico("Garfield"),
        PatoPolimorfico("Donald")
    ]

    print("Haciendo que cada animal haga su sonido:")
    for animal in animales:
        hacer_sonar_animal(animal)

    print("\nEsto demuestra polimorfismo - la función hacer_sonar_animal")
    print("funciona con cualquier objeto que tenga un método hacer_sonido,")
    print("independientemente de su clase concreta.")

    print("\nVentajas de la herencia y el polimorfismo:")
    print("- Reutilización de código")
    print("- Organización jerárquica de clases")
    print("- Flexibilidad para extender funcionalidades")
    print("- Código más mantenible y extensible")
    print("- Abstracción de comportamientos comunes")


# =============================================================================
# SECCIÓN 9: CLASE OBJECT Y REPRESENTACIÓN DE OBJETOS
# =============================================================================

def seccion_9_clase_object():
    """
    Demuestra la clase object y la representación de objetos en Python.

    Todas las clases en Python heredan de la clase object.
    Métodos especiales como __str__ y __repr__ pueden ser sobreescritos para personalizar
    la representación de objetos.
    """
    print("\n" + "=" * 80)
    print("SECCIÓN 9: CLASE OBJECT Y REPRESENTACIÓN DE OBJETOS")
    print("=" * 80)

    print("\n9.1: Herencia Implícita de Object")
    print("-" * 40)

    class MiClase:
        """Una clase simple que hereda implícitamente de object."""
        pass

    class MiClaseExplicita(object):
        """Una clase simple que hereda explícitamente de object."""
        pass

    # Ejemplo de herencia de object
    print("\nEjemplo - Herencia de object:")

    obj1 = MiClase()
    obj2 = MiClaseExplicita()

    print(f"Tipo de obj1: {type(obj1)}")
    print(f"Tipo de obj2: {type(obj2)}")

    print(f"\nobj1 es instancia de MiClase: {isinstance(obj1, MiClase)}")
    print(f"obj1 es instancia de object: {isinstance(obj1, object)}")

    print(f"\nobj2 es instancia de MiClaseExplicita: {isinstance(obj2, MiClaseExplicita)}")
    print(f"obj2 es instancia de object: {isinstance(obj2, object)}")

    print("\nTodas las clases en Python 3 heredan de object, ya sea implícita o explícitamente.")

    print("\n9.2: Representación de Objetos")
    print("-" * 40)

    class Producto:
        """
        Una clase que representa un producto con representación de cadena personalizada.
        """

        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

    # Sin personalización
    producto = Producto("Laptop", 1200)
    print(f"Representación predeterminada: {producto}")

    class ProductoConStr:
        """
        Una clase que representa un producto con un método __str__ personalizado.
        """

        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

        def __str__(self):
            """
            Devuelve una representación de cadena del producto.

            Este método se llama cuando se usa str(objeto) o print(objeto).
            """
            return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"

    # Con __str__ personalizado
    producto_con_str = ProductoConStr("Laptop", 1200)
    print(f"\nCon __str__ personalizado: {producto_con_str}")

    class ProductoConRepr:
        """
        Una clase que representa un producto con métodos __str__ y __repr__ personalizados.
        """

        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

        def __str__(self):
            """
            Devuelve una representación de cadena amigable para el usuario del producto.

            Este método se llama cuando se usa str(objeto) o print(objeto).
            """
            return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"

        def __repr__(self):
            """
            Devuelve una representación de cadena detallada del producto.

            Este método se llama cuando se usa repr(objeto) o cuando se
            muestra un objeto en una sesión interactiva sin print.

            Idealmente, debería devolver una cadena que, cuando se pasa a eval(),
            recrearía el objeto.
            """
            return f"ProductoConRepr('{self.nombre}', {self.precio})"

    # Con __str__ y __repr__ personalizados
    producto_con_repr = ProductoConRepr("Laptop", 1200)
    print(f"\nCon __str__ personalizado: {producto_con_repr}")
    print(f"Con __repr__ personalizado: {repr(producto_con_repr)}")

    print("\n9.3: Otros Métodos Especiales")
    print("-" * 40)

    class ProductoCompleto:
        """
        Una clase que representa un producto con varios métodos sobreescritos.
        """

        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

        def __str__(self):
            """Representación de cadena amigable para el usuario."""
            return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"

        def __repr__(self):
            """Representación de cadena detallada."""
            return f"ProductoCompleto('{self.nombre}', {self.precio})"

        def __eq__(self, other):
            """
            Compara este producto con otro.

            Dos productos se consideran iguales si tienen el mismo nombre y precio.

            Args:
                other: Otro objeto para comparar

            Returns:
                bool: True si son iguales, False en caso contrario
            """
            if not isinstance(other, ProductoCompleto):
                return False
            return self.nombre == other.nombre and self.precio == other.precio

        def __lt__(self, other):
            """
            Comparación menor que.

            Los productos se comparan por precio.

            Args:
                other: Otro producto para comparar

            Returns:
                bool: True si el precio de este producto es menor que el del otro
            """
            if not isinstance(other, ProductoCompleto):
                return NotImplemented
            return self.precio < other.precio

        def __hash__(self):
            """
            Devuelve un valor hash para el producto.

            Esto permite usar el producto como clave de diccionario o en un conjunto.

            Returns:
                int: Un valor hash basado en el nombre y el precio
            """
            return hash((self.nombre, self.precio))

    # Ejemplo de uso de métodos especiales
    print("\nEjemplo - Usando métodos especiales:")

    producto1 = ProductoCompleto("Laptop", 1200)
    producto2 = ProductoCompleto("Laptop", 1200)  # Mismo nombre y precio
    producto3 = ProductoCompleto("Smartphone", 800)

    print(f"producto1: {producto1}")
    print(f"producto2: {producto2}")
    print(f"producto3: {producto3}")

    print(f"\nproducto1 == producto2: {producto1 == producto2}")  # True
    print(f"producto1 == producto3: {producto1 == producto3}")  # False

    print(f"\nproducto1 < producto3: {producto1 < producto3}")  # False (1200 > 800)
    print(f"producto3 < producto1: {producto3 < producto1}")  # True (800 < 1200)

    # Uso como clave de diccionario
    productos_dict = {producto1: "En stock", producto3: "Agotado"}
    print(f"\nproducto1 en diccionario: {'En stock' if producto1 in productos_dict else 'No encontrado'}")
    print(
        f"producto2 en diccionario: {'En stock' if producto2 in productos_dict else 'No encontrado'}")  # También encuentra producto2 porque es igual a producto1

    print("\nMétodos especiales comunes:")
    print("- __str__: Representación de cadena para print() y str()")
    print("- __repr__: Representación de cadena detallada para depuración")
    print("- __eq__, __lt__, etc.: Comparaciones entre objetos")
    print("- __hash__: Para usar objetos como claves de diccionario")
    print("- __len__: Para len(objeto)")
    print("- __getitem__, __setitem__: Para acceso con corchetes (objeto[clave])")
    print("- __call__: Para hacer que el objeto sea callable (objeto())")
    print("- __enter__, __exit__: Para uso con el gestor de contexto (with)")


# =============================================================================
# EJERCICIOS
# =============================================================================

def ejercicios():
    """
    Proporciona ejercicios prácticos para reforzar los conceptos aprendidos.
    """
    print("\n" + "=" * 80)
    print("EJERCICIOS")
    print("=" * 80)

    print("\nEjercicio 1: Crear una Clase Básica")
    print("Crea una clase llamada 'Coche' con atributos para 'marca', 'modelo' y 'año'.")
    print("Incluye un método para mostrar la información del coche.")
    print("Crea al menos dos instancias con diferentes atributos.")

    print("\nEjercicio 2: Encapsulamiento")
    print("Implementa el encapsulamiento en una clase 'CuentaBancaria'.")
    print("Incluye atributos privados para 'titular' y 'saldo'.")
    print("Implementa métodos getter y setter para estos atributos.")
    print("Agrega métodos para 'depositar' y 'retirar' dinero con validación.")

    print("\nEjercicio 3: Herencia")
    print("Crea una clase base 'Vehiculo' con atributos y métodos comunes.")
    print("Crea clases derivadas 'Coche' y 'Motocicleta' que hereden de 'Vehiculo'.")
    print("Sobreescribe algunos métodos en las clases derivadas.")

    print("\nEjercicio 4: Sistema de Biblioteca")
    print("Crea un sistema de biblioteca con clases 'Libro' y 'Biblioteca'.")
    print("La clase 'Libro' debe tener propiedades para 'titulo', 'autor' y 'genero'.")
    print("La clase 'Biblioteca' debe permitir agregar libros y buscar por autor o género.")

    print("\nEjercicio 5: Polimorfismo")
    print("Crea una jerarquía de clases que demuestre polimorfismo.")
    print("Crea una clase base 'Figura' y clases derivadas como 'Cuadrado' y 'Circulo'.")
    print("Cada clase debe implementar un método 'calcular_area'.")
    print("Escribe una función que acepte cualquier figura y muestre su área.")

    print("\nLas soluciones a estos ejercicios se encuentran en el archivo 'ejercicios_soluciones.py'.")


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

def main():
    """
    Función principal para ejecutar el tutorial de POO.
    """
    print("\n" + "=" * 80)
    print("TUTORIAL DE PROGRAMACIÓN ORIENTADA A OBJETOS EN PYTHON")
    print("=" * 80)

    print("\nEste tutorial cubre los fundamentos de la Programación Orientada a Objetos en Python.")
    print("Cada sección se basa en las anteriores, por lo que se recomienda seguirlas en orden.")

    while True:
        print("\nSecciones disponibles:")
        print("1. Introducción a Clases y Objetos")
        print("2. Constructores en Python")
        print("3. Ejemplo Práctico - Clase Aritmética")
        print("4. Encapsulamiento en Python")
        print("5. Propiedades en Python")
        print("6. Atributos y Métodos de Clase")
        print("7. Módulos y Paquetes")
        print("8. Herencia y Polimorfismo")
        print("9. Clase Object y Representación de Objetos")
        print("10. Ejercicios")
        print("0. Salir")

        try:
            opcion = int(input("\nIngrese el número de sección a ejecutar (0-10): "))

            if opcion == 0:
                print("\n¡Gracias por utilizar este tutorial de POO en Python!")
                break
            elif opcion == 1:
                seccion_1_intro_clases_y_objetos()
            elif opcion == 2:
                seccion_2_constructores()
            elif opcion == 3:
                seccion_3_clase_aritmetica()
            elif opcion == 4:
                seccion_4_encapsulamiento()
            elif opcion == 5:
                seccion_5_propiedades()
            elif opcion == 6:
                seccion_6_atributos_y_metodos_clase()
            elif opcion == 7:
                seccion_7_modulos_y_paquetes()
            elif opcion == 8:
                seccion_8_herencia_y_polimorfismo()
            elif opcion == 9:
                seccion_9_clase_object()
            elif opcion == 10:
                ejercicios()
            else:
                print("\nOpción inválida. Por favor, ingrese un número entre 0 y 10.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.")

        input("\nPresione Enter para continuar...")


# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()