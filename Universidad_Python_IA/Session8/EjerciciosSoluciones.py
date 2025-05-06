# =============================================================================
# EJERCICIOS DE PROGRAMACIÓN ORIENTADA A OBJETOS EN PYTHON CON SOLUCIONES
# =============================================================================
"""
Este módulo contiene ejercicios sobre Programación Orientada a Objetos en Python
con soluciones detalladas para ayudar a reforzar los conceptos.

Cada ejercicio se enfoca en diferentes aspectos de la POO y se basa en los conceptos
cubiertos en el tutorial principal.
"""


# =============================================================================
# EJERCICIO 1: CREAR UNA CLASE BÁSICA
# =============================================================================

def ejercicio_1_clase_basica():
    """
    Ejercicio 1: Crear una clase básica que representa un coche.

    Requisitos:
    - Crear una clase llamada Coche
    - Incluir atributos para marca, modelo y año
    - Incluir un método para mostrar la información del coche
    - Crear al menos dos instancias de la clase con diferentes atributos
    """
    print("\n" + "=" * 80)
    print("EJERCICIO 1: CREAR UNA CLASE BÁSICA")
    print("=" * 80)

    print("\nEnunciado del problema:")
    print("Crear una clase llamada Coche con atributos para marca,")
    print("modelo y año. Incluir un método para mostrar la información del coche.")
    print("Crear al menos dos instancias con diferentes atributos.")

    print("\nSolución:")

    class Coche:
        """
        Una clase que representa un coche con atributos básicos.
        """

        def __init__(self, marca, modelo, año):
            """
            Inicializa un nuevo coche.

            Args:
                marca (str): La marca del coche
                modelo (str): El modelo del coche
                año (int): El año de fabricación del coche
            """
            self.marca = marca
            self.modelo = modelo
            self.año = año

        def mostrar_informacion(self):
            """Muestra la información del coche."""
            print(f"Coche: {self.marca} {self.modelo} ({self.año})")

    # Crear dos instancias de coche
    coche1 = Coche("Toyota", "Corolla", 2020)
    coche2 = Coche("Honda", "Civic", 2019)

    # Mostrar información de los coches
    print("Coche 1:")
    coche1.mostrar_informacion()

    print("\nCoche 2:")
    coche2.mostrar_informacion()

    print("\nExplicación:")
    print("1. Creamos una clase Coche con tres atributos: marca, modelo y año.")
    print("2. El método __init__ inicializa estos atributos cuando se crea un nuevo coche.")
    print("3. El método mostrar_informacion muestra la información del coche de manera formateada.")
    print("4. Creamos dos instancias de la clase con diferentes valores para los atributos.")
    print("5. Cada instancia mantiene su propio conjunto de valores de atributos.")


# =============================================================================
# EJERCICIO 2: ENCAPSULAMIENTO
# =============================================================================

