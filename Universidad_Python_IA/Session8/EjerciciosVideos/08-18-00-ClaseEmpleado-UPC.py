class Empleado:
    contador_empleados = 0

    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleados += 1

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados

    