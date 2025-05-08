import re
import os

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre.strip()
        self.telefono = telefono.strip()
        self.correo = correo.strip()

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"

class GestionContactos:
    def __init__(self, archivo='contactos.txt'):
        self.contactos = []

        # Asegura que el archivo se guarde en el mismo directorio del script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.archivo = os.path.join(script_dir, archivo)

        self.cargar_contactos()

    def cargar_contactos(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        partes = linea.strip().split(',')
                        if len(partes) == 3:
                            nombre, telefono, correo = partes
                            self.contactos.append(Contacto(nombre, telefono, correo))
        except Exception as e:
            print(f"[Error al cargar contactos]: {e}")

    def guardar_contactos(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for contacto in self.contactos:
                    f.write(f"{contacto.nombre},{contacto.telefono},{contacto.correo}\n")
        except Exception as e:
            print(f"[Error al guardar contactos]: {e}")

    @staticmethod
    def validar_correo(correo):
        """Valida el formato del correo electrónico con una expresión regular."""
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo)

    def agregar_contacto(self, nombre, telefono, correo):
        if not nombre or not telefono or not correo:
            print("[Error]: Todos los campos son obligatorios.")
            return
        if not self.validar_correo(correo):
            print("[Error]: Formato de correo electrónico inválido.")
            return
        self.contactos.append(Contacto(nombre, telefono, correo))
        self.guardar_contactos()
        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos guardados.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        resultados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if resultados:
            for contacto in resultados:
                print(contacto)
        else:
            print("Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if encontrados:
            for c in encontrados:
                self.contactos.remove(c)
            self.guardar_contactos()
            print("Contacto eliminado.")
        else:
            print("No se encontró un contacto con ese nombre.")

# --- Menú principal ---
def menu():
    gestion = GestionContactos()
    while True:
        print("\n--- Menú de Gestión de Contactos ---")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo electrónico: ")
            gestion.agregar_contacto(nombre, telefono, correo)
        elif opcion == '2':
            gestion.mostrar_contactos()
        elif opcion == '3':
            nombre = input("Nombre a buscar: ")
            gestion.buscar_contacto(nombre)
        elif opcion == '4':
            nombre = input("Nombre a eliminar: ")
            gestion.eliminar_contacto(nombre)
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("[Error]: Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
# Este código implementa un sistema de gestión de contactos en Python.
# Permite agregar, mostrar, buscar y eliminar contactos.
# Los contactos se guardan en un archivo de texto y se cargan al iniciar el programa.
# Se valida el formato del correo electrónico al agregar un contacto.