def ejercicio_2_encapsulamiento():
    """
    Ejercicio 2: Implementar encapsulamiento en una clase de cuenta bancaria.

    Requisitos:
    - Crear una clase llamada CuentaBancaria
    - Incluir atributos privados para _titular y _saldo
    - Implementar métodos getter y setter para estos atributos
    - Incluir validación en los métodos setter
    - Implementar métodos para depositar y retirar
    - Crear una instancia y probar los métodos
    """
    print("\n" + "=" * 80)
    print("EJERCICIO 2: ENCAPSULAMIENTO")
    print("=" * 80)

    print("\nEnunciado del problema:")
    print("Crear una clase llamada CuentaBancaria con atributos privados")
    print("para _titular y _saldo. Implementar métodos getter y setter")
    print("para estos atributos con validación. Incluir métodos para depositar")
    print("y retirar. Crear una instancia y probar los métodos.")

    print("\nSolución:")

    class CuentaBancaria:
        """
        Una clase que representa una cuenta bancaria con encapsulamiento.
        """

        def __init__(self, titular, saldo_inicial=0):
            """
            Inicializa una nueva cuenta bancaria.

            Args:
                titular (str): El nombre del titular de la cuenta
                saldo_inicial (float, opcional): El saldo inicial (por defecto: 0)
            """
            self._titular = titular
            # Validar saldo inicial
            if saldo_inicial < 0:
                raise ValueError("El saldo inicial no puede ser negativo")
            self._saldo = saldo_inicial

        # Getter y setter para titular
        def get_titular(self):
            """Obtiene el nombre del titular de la cuenta."""
            return self._titular

        def set_titular(self, titular):
            """
            Establece el nombre del titular de la cuenta.

            Args:
                titular (str): El nuevo nombre del titular

            Raises:
                ValueError: Si el nombre está vacío
            """
            if not titular:
                raise ValueError("El nombre del titular no puede estar vacío")
            self._titular = titular

        # Getter y setter para saldo
        def get_saldo(self):
            """Obtiene el saldo actual."""
            return self._saldo

        def set_saldo(self, saldo):
            """
            Establece el saldo de la cuenta.

            Args:
                saldo (float): El nuevo saldo

            Raises:
                ValueError: Si el saldo es negativo
            """
            if saldo < 0:
                raise ValueError("El saldo no puede ser negativo")
            self._saldo = saldo

        # Métodos de negocio
        def depositar(self, cantidad):
            """
            Deposita dinero en la cuenta.

            Args:
                cantidad (float): La cantidad a depositar

            Raises:
                ValueError: Si la cantidad es negativa o cero

            Returns:
                float: El nuevo saldo
            """
            if cantidad <= 0:
                raise ValueError("La cantidad a depositar debe ser positiva")
            self._saldo += cantidad
            print(f"Depósito de ${cantidad:.2f} realizado. Nuevo saldo: ${self._saldo:.2f}")
            return self._saldo

        def retirar(self, cantidad):
            """
            Retira dinero de la cuenta.

            Args:
                cantidad (float): La cantidad a retirar

            Raises:
                ValueError: Si la cantidad es negativa o cero,
                           o si excede el saldo actual

            Returns:
                float: El nuevo saldo
            """
            if cantidad <= 0:
                raise ValueError("La cantidad a retirar debe ser positiva")
            if cantidad > self._saldo:
                raise ValueError("Fondos insuficientes")
            self._saldo -= cantidad
            print(f"Retiro de ${cantidad:.2f} realizado. Nuevo saldo: ${self._saldo:.2f}")
            return self._saldo

    # Crear una cuenta bancaria
    try:
        print("Creando cuenta para 'Juan Pérez' con saldo inicial de $1000...")
        cuenta = CuentaBancaria("Juan Pérez", 1000)

        # Mostrar información inicial
        print(f"Titular: {cuenta.get_titular()}")
        print(f"Saldo inicial: ${cuenta.get_saldo():.2f}")

        # Probar métodos de depósito y retiro
        print("\nProbando métodos de depósito y retiro:")
        cuenta.depositar(500)
        cuenta.retirar(200)

        # Intentar retirar demasiado
        print("\nIntentando retirar más del saldo:")
        try:
            cuenta.retirar(2000)
        except ValueError as e:
            print(f"Error: {e}")

        # Cambiar el nombre del titular
        print("\nCambiando el nombre del titular:")
        cuenta.set_titular("Juan Alberto Pérez")
        print(f"Nuevo titular: {cuenta.get_titular()}")

        # Intentar establecer un nombre de titular inválido
        print("\nIntentando establecer un nombre de titular vacío:")
        try:
            cuenta.set_titular("")
        except ValueError as e:
            print(f"Error: {e}")

        # Intentar crear una cuenta con saldo negativo
        print("\nIntentando crear una cuenta con saldo negativo:")
        try:
            cuenta_invalida = CuentaBancaria("Pedro Gómez", -100)
        except ValueError as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    print("\nExplicación:")
    print("1. Creamos una clase CuentaBancaria con atributos privados _titular y _saldo.")
    print("2. Implementamos métodos getter y setter para cada atributo con validación.")
    print("3. Agregamos métodos para depositar y retirar con validación apropiada.")
    print("4. Probamos la clase creando una instancia y llamando a varios métodos.")
    print("5. Demostramos cómo el encapsulamiento protege los datos mediante validación.")


# =============================================================================
# EJERCICIO 3: HERENCIA
# =============================================================================

