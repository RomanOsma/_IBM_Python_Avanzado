import os.path

from snack import Snack


class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'

    def __init__(self):
        self.snacks = []
        # Revisar si ya existe el archivo snacks
        # Si ya existe, obtenemos los snacks del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        # Sino, cargarmos algunos snacks iniciales
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Papas', 70),
            Snack('Refresco', 50),
            Snack('Sandwich', 120)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar snacks en archivo: {e}')

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    # 1,'Papas',70.0
                    # 2,'Refresco',50.0
                    id_snack, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f'Error al leer archivo de snacks: {e}')
        return snacks

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print('--- Snacks en el Inventario ---')
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks
