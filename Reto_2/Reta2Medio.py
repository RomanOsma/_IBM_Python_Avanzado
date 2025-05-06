""""

pip install reportlab
pip install tkinter
necesario pip install faker
pip install python-dotenv


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

CREATE TABLE price_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    new_price DECIMAL(10,2),
    change_date DATETIME,
    FOREIGN KEY (product_name) REFERENCES products(name)
);

SISTEMA DE GESTIÓN DE INVENTARIO COMPLETO

Este programa implementa un sistema de gestión de inventario con las siguientes características:
- Conexión a base de datos MySQL
- Operaciones CRUD completas
- Búsquedas avanzadas (por nombre y categoría)
- Informes de stock bajo
- Manejo robusto de errores
- Interfaz de usuario interactiva
"""

import mysql.connector
from mysql.connector import Error


class Product:
    ALLOWED_CATEGORIES = ["Electrónica", "Muebles", "Alimentos", "Ropa"]
    """
    Clase modelo que representa un producto en el inventario.

    Atributos:
        name (str): Nombre único del producto (clave primaria)
        quantity (int): Cantidad disponible (debe ser > 0)
        price (float): Precio unitario (debe ser > 0)
        category (str): Categoría del producto
    """

    def __init__(self, name, quantity, price, category):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        if category not in self.ALLOWED_CATEGORIES:
            raise ValueError(f"Categoría no permitida. Valores válidos: {', '.join(self.ALLOWED_CATEGORIES)}")

    def __repr__(self):
        return (f"Producto(nombre={self.name!r}, cantidad={self.quantity}, "
                f"precio=${self.price:.2f}, categoría={self.category!r})")


