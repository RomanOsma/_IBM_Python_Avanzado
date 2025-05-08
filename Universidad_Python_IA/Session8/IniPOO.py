# ============================================================
# GUÍA DE ESTUDIO: Programación Orientada a Objetos (POO) en Python
# ============================================================
# Temas: Clases, Objetos, Constructores, Encapsulamiento, Herencia, Polimorfismo, Métodos y Atributos de Clase
# ============================================================


# -------------------------------
# 1. DEFINICIÓN DE UNA CLASE Y CREACIÓN DE OBJETOS
# -------------------------------

class Persona:
    # Constructor de la clase
    def __init__(self, nombre, apellido):
        # Atributos de instancia
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_contacto(self):
        print(f"Persona: Nombre: {self.nombre} Apellido: {self.apellido}")

# Ejemplo de creación de objetos
if __name__ == '__main__': #Crea un objeto de la clase Persona vacio
    persona1 = Persona('Layla', 'Acosta')
    persona1.mostrar_contacto()
    print()
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar_contacto()

# -------------------------------
# 2. CONSTRUCTORES Y DIRECCIONES DE MEMORIA
# -------------------------------

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_contacto(self):
        print(f"Persona: Nombre: {self.nombre} Apellido: {self.apellido}")
        print(f"Dir. mem self: {id(self)}")
        print(f"Dir. mem hex self: {hex(id(self))}")

if __name__ == '__main__':
    persona1 = Persona('Layla', 'Acosta')
    persona1.mostrar_contacto()
    print(f"Dir. mem persona1: {id(persona1)}")
    print(f"Dir. mem hex persona1: {hex(id(persona1))}")
    print()
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar_contacto()
    print(f"Dir. mem persona2: {id(persona2)}")
    print(f"Dir. mem hex persona2: {hex(id(persona2))}")

# -------------------------------
# 3. EJEMPLO: CLASE ARITMÉTICA
# -------------------------------

class Aritmetica:
    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')

    # Completar con multiplicar y dividir
    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        if self.operando2 != 0:
            resultado = self.operando1 / self.operando2
            print(f'Resultado división: {resultado}')
        else:
            print('Error: División por cero')

if __name__ == '__main__':
    print('*** Ejemplo Clase Aritmetica ***')
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    print()
    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.restar()

# -------------------------------
# 4. ENCAPSULAMIENTO Y GET/SET
# -------------------------------

class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca      # protegido
        self._modelo = modelo    # protegido
        self.__color = color     # privado

    def conducir(self):
        print(f"Conduciendo el coche: Marca: {self._marca} Modelo: {self._modelo} Color: {self.__color}")

    # Métodos get/set para encapsulamiento
    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

if __name__ == '__main__':
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # Uso de métodos get/set
    coche1.set_marca('Toyota 2')
    coche1.set_modelo('Yaris 2')
    coche1.set_color('Azul 2')
    coche1.conducir()

# -------------------------------
# 5. ATRIBUTOS Y MÉTODOS DE CLASE
# -------------------------------

class Persona:
    contador_personas = 0  # atributo de clase

    def __init__(self, nombre, apellido):
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('Método estático')
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        print('Método de clase')
        return cls.contador_personas

if __name__ == '__main__':
    persona1 = Persona('Gerardo','Perez')
    persona1.mostrar_persona()
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()
    print(f'Contador objetos Persona: {Persona.contador_personas}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}')

# -------------------------------
# 6. HERENCIA Y POLIMORFISMO
# -------------------------------

class Animal:
    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')

    def hacer_sonido(self):
        print('Hago un pitido...')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    def dormir(self):
        print('Duermo 15 horas al día')  # Sobreescritura

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

if __name__ == '__main__':
    print('*** Ejemplo de Herencia en Python ***')
    animal1 = Animal()
    animal1.comer()
    animal1.dormir()
    print('\nClase Hija, soy un Perro')
    perro1 = Perro()
    perro1.comer()
    perro1.dormir()
    perro1.hacer_sonido()
    print('\nClase Hija Gato:')
    gato1 = Gato()
    gato1.hacer_sonido()

# -------------------------------
# 7. PROPIEDADES CON @property
# -------------------------------

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

# -------------------------------
# 8. CLASES COMPUESTAS: SISTEMA DE BIBLIOTECA
# -------------------------------

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

    def buscar_libros_por_genero(self, genero):
        for libro in self._libros:
            if libro.genero == genero:
                self.mostrar_libro(libro)

    def mostrar_todos_los_libros(self):
        print(f'\nTodos los libros de la biblioteca {self.nombre}:')
        for libro in self.libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self, libro):
        print(f'Libro -> Titulo: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}')

    @property
    def nombre(self):
        return self._nombre

    @property
    def libros(self):
        return self._libros

# -------------------------------
# 9. SOBRESCRITURA DE MÉTODOS ESPECIALES
# -------------------------------

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Persona nombre = {self.nombre} apellido = {self.apellido} Dir. Mem. {super().__str__()}'

if __name__ == '__main__':
    persona1 = Persona('Ana', 'Martinez')
    print(persona1)

# ============================================================
# FIN DE LA GUÍA DE ESTUDIO DE POO EN PYTHON
# ============================================================
