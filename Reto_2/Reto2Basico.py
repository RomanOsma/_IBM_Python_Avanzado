""""
Crear la base de datos
CREATE DATABASE inventory_db;
USE inventory_db;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(255)
);

"""


import mysql.connector
from mysql.connector import Error


class Product:
    """
    Representa un producto con atributos: nombre, cantidad, precio y categoría.

    Atributos:
        name (str): Nombre único del producto
        quantity (int): Cantidad disponible en inventario
        price (float): Precio unitario del producto
        category (str): Categoría a la que pertenece
    """

    def __init__(self, name, quantity, price, category):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def __repr__(self):
        return (f"Producto(nombre={self.name}, cantidad={self.quantity}, "
                f"precio=${self.price:.2f}, categoría={self.category})")


class InventoryManager:
    """
    Gestiona operaciones de inventario e interactúa con la base de datos MySQL.

    Implementa:
    - Conexión segura a la base de datos
    - Operaciones CRUD (Crear, Leer, Actualizar, Borrar)
    - Manejo robusto de errores
    """

    def __init__(self, host, user, password, database):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Aroman1984',
            'database': 'inventory_db'
        }
        self.connection = None

    def connect(self):
        """Establece conexión con la base de datos."""
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print("¡Conexión exitosa a la base de datos!")
        except Error as e:
            print(f"Error de conexión: {e}")
            raise

    def disconnect(self):
        """Cierra la conexión con la base de datos."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def add_product(self, product):
        """Agrega un nuevo producto al inventario."""
        if product.quantity <= 0:
            print("Error: La cantidad debe ser mayor que 0")
            return
        if product.price <= 0:
            print("Error: El precio debe ser mayor que 0")
            return
        if not product.name.strip():
            print("Error: El nombre no puede estar vacío")
            return
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = """INSERT INTO products 
                      (name, quantity, price, category) 
                      VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (product.name, product.quantity,
                                   product.price, product.category))
            self.connection.commit()
            print(f"¡{product} añadido exitosamente!")
        except Error as e:
            if "Duplicate entry" in str(e):
                print(f"Error: {product.name} ya existe en el inventario")
            else:
                print(f"Error al añadir producto: {e}")
        finally:
            if cursor: cursor.close()
            self.disconnect()

    def show_all_products(self):
        """Muestra todos los productos en el inventario."""
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            if not products:
                print("No hay productos en el inventario")
                return

            print("\nLista de productos:")
            print("-" * 50)
            for p in products:
                print(f"ID: {p['id']:2} | {p['name']:15} | "
                      f"Cantidad: {p['quantity']:3} | "
                      f"Precio: ${p['price']:6.2f} | "
                      f"Categoría: {p['category']:10}")
            print("-" * 50)

        except Error as e:
            print(f"Error al mostrar productos: {e}")
        finally:
            if cursor: cursor.close()
            self.disconnect()

    def search_product(self, name):
        """Busca un producto por nombre."""
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM products WHERE name = %s"
            cursor.execute(query, (name,))
            product = cursor.fetchone()

            if product:
                print(f"\nProducto encontrado:")
                print(f"ID: {product['id']} | Nombre: {product['name']} | "
                      f"Cantidad: {product['quantity']} | Precio: ${product['price']} | "
                      f"Categoría: {product['category']}")
                return product
            else:
                print(f"No se encontró '{name}' en el inventario")

        except Error as e:
            print(f"Error al buscar producto: {e}")
        finally:
            if cursor: cursor.close()
            self.disconnect()

    def search_by_category(self, category):
        """Busca y muestra productos por categoría específica."""
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM products WHERE category = %s"
            cursor.execute(query, (category,))
            products = cursor.fetchall()

            if not products:
                print(f"\nNo hay productos en la categoría '{category}'")
                return

            print(f"\nProductos en categoría '{category}':")
            print("-" * 60)
            for p in products:
                print(f"ID: {p['id']:2} | {p['name']:20} | "
                      f"Cantidad: {p['quantity']:3} | "
                      f"Precio: ${p['price']:6.2f}")
            print("-" * 60)

        except Error as e:
            print(f"Error en búsqueda por categoría: {e}")
        finally:
            if cursor: cursor.close()
            self.disconnect()

    def update_product(self, name, **kwargs):
        """Actualiza información de un producto existente."""
        try:
            self.connect()
            cursor = self.connection.cursor()

            # Verificar existencia del producto
            if not self.search_product(name):
                print(f"Error: {name} no existe en el inventario")
                return

            # Construir consulta de actualización
            updates = []
            params = []
            for key, value in kwargs.items():
                if value is not None:
                    updates.append(f"{key} = %s")
                    params.append(value)
            params.append(name)  # Añadir nombre para cláusula WHERE

            if not updates:
                print("No se proporcionaron campos para actualizar")
                return

            query = f"UPDATE products SET {', '.join(updates)} WHERE name = %s"
            cursor.execute(query, params)
            self.connection.commit()
            print(f"¡{name} actualizado exitosamente!")

        except Error as e:
            print(f"Error al actualizar producto: {e}")
        finally:
            if cursor: cursor.close()
            self.disconnect()

    def delete_product(self, name):
        """Elimina un producto del inventario."""
        try:
            self.connect()
            cursor = self.connection.cursor()

            # Verificar existencia del producto
            if not self.search_product(name):
                print(f"Error: {name} no existe en el inventario")
                return

            query = "DELETE FROM products WHERE name = %s"
            cursor.execute(query, (name,))
            self.connection.commit()
            print(f"¡{name} eliminado exitosamente!")

        except Error as e:
            print(f"Error al eliminar producto: {e}")
        finally:
            if cursor: cursor.close()
            self.disconnect()

    def low_stock_report(self, threshold=10):
        """Genera un informe de productos con stock por debajo del umbral especificado."""
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM products WHERE quantity < %s"
            cursor.execute(query, (threshold,))
            low_stock = cursor.fetchall()

            if not low_stock:
                print(f"\nNo hay productos con stock por debajo de {threshold} unidades")
                return

            print(f"\n¡Alerta! Productos con stock bajo (< {threshold} unidades):")
            print("-" * 70)
            for p in low_stock:
                print(f"ID: {p['id']:2} | {p['name']:25} | "
                      f"Stock actual: {p['quantity']:2} | "
                      f"Categoría: {p['category']:10}")
            print("-" * 70)
            print(f"Total de productos con stock bajo: {len(low_stock)}")

        except Error as e:
            print(f"Error en informe de stock bajo: {e}")
        finally:
            if cursor: cursor.close()
            self.disconnect()

