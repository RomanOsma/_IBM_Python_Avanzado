class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribir el metodo __str__
    def __str__(self):
        return f'''Persona
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. Mem. {super.__str__(self)}'''


# Codigo principal
persona1 = Persona('Ana', 'Martinez')
#print(persona1.__str__())  # El metodo str se llama automaticamente desde print
print(persona1)