class InventoryManager:
    """
    Controlador principal que gestiona todas las operaciones de inventario.

    Métodos principales:
    - add_product(): Añadir nuevo producto
    - show_all_products(): Mostrar todos los productos
    - search_product(): Búsqueda por nombre
    - search_by_category(): Búsqueda por categoría
    - update_product(): Actualizar producto existente
    - delete_product(): Eliminar producto
    - low_stock_report(): Informe de stock bajo
    """

    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.connection = None

    def connect(self):
        """Establece conexión con la base de datos MySQL."""
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

    # MÉTODOS CRUD

    def add_product(self, product):
        """Agrega un nuevo producto con validaciones completas."""
        self._validate_product(product)

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
            self._handle_db_error(e, product.name)
        finally:
            self._close_cursor(cursor)
            self.disconnect()

    def show_all_products(self):
        """Muestra todos los productos en formato tabular."""
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            self._display_products(products, "Lista completa de productos")

        except Error as e:
            print(f"Error al mostrar productos: {e}")
        finally:
            self._close_cursor(cursor)
            self.disconnect()

    # MÉTODOS DE BÚSQUEDA

    def search_product(self, name):
        """Búsqueda exacta por nombre con manejo de casos no encontrados."""
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM products WHERE name = %s"
            cursor.execute(query, (name,))
            product = cursor.fetchone()

            if product:
                self._display_products([product], "Resultado de búsqueda")
                return product
            else:
                print(f"No se encontró '{name}' en el inventario")

        except Error as e:
            print(f"Error al buscar producto: {e}")
        finally:
            self._close_cursor(cursor)
            self.disconnect()

    def search_by_category(self, category):
        """Búsqueda por categoría con formato de resultados especializado."""
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
            self._display_products(products, show_ids=False)

        except Error as e:
            print(f"Error en búsqueda por categoría: {e}")
        finally:
            self._close_cursor(cursor)
            self.disconnect()

    # MÉTODOS AVANZADOS

    def update_product(self, name, **kwargs):
        """Actualización parcial de producto con validación de campos."""
        try:
            self.connect()
            cursor = self.connection.cursor()

            if not self._product_exists(name):
                return

            updates = self._build_update_query(kwargs)
            if not updates:
                print("No se proporcionaron campos para actualizar")
                return

            query = f"UPDATE products SET {', '.join(updates)} WHERE name = %s"
            cursor.execute(query, (*kwargs.values(), name))
            self.connection.commit()
            print(f"¡{name} actualizado exitosamente!")

        except Error as e:
            print(f"Error al actualizar producto: {e}")
        finally:
            self._close_cursor(cursor)
            self.disconnect()

    def delete_product(self, name):
        """Elimina un producto del inventario con manejo mejorado de conexiones."""
        try:
            self.connect()
            with self.connection.cursor() as cursor:  # Usando context manager
                # Verificar existencia del producto
                cursor.execute("SELECT name FROM products WHERE name = %s", (name,))
                if not cursor.fetchone():
                    print(f"Error: {name} no existe en el inventario")
                    return

                # Ejecutar eliminación
                cursor.execute("DELETE FROM products WHERE name = %s", (name,))
                self.connection.commit()
                print(f"¡{name} eliminado exitosamente!")

        except Error as e:
            print(f"Error al eliminar producto: {e}")
            if 'connection' in locals() and self.connection.is_connected():
                self.connection.rollback()
        finally:
            self.disconnect()

    def low_stock_report(self, threshold=10):
        """Informe de stock bajo con formato especial y resumen."""
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
            self._display_products(low_stock, show_category=False)
            print(f"Total de productos con stock bajo: {len(low_stock)}")

        except Error as e:
            print(f"Error en informe de stock bajo: {e}")
        finally:
            self._close_cursor(cursor)
            self.disconnect()

    # Implementar búsqueda por rango de precios
    def search_by_price_range(self, min_price, max_price):
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            query = """SELECT * FROM products 
                      WHERE price BETWEEN %s AND %s"""
            cursor.execute(query, (min_price, max_price))
            products = cursor.fetchall()

            self._display_products(products, "Resultados de búsqueda por rango de precio")

        except Error as e:
            print(f"Error en búsqueda por rango de precio: {e}")
        finally:
            self._close_cursor(cursor)
            self.disconnect()



    def add_price_history(self, product_name, new_price):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = """INSERT INTO price_history 
                      (product_name, new_price, change_date)
                      VALUES (%s, %s, NOW())"""
            cursor.execute(query, (product_name, new_price))
            self.connection.commit()
        except Error as e:
            print(f"Error en historial de precios: {e}")
        finally:
            self._close_cursor(cursor)
            self.disconnect()

    # En tu InventoryManager, agrega esta función
    def get_paginated_products(self, page=1, per_page=10):
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            offset = (page - 1) * per_page
            query = f"SELECT * FROM products LIMIT {per_page} OFFSET {offset}"
            cursor.execute(query)
            products = cursor.fetchall()
            return products
        except Error as e:
            print(f"Error: {e}")
        finally:
            self._close_cursor(cursor)
            self.disconnect()

    # MÉTODOS AUXILIARES

    def _validate_product(self, product):
        """Valida todos los campos del producto antes de guardar."""
        errors = []
        if not product.name.strip():
            errors.append("El nombre no puede estar vacío")
        if product.quantity <= 0:
            errors.append("La cantidad debe ser mayor que 0")
        if product.price <= 0:
            errors.append("El precio debe ser mayor que 0")

        if errors:
            raise ValueError("\n".join(errors))

    def _product_exists(self, name):
        """Verifica si un producto existe en la base de datos."""
        if self.search_product(name):
            return True
        print(f"Error: {name} no existe en el inventario")
        return False

    def _build_update_query(self, fields):
        """Construye dinámicamente la consulta UPDATE."""
        valid_fields = ['quantity', 'price', 'category']
        updates = []
        for field in valid_fields:
            if field in fields:
                updates.append(f"{field} = %s")
        return updates

    def _display_products(self, products, title="Productos", show_ids=True, show_category=True):
        """Formatea y muestra productos en formato tabular."""
        if not products:
            print("No hay productos para mostrar")
            return

        print(f"\n{title}:")
        print("-" * (50 if show_category else 40))
        for p in products:
            line = f"ID: {p['id']:2} | {p['name']:15}" if show_ids else ""
            line += f" | Cantidad: {p['quantity']:3}" if show_ids else ""
            line += f" | Precio: ${p['price']:6.2f}"
            if show_category:
                line += f" | Categoría: {p['category']:10}"
            print(line)
        print("-" * (50 if show_category else 40))

    def _handle_db_error(self, error, product_name):
        """Manejo común de errores de base de datos."""
        if "Duplicate entry" in str(error):
            print(f"Error: {product_name} ya existe en el inventario")
        else:
            print(f"Error de base de datos: {error}")

    def _close_cursor(self, cursor):
        """Cierra un cursor de forma segura."""
        if cursor:
            cursor.close()