def main_menu(inventory):
    """Interfaz de usuario interactiva."""
    while True:
        print("\nSISTEMA DE GESTIÓN DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto")
        print("4. Buscar producto")
        print("5. Actualizar producto")
        print("7. Reporte stock bajo (unidades): ")
        print("8. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            name = input("Nombre del producto: ").strip()
            quantity = int(input("Cantidad: "))
            price = float(input("Precio: "))
            category = input("Categoría: ").strip()
            product = Product(name, quantity, price, category)
            inventory.add_product(product)

        elif choice == '2':
            inventory.show_all_products()

        elif choice == '3':
            name = input("Nombre del producto a buscar: ").strip()
            inventory.search_product(name)

        elif choice == '4':
            category = input("Categoría a buscar: ").strip()
            inventory.search_by_category(category)

        elif choice == '5':
            name = input("Nombre del producto a actualizar: ").strip()
            print("\nDeje vacío los campos que no desea modificar")
            new_quantity = input("Nueva cantidad: ")
            new_price = input("Nuevo precio: ")
            new_category = input("Nueva categoría: ").strip()

            updates = {}
            if new_quantity:
                updates['quantity'] = int(new_quantity)
            if new_price:
                updates['price'] = float(new_price)
            if new_category:
                updates['category'] = new_category

            inventory.update_product(name, **updates)

        elif choice == '6':
            name = input("Nombre del producto a eliminar: ").strip()
            inventory.delete_product(name)

            # Ejemplo de uso en el menú principal:
        elif choice == '7':
            try:
                threshold = int(input("Umbral de stock bajo (unidades): "))
                inventory.low_stock_report(threshold)
            except ValueError:
                print("Error: Ingrese un número válido para el umbral")

        elif choice == '8':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    # Configuración de la base de datos
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',  # Cambiar por su usuario MySQL
        'password': 'password',  # Cambiar por su contraseña
        'database': 'inventory_db'
    }

    # Crear instancia del gestor de inventario
    inventory_manager = InventoryManager(**DB_CONFIG)

    # Iniciar menú principal
    main_menu(inventory_manager)

    # Crear productos de ejemplo
    p1 = Product("Laptop Gamer", 10, 1299.99, "Electrónica")
    p2 = Product("Silla Gaming", 25, 299.99, "Muebles")

    # Añadir productos al inventario
    inventory_manager.add_product(p1)
    inventory_manager.add_product(p2)

    # Actualizar precio de un producto
    inventory_manager.update_product("Laptop Gamer", price=1399.99)

    # Mostrar todos los productos
    inventory_manager.show_all_products()

"""
Documentación y Mejoras Adicionales

1. Estructura del Código
Se utiliza la arquitectura MVC (Modelo-Vista-Controlador) simplificada:
Product: Clase modelo que representa los datos
InventoryManager: Controlador que gestiona la lógica de negocio
main_menu(): Vista que maneja la interfaz de usuario

2. Manejo de Errores
Se capturan excepciones específicas de MySQL (Error, IntegrityError)
Se implementa manejo de errores para:
Conexión a la base de datos
Duplicados en nombres de productos
Operaciones en productos inexistentes
Entradas de usuario incorrectas
"""