def ejercicio_3_herencia():
    """
    Ejercicio 3: Implementar herencia con una jerarquía de vehículos.

    Requisitos:
    - Crear una clase base llamada Vehiculo con atributos y métodos comunes
    - Crear clases derivadas para diferentes tipos de vehículos: Coche, Motocicleta
    - Sobreescribir métodos en las clases derivadas para proporcionar implementaciones específicas
    - Crear instancias de cada clase y demostrar polimorfismo
    """
    print("\n" + "=" * 80)
    print("EJERCICIO 3: HERENCIA")
    print("=" * 80)

    print("\nEnunciado del problema:")
    print("Crear una clase base llamada Vehiculo con atributos y métodos comunes.")
    print("Crear clases derivadas para diferentes tipos de vehículos: Coche, Motocicleta.")
    print("Sobreescribir métodos en las clases derivadas para proporcionar implementaciones específicas.")
    print("Crear instancias de cada clase y demostrar polimorfismo.")

    print("\nSolución:")

    class Vehiculo:
        """
        Clase base para todos los vehículos.
        """

        def __init__(self, marca, modelo, año):
            """
            Inicializa un nuevo vehículo.

            Args:
                marca (str): La marca del vehículo
                modelo (str): El modelo del vehículo
                año (int): El año de fabricación del vehículo
            """
            self.marca = marca
            self.modelo = modelo
            self.año = año
            self.encendido = False
            self.velocidad = 0

        def encender(self):
            """Enciende el vehículo."""
            if not self.encendido:
                self.encendido = True
                print(f"El {self.__class__.__name__} está encendido")
            else:
                print(f"El {self.__class__.__name__} ya está encendido")

        def apagar(self):
            """Apaga el vehículo."""
            if self.encendido:
                self.encendido = False
                self.velocidad = 0
                print(f"El {self.__class__.__name__} está apagado")
            else:
                print(f"El {self.__class__.__name__} ya está apagado")

        def acelerar(self, incremento):
            """
            Acelera el vehículo.

            Args:
                incremento (int): La cantidad de aumento de velocidad

            Returns:
                int: La nueva velocidad
            """
            if not self.encendido:
                print(f"No se puede acelerar. El {self.__class__.__name__} está apagado")
                return self.velocidad

            self.velocidad += incremento
            print(f"El {self.__class__.__name__} ha acelerado a {self.velocidad} km/h")
            return self.velocidad

        def frenar(self, decremento):
            """
            Frena el vehículo.

            Args:
                decremento (int): La cantidad de disminución de velocidad

            Returns:
                int: La nueva velocidad
            """
            if not self.encendido:
                print(f"No se puede frenar. El {self.__class__.__name__} está apagado")
                return self.velocidad

            self.velocidad = max(0, self.velocidad - decremento)
            print(f"El {self.__class__.__name__} ha frenado a {self.velocidad} km/h")
            return self.velocidad

        def mostrar_informacion(self):
            """Muestra la información del vehículo."""
            estado = "encendido" if self.encendido else "apagado"
            print(f"{self.__class__.__name__}: {self.marca} {self.modelo} ({self.año})")
            print(f"Estado: {estado}")
            print(f"Velocidad actual: {self.velocidad} km/h")

    class Coche(Vehiculo):
        """
        Una clase que representa un coche, derivada de Vehículo.
        """

        def __init__(self, marca, modelo, año, puertas):
            """
            Inicializa un nuevo coche.

            Args:
                marca (str): La marca del coche
                modelo (str): El modelo del coche
                año (int): El año de fabricación del coche
                puertas (int): El número de puertas
            """
            super().__init__(marca, modelo, año)
            self.puertas = puertas
            self.aire_acondicionado = False

        def activar_aire_acondicionado(self):
            """Activa el aire acondicionado."""
            if not self.encendido:
                print("No se puede activar el aire acondicionado. El coche está apagado")
                return

            if not self.aire_acondicionado:
                self.aire_acondicionado = True
                print("Aire acondicionado activado")
            else:
                print("El aire acondicionado ya está activado")

        def desactivar_aire_acondicionado(self):
            """Desactiva el aire acondicionado."""
            if not self.encendido:
                print("No se puede desactivar el aire acondicionado. El coche está apagado")
                return

            if self.aire_acondicionado:
                self.aire_acondicionado = False
                print("Aire acondicionado desactivado")
            else:
                print("El aire acondicionado ya está desactivado")

        def mostrar_informacion(self):
            """Muestra la información del coche."""
            super().mostrar_informacion()
            print(f"Número de puertas: {self.puertas}")
            aire = "activado" if self.aire_acondicionado else "desactivado"
            print(f"Aire acondicionado: {aire}")

    class Motocicleta(Vehiculo):
        """
        Una clase que representa una motocicleta, derivada de Vehículo.
        """

        def __init__(self, marca, modelo, año, tipo):
            """
            Inicializa una nueva motocicleta.

            Args:
                marca (str): La marca de la motocicleta
                modelo (str): El modelo de la motocicleta
                año (int): El año de fabricación de la motocicleta
                tipo (str): El tipo de motocicleta (deportiva, crucero, etc.)
            """
            super().__init__(marca, modelo, año)
            self.tipo = tipo
            self.pata_de_apoyo = True

        def hacer_caballito(self):
            """Realiza un caballito."""
            if not self.encendido:
                print("No se puede hacer un caballito. La motocicleta está apagada")
                return

            if self.velocidad < 10:
                print("No se puede hacer un caballito. La velocidad es muy baja")
                return

            print("¡Haciendo un caballito!")

        def activar_pata_de_apoyo(self):
            """Activa la pata de apoyo."""
            if self.encendido and self.velocidad > 0:
                print("No se puede activar la pata de apoyo mientras se está en movimiento")
                return

            if not self.pata_de_apoyo:
                self.pata_de_apoyo = True
                print("Pata de apoyo activada")
            else:
                print("La pata de apoyo ya está activada")

        def desactivar_pata_de_apoyo(self):
            """Desactiva la pata de apoyo."""
            if not self.pata_de_apoyo:
                print("La pata de apoyo ya está desactivada")
                return

            self.pata_de_apoyo = False
            print("Pata de apoyo desactivada")

        def mostrar_informacion(self):
            """Muestra la información de la motocicleta."""
            super().mostrar_informacion()
            print(f"Tipo: {self.tipo}")
            pata = "activada" if self.pata_de_apoyo else "desactivada"
            print(f"Pata de apoyo: {pata}")

    # Ejemplo de uso de la jerarquía de vehículos
    print("\nEjemplo - Jerarquía de vehículos:")

    # Crear instancias
    coche = Coche("Toyota", "Corolla", 2020, 4)
    moto = Motocicleta("Honda", "CBR", 2019, "Deportiva")

    # Probando la clase Coche
    print("\nProbando el Coche:")
    coche.mostrar_informacion()

    print("\nOperaciones con el Coche:")
    coche.encender()
    coche.activar_aire_acondicionado()
    coche.acelerar(30)
    coche.frenar(10)
    coche.desactivar_aire_acondicionado()
    coche.apagar()

    # Probando la clase Motocicleta
    print("\nProbando la Motocicleta:")
    moto.mostrar_informacion()

    print("\nOperaciones con la Motocicleta:")
    moto.encender()
    moto.desactivar_pata_de_apoyo()
    moto.acelerar(20)
    moto.hacer_caballito()  # Velocidad muy baja
    moto.acelerar(30)  # Ahora a 50 km/h
    moto.hacer_caballito()  # Ahora sí puede
    moto.frenar(30)
    moto.activar_pata_de_apoyo()  # No se puede mientras se mueve
    moto.frenar(20)  # Ahora a 0 km/h
    moto.activar_pata_de_apoyo()
    moto.apagar()

    # Demostrando polimorfismo
    print("\nDemostrando polimorfismo:")

    def probar_vehiculo(vehiculo):
        """
        Prueba un vehículo independientemente de su tipo concreto.

        Esta función demuestra polimorfismo - funciona con cualquier objeto
        que sea un Vehiculo, independientemente de su clase concreta.

        Args:
            vehiculo: Un objeto de tipo Vehiculo o una subclase
        """
        print(f"\nProbando un {vehiculo.__class__.__name__}:")
        vehiculo.encender()
        vehiculo.acelerar(50)
        vehiculo.frenar(20)
        vehiculo.mostrar_informacion()
        vehiculo.apagar()

    # Usar la misma función con diferentes tipos de vehículos
    probar_vehiculo(coche)
    probar_vehiculo(moto)

    print("\nExplicación:")
    print("1. Creamos una clase base Vehiculo con atributos y métodos comunes.")
    print("2. Implementamos clases derivadas Coche y Motocicleta con características específicas.")
    print("3. Sobreescribimos el método mostrar_informacion en ambas clases derivadas.")
    print("4. Agregamos métodos específicos a cada clase derivada.")
    print("5. Demostramos polimorfismo usando una función probar_vehiculo que funciona con cualquier tipo de vehículo.")
    print("6. La función probar_vehiculo llama a los métodos apropiados según el tipo de objeto.")