def main_menu(inventory):
    """Interfaz de usuario interactiva con menú principal."""
    while True:
        print("\nSISTEMA DE GESTIÓN DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto por nombre")
        print("4. Buscar producto por categoría")
        print("5. Actualizar producto")
        print("6. Eliminar producto")
        print("7. Reporte de stock bajo")
        print("8. Salir")

        choice = input("Seleccione una opción: ").strip()

        if choice == '1':
            _handle_add_product(inventory)

        elif choice == '2':
            inventory.show_all_products()

        elif choice == '3':
            name = input("Nombre del producto a buscar: ").strip()
            inventory.search_product(name)

        elif choice == '4':
            category = input("Categoría a buscar: ").strip()
            inventory.search_by_category(category)

        elif choice == '5':
            _handle_update_product(inventory)

        elif choice == '6':
            _handle_delete_product(inventory)

        elif choice == '7':
            _handle_low_stock_report(inventory)

        elif choice == '8':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


def _handle_add_product(inventory):
    """Controlador para añadir producto con validaciones adicionales."""
    try:
        name = input("Nombre del producto: ").strip()
        quantity = int(input("Cantidad: "))
        price = float(input("Precio: "))
        category = input("Categoría: ").strip()

        product = Product(name, quantity, price, category)
        inventory.add_product(product)

    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except Error as e:
        print(f"Error inesperado: {e}")


def _handle_update_product(inventory):
    """Controlador para actualizar producto con manejo de campos vacíos."""
    name = input("Nombre del producto a actualizar: ").strip()

    if not inventory._product_exists(name):
        return

    print("\nDeje vacío los campos que no desea modificar")
    new_quantity = input("Nueva cantidad: ").strip()
    new_price = input("Nuevo precio: ").strip()
    new_category = input("Nueva categoría: ").strip()

    updates = {}
    if new_quantity:
        updates['quantity'] = int(new_quantity)
    if new_price:
        updates['price'] = float(new_price)
    if new_category:
        updates['category'] = new_category

    inventory.update_product(name, **updates)


def _handle_delete_product(inventory):
    """Controlador para eliminar producto con manejo mejorado de confirmación."""
    name = input("Nombre del producto a eliminar: ").strip()

    # Verificar existencia antes de confirmar
    if not inventory.search_product(name):
        return

    confirm = input(f"¿Está seguro de eliminar {name}? (s/n): ").lower()
    if confirm == 's':
        inventory.delete_product(name)
    else:
        print("Operación cancelada")


def _handle_low_stock_report(inventory):
    """Controlador para informe de stock bajo con entrada validada."""
    try:
        threshold = int(input("Umbral de stock bajo (unidades): "))
        inventory.low_stock_report(threshold)
    except ValueError:
        print("Error: Ingrese un número válido para el umbral")


if __name__ == "__main__":
    # Configuración de la base de datos
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Aroman1984',
        'database': 'inventory_db'
    }

    # Crear instancia del gestor de inventario
    inventory_manager = InventoryManager(**DB_CONFIG)

    # Iniciar menú principal
    main_menu(inventory_manager)

    # --- SECCIÓN DE PRUEBAS ---
    print("\n=== Ejecutando pruebas automatizadas ===")

    # Prueba de filtros de precio
    print("\n--- Prueba de búsqueda por rango de precio ($500-$1500) ---")
    inventory_manager.search_by_price_range(500, 600)

    print("\n--- Prueba de búsqueda por categoría (Electrónica) ---")
    inventory_manager.search_by_category("Electrónica")

    # Prueba de informes de stock bajo
    print("\n--- Prueba de informe de stock bajo (umbral 50) ---")
    inventory_manager.low_stock_report(20
                                       )
    print("\n--- Prueba de informe de stock bajo (umbral 10) ---")
    inventory_manager.low_stock_report(10)