# =============================================================================
# EJERCICIO 4: SISTEMA DE BIBLIOTECA
# =============================================================================

def ejercicio_4_sistema_biblioteca():
    """
    Ejercicio 4: Crear un sistema de biblioteca con propiedades.

    Requisitos:
    - Crear una clase Libro con propiedades para título, autor y género
    - Crear una clase Biblioteca para gestionar libros
    - Implementar métodos para agregar libros y buscar por autor o género
    - Usar propiedades para acceder a los atributos
    """
    print("\n" + "=" * 80)
    print("EJERCICIO 4: SISTEMA DE BIBLIOTECA")
    print("=" * 80)

    print("\nEnunciado del problema:")
    print("Crear una clase Libro con propiedades para título, autor y género.")
    print("Crear una clase Biblioteca para gestionar libros.")
    print("Implementar métodos para agregar libros y buscar por autor o género.")
    print("Usar propiedades para acceder a los atributos.")

    print("\nSolución:")

    class Libro:
        """
        Una clase que representa un libro con propiedades.
        """

        def __init__(self, titulo, autor, genero):
            """
            Inicializa un nuevo libro.

            Args:
                titulo (str): El título del libro
                autor (str): El autor del libro
                genero (str): El género del libro
            """
            self._titulo = titulo
            self._autor = autor
            self._genero = genero

        @property
        def titulo(self):
            """Obtiene el título del libro."""
            return self._titulo

        @titulo.setter
        def titulo(self, titulo):
            """
            Establece el título del libro.

            Args:
                titulo (str): El nuevo título

            Raises:
                ValueError: Si el título está vacío
            """
            if not titulo:
                raise ValueError("El título no puede estar vacío")
            self._titulo = titulo

        @property
        def autor(self):
            """Obtiene el autor del libro."""
            return self._autor

        @autor.setter
        def autor(self, autor):
            """
            Establece el autor del libro.

            Args:
                autor (str): El nuevo autor

            Raises:
                ValueError: Si el autor está vacío
            """
            if not autor:
                raise ValueError("El autor no puede estar vacío")
            self._autor = autor

        @property
        def genero(self):
            """Obtiene el género del libro."""
            return self._genero

        @genero.setter
        def genero(self, genero):
            """
            Establece el género del libro.

            Args:
                genero (str): El nuevo género

            Raises:
                ValueError: Si el género está vacío
            """
            if not genero:
                raise ValueError("El género no puede estar vacío")
            self._genero = genero

        def __str__(self):
            """Representación de cadena del libro."""
            return f"{self.titulo} - {self.autor} ({self.genero})"

    class Biblioteca:
        """
        Una clase que representa una biblioteca que gestiona libros.
        """

        def __init__(self, nombre):
            """
            Inicializa una nueva biblioteca.

            Args:
                nombre (str): El nombre de la biblioteca
            """
            self._nombre = nombre
            self._libros = []

        @property
        def nombre(self):
            """Obtiene el nombre de la biblioteca."""
            return self._nombre

        @property
        def libros(self):
            """Obtiene la lista de libros."""
            return self._libros

        def agregar_libro(self, libro):
            """
            Agrega un libro a la biblioteca.

            Args:
                libro (Libro): El libro a agregar
            """
            self._libros.append(libro)
            print(f"Libro '{libro.titulo}' agregado a la biblioteca")

        def buscar_libros_por_autor(self, autor):
            """
            Busca libros por autor.

            Args:
                autor (str): El autor a buscar

            Returns:
                list: Lista de libros del autor especificado
            """
            libros_encontrados = [libro for libro in self._libros if libro.autor == autor]
            return libros_encontrados

        def buscar_libros_por_genero(self, genero):
            """
            Busca libros por género.

            Args:
                genero (str): El género a buscar

            Returns:
                list: Lista de libros del género especificado
            """
            libros_encontrados = [libro for libro in self._libros if libro.genero == genero]
            return libros_encontrados

        def mostrar_todos_los_libros(self):
            """Muestra todos los libros de la biblioteca."""
            if not self._libros:
                print(f"La biblioteca {self.nombre} no tiene libros")
                return

            print(f"\nLibros en la biblioteca {self.nombre}:")
            for i, libro in enumerate(self._libros, 1):
                print(f"{i}. {libro}")

        def mostrar_resultados_busqueda(self, libros, criterio):
            """
            Muestra los resultados de una búsqueda.

            Args:
                libros (list): Lista de libros encontrados
                criterio (str): El criterio de búsqueda
            """
            if not libros:
                print(f"No se encontraron libros para el criterio: {criterio}")
                return

            print(f"\nLibros encontrados para {criterio}:")
            for i, libro in enumerate(libros, 1):
                print(f"{i}. {libro}")

    # Ejemplo de uso del sistema de biblioteca
    print("\nEjemplo - Sistema de Biblioteca:")

    # Crear biblioteca
    biblioteca = Biblioteca("Biblioteca Municipal")

    # Crear libros
    libros = [
        Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico"),
        Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela romántica"),
        Libro("El código Da Vinci", "Dan Brown", "Thriller"),
        Libro("Inferno", "Dan Brown", "Thriller"),
        Libro("1984", "George Orwell", "Distopía"),
        Libro("Rebelión en la granja", "George Orwell", "Fábula política")
    ]

    # Agregar libros a la biblioteca
    for libro in libros:
        biblioteca.agregar_libro(libro)

    # Mostrar todos los libros
    biblioteca.mostrar_todos_los_libros()

    # Buscar libros por autor
    autores_a_buscar = ["Gabriel García Márquez", "Dan Brown", "J.K. Rowling"]

    for autor in autores_a_buscar:
        libros_encontrados = biblioteca.buscar_libros_por_autor(autor)
        biblioteca.mostrar_resultados_busqueda(libros_encontrados, f"autor '{autor}'")

    # Buscar libros por género
    generos_a_buscar = ["Thriller", "Ciencia ficción", "Distopía"]

    for genero in generos_a_buscar:
        libros_encontrados = biblioteca.buscar_libros_por_genero(genero)
        biblioteca.mostrar_resultados_busqueda(libros_encontrados, f"género '{genero}'")

    # Modificar un libro usando propiedades
    print("\nModificando un libro:")
    libro_a_modificar = libros[0]
    print(f"Libro original: {libro_a_modificar}")

    libro_a_modificar.titulo = "Cien años de soledad (Edición especial)"
    libro_a_modificar.genero = "Novela literaria"

    print(f"Libro modificado: {libro_a_modificar}")

    # Volver a mostrar todos los libros
    biblioteca.mostrar_todos_los_libros()

    print("\nExplicación:")
    print("1. Creamos una clase Libro con propiedades para título, autor y género.")
    print("2. Usamos el decorador @property para proporcionar acceso controlado a los atributos.")
    print("3. Agregamos validación a los setters para prevenir valores inválidos.")
    print("4. Creamos una clase Biblioteca para gestionar una colección de libros.")
    print("5. Implementamos métodos para agregar y buscar libros por diferentes criterios.")
    print("6. Demostramos cómo las propiedades permiten modificar atributos con validación.")


# =============================================================================
# EJERCICIO 5: POLIMORFISMO
# =============================================================================

def ejercicio_5_polimorfismo():
    """
    Ejercicio 5: Implementar polimorfismo con una jerarquía de figuras geométricas.

    Requisitos:
    - Crear una clase base abstracta Figura
    - Crear clases derivadas como Cuadrado, Círculo y Triángulo
    - Cada clase debe implementar un método calcular_area
    - Escribir una función que acepte cualquier figura y muestre su área
    """
    print("\n" + "=" * 80)
    print("EJERCICIO 5: POLIMORFISMO")
    print("=" * 80)

    print("\nEnunciado del problema:")
    print("Crear una clase base abstracta Figura.")
    print("Crear clases derivadas como Cuadrado, Círculo y Triángulo.")
    print("Cada clase debe implementar un método calcular_area.")
    print("Escribir una función que acepte cualquier figura y muestre su área.")

    print("\nSolución:")

    import math
    from abc import ABC, abstractmethod

    class Figura(ABC):
        """
        Clase base abstracta para todas las figuras geométricas.
        """

        def __init__(self):
            """Inicializa una nueva figura."""
            pass

        @abstractmethod
        def calcular_area(self) -> float:
            """
            Calcula el área de la figura.

            Este método debe ser implementado por todas las subclases.

            Returns:
                float: El área de la figura
            """
            pass

        @abstractmethod
        def calcular_perimetro(self) -> float:
            """
            Calcula el perímetro de la figura.

            Este método debe ser implementado por todas las subclases.

            Returns:
                float: El perímetro de la figura
            """
            pass

        def __str__(self):
            """Representación de cadena de la figura."""
            return f"{self.__class__.__name__}"

    class Cuadrado(Figura):
        """
        Una clase que representa un cuadrado.
        """

        def __init__(self, lado):
            """
            Inicializa un nuevo cuadrado.

            Args:
                lado (float): La longitud del lado del cuadrado
            """
            super().__init__()
            self.lado = lado

        def calcular_area(self):
            """
            Calcula el área del cuadrado.

            Returns:
                float: El área del cuadrado (lado^2)
            """
            return self.lado ** 2

        def calcular_perimetro(self):
            """
            Calcula el perímetro del cuadrado.

            Returns:
                float: El perímetro del cuadrado (4 * lado)
            """
            return 4 * self.lado

        def __str__(self):
            """Representación de cadena del cuadrado."""
            return f"Cuadrado de lado {self.lado}"

    class Circulo(Figura):
        """
        Una clase que representa un círculo.
        """

        def __init__(self, radio):
            """
            Inicializa un nuevo círculo.

            Args:
                radio (float): El radio del círculo
            """
            super().__init__()
            self.radio = radio

        def calcular_area(self):
            """
            Calcula el área del círculo.

            Returns:
                float: El área del círculo (π * radio^2)
            """
            return math.pi * (self.radio ** 2)

        def calcular_perimetro(self):
            """
            Calcula el perímetro (circunferencia) del círculo.

            Returns:
                float: El perímetro del círculo (2 * π * radio)
            """
            return 2 * math.pi * self.radio

        def __str__(self):
            """Representación de cadena del círculo."""
            return f"Círculo de radio {self.radio}"

    class Triangulo(Figura):
        """
        Una clase que representa un triángulo (utilizando la fórmula de Herón).
        """

        def __init__(self, lado1, lado2, lado3):
            """
            Inicializa un nuevo triángulo.

            Args:
                lado1 (float): La longitud del primer lado
                lado2 (float): La longitud del segundo lado
                lado3 (float): La longitud del tercer lado

            Raises:
                ValueError: Si los lados no pueden formar un triángulo
            """
            # Verificar si los lados pueden formar un triángulo
            if (lado1 + lado2 <= lado3) or (lado1 + lado3 <= lado2) or (lado2 + lado3 <= lado1):
                raise ValueError("Los lados proporcionados no pueden formar un triángulo")

            super().__init__()
            self.lado1 = lado1
            self.lado2 = lado2
            self.lado3 = lado3

        def calcular_area(self):
            """
            Calcula el área del triángulo usando la fórmula de Herón.

            Returns:
                float: El área del triángulo
            """
            # Semiperímetro
            s = (self.lado1 + self.lado2 + self.lado3) / 2

            # Fórmula de Herón
            area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
            return area

        def calcular_perimetro(self):
            """
            Calcula el perímetro del triángulo.

            Returns:
                float: El perímetro del triángulo (suma de todos los lados)
            """
            return self.lado1 + self.lado2 + self.lado3

        def __str__(self):
            """Representación de cadena del triángulo."""
            return f"Triángulo de lados {self.lado1}, {self.lado2} y {self.lado3}"

    class Rectangulo(Figura):
        """
        Una clase que representa un rectángulo.
        """

        def __init__(self, base, altura):
            """
            Inicializa un nuevo rectángulo.

            Args:
                base (float): La base del rectángulo
                altura (float): La altura del rectángulo
            """
            super().__init__()
            self.base = base
            self.altura = altura

        def calcular_area(self):
            """
            Calcula el área del rectángulo.

            Returns:
                float: El área del rectángulo (base * altura)
            """
            return self.base * self.altura

        def calcular_perimetro(self):
            """
            Calcula el perímetro del rectángulo.

            Returns:
                float: El perímetro del rectángulo (2 * (base + altura))
            """
            return 2 * (self.base + self.altura)

        def __str__(self):
            """Representación de cadena del rectángulo."""
            return f"Rectángulo de base {self.base} y altura {self.altura}"

    def mostrar_informacion_figura(figura):
        """
        Muestra información sobre una figura.

        Esta función demuestra polimorfismo - funciona con cualquier objeto
        que sea una Figura, independientemente de su clase concreta.

        Args:
            figura (Figura): La figura a mostrar
        """
        print(f"\nInformación de {figura}:")
        print(f"Área: {figura.calcular_area():.2f}")
        print(f"Perímetro: {figura.calcular_perimetro():.2f}")

    # Ejemplo de uso de las figuras con polimorfismo
    print("\nEjemplo - Figuras geométricas con polimorfismo:")

    try:
        # Crear varias figuras
        cuadrado = Cuadrado(5)
        circulo = Circulo(3)
        triangulo = Triangulo(3, 4, 5)  # Triángulo rectángulo 3-4-5
        rectangulo = Rectangulo(4, 6)

        # Recopilar todas las figuras en una lista
        figuras = [cuadrado, circulo, triangulo, rectangulo]

        # Usar la función polimórfica con cada figura
        for figura in figuras:
            mostrar_informacion_figura(figura)

        # Intentar crear un triángulo inválido
        print("\nIntentando crear un triángulo inválido:")
        try:
            triangulo_invalido = Triangulo(1, 1, 10)  # Estos lados no pueden formar un triángulo
        except ValueError as e:
            print(f"Error: {e}")

        # Calcular el área total de todas las figuras
        area_total = sum(figura.calcular_area() for figura in figuras)
        print(f"\nÁrea total de todas las figuras: {area_total:.2f}")

        # Encontrar la figura con el perímetro más grande
        figura_mayor_perimetro = max(figuras, key=lambda f: f.calcular_perimetro())
        print(f"Figura con mayor perímetro: {figura_mayor_perimetro}")
        print(f"Perímetro: {figura_mayor_perimetro.calcular_perimetro():.2f}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    print("\nExplicación:")
    print("1. Creamos una clase base abstracta Figura usando ABC (Abstract Base Class).")
    print(
        "2. Definimos métodos abstractos calcular_area y calcular_perimetro que deben ser implementados por las subclases.")
    print("3. Implementamos diferentes clases de figuras que heredan de Figura.")
    print("4. Cada clase implementa sus propios métodos calcular_area y calcular_perimetro.")
    print("5. Creamos una función mostrar_informacion_figura que funciona con cualquier tipo de Figura.")
    print(
        "6. Esto demuestra polimorfismo: un objeto puede ser tratado como su clase base, pero el comportamiento depende del tipo concreto.")


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================

def main():
    """
    Función principal para ejecutar los ejercicios de POO.
    """
    print("\n" + "=" * 80)
    print("EJERCICIOS DE PROGRAMACIÓN ORIENTADA A OBJETOS EN PYTHON")
    print("=" * 80)

    print("\nEjercicios disponibles:")
    print("1. Crear una Clase Básica")
    print("2. Encapsulamiento")
    print("3. Herencia")
    print("4. Sistema de Biblioteca")
    print("5. Polimorfismo")

    # Ejecutar todos los ejercicios en orden para demostración
    print("\n" + "=" * 80)
    print("EJECUTANDO TODOS LOS EJERCICIOS EN ORDEN")
    print("=" * 80)

    ejercicio_1_clase_basica()
    ejercicio_2_encapsulamiento()
    ejercicio_3_herencia()
    ejercicio_4_sistema_biblioteca()
    ejercicio_5_polimorfismo()

    print("\n" + "=" * 80)
    print("¡EJERCICIOS COMPLETADOS!")
    print("=" * 80)
    print("\n¡Gracias por completar los ejercicios de POO en Python!")


# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()