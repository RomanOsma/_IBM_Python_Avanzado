import os
import logging
from mysql.connector import Error, pooling
from dotenv import load_dotenv

# Configuración inicial
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

class Product:
    ALLOWED_CATEGORIES = ["Electrónica", "Muebles", "Alimentos", "Ropa"]

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
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME', 'inventory_db'),
            'pool_size': 5
        }

        missing_vars = [var for var in ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
                       if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Faltan variables de entorno: {', '.join(missing_vars)}")

        self.connection_pool = pooling.MySQLConnectionPool(**self.config)
        logging.info("Pool de conexiones inicializado correctamente")

    def get_connection(self):
        try:
            return self.connection_pool.get_connection()
        except Error as e:
            logging.error(f"Error obteniendo conexión: {e}")
            raise

    def _execute_query(self, query, params=None, commit=False):
        connection = None
        cursor = None
        try:
            connection = self.get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            if commit:
                connection.commit()
            return cursor.fetchall() if cursor.description else None
        except Error as e:
            if connection:
                connection.rollback()
            logging.error(f"Error de base de datos: {e}", exc_info=True)
            raise
        finally:
            if cursor:
                cursor.close()
            # No es necesario liberar la conexión manualmente en versiones modernas
            # La conexión se devuelve automáticamente al pool cuando se cierra
            if connection:
                connection.close()  # Esto devuelve la conexión al pool

    # MÉTODOS CRUD

    def add_product(self, product):
        self._validate_product(product)
        try:
            self._execute_query("""
                INSERT INTO products (name, quantity, price, category) 
                VALUES (%s, %s, %s, %s)
            """, (product.name, product.quantity, product.price, product.category), commit=True)
            logging.info(f"Producto añadido: {product}")
        except Error as e:
            if "Duplicate entry" in str(e):
                raise ValueError(f"Error: {product.name} ya existe en el inventario")
            raise

    def show_all_products(self):
        products = self._execute_query("SELECT * FROM products")
        self._display_products(products, "Lista completa de productos")

    def search_product(self, name):
        products = self._execute_query("SELECT * FROM products WHERE name = %s", (name,))
        if products:
            self._display_products(products, "Resultado de búsqueda")
            return products[0]
        print(f"No se encontró '{name}' en el inventario")
        return None

    def search_by_category(self, category):
        products = self._execute_query("SELECT * FROM products WHERE category = %s", (category,))
        if products:
            print(f"\nProductos en categoría '{category}':")
            self._display_products(products, show_ids=False)
        else:
            print(f"\nNo hay productos en la categoría '{category}'")

    def update_product(self, name, **kwargs):
        if not self.search_product(name):
            return

        updates = self._build_update_query(kwargs)
        if not updates:
            print("No se proporcionaron campos para actualizar")
            return

        query = f"UPDATE products SET {', '.join(updates)} WHERE name = %s"
        self._execute_query(query, (*kwargs.values(), name), commit=True)
        print(f"¡{name} actualizado exitosamente!")

    def delete_product(self, name):
        if not self.search_product(name):
            return

        self._execute_query("DELETE FROM products WHERE name = %s", (name,), commit=True)
        print(f"¡{name} eliminado exitosamente!")

    def low_stock_report(self, threshold=10):
        products = self._execute_query("SELECT * FROM products WHERE quantity < %s", (threshold,))
        if products:
            print(f"\n¡Alerta! Productos con stock bajo (< {threshold} unidades):")
            self._display_products(products, show_category=False)
            print(f"Total de productos con stock bajo: {len(products)}")
        else:
            print(f"\nNo hay productos con stock por debajo de {threshold} unidades")

    def search_by_price_range(self, min_price, max_price):
        products = self._execute_query("""
            SELECT * FROM products 
            WHERE price BETWEEN %s AND %s""", (min_price, max_price))
        self._display_products(products, "Resultados de búsqueda por rango de precio")

    # MÉTODOS AUXILIARES

    def _validate_product(self, product):
        errors = []
        if not product.name.strip():
            errors.append("El nombre no puede estar vacío")
        if product.quantity <= 0:
            errors.append("La cantidad debe ser mayor que 0")
        if product.price <= 0:
            errors.append("El precio debe ser mayor que 0")
        if errors:
            raise ValueError("\n".join(errors))

    def _display_products(self, products, title="Productos", show_ids=True, show_category=True):
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

    def _build_update_query(self, fields):
        valid_fields = ['quantity', 'price', 'category']
        return [f"{field} = %s" for field in valid_fields if field in fields]

def main_menu(inventory):
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
            _handle_search_product(inventory)
        elif choice == '4':
            _handle_search_by_category(inventory)
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
    try:
        name = input("Nombre del producto: ").strip()
        quantity = int(input("Cantidad: "))
        price = float(input("Precio: "))
        category = input("Categoría: ").strip()

        product = Product(name, quantity, price, category)
        inventory.add_product(product)
    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def _handle_search_product(inventory):
    name = input("Nombre del producto a buscar: ").strip()
    inventory.search_product(name)

def _handle_search_by_category(inventory):
    category = input("Categoría a buscar: ").strip()
    inventory.search_by_category(category)

def _handle_update_product(inventory):
    name = input("Nombre del producto a actualizar: ").strip()
    if not inventory.search_product(name):
        return

    updates = {}
    new_quantity = input("Nueva cantidad (dejar vacío para mantener): ").strip()
    if new_quantity:
        updates['quantity'] = int(new_quantity)
    new_price = input("Nuevo precio (dejar vacío para mantener): ").strip()
    if new_price:
        updates['price'] = float(new_price)
    new_category = input("Nueva categoría (dejar vacío para mantener): ").strip()
    if new_category:
        updates['category'] = new_category

    if updates:
        inventory.update_product(name, **updates)
    else:
        print("No se proporcionaron campos para actualizar")

def _handle_delete_product(inventory):
    name = input("Nombre del producto a eliminar: ").strip()
    if not inventory.search_product(name):
        return

    confirm = input(f"¿Está seguro de eliminar {name}? (s/n): ").lower()
    if confirm == 's':
        inventory.delete_product(name)
    else:
        print("Operación cancelada")

def _handle_low_stock_report(inventory):
    try:
        threshold = int(input("Umbral de stock bajo (unidades): "))
        inventory.low_stock_report(threshold)
    except ValueError:
        print("Error: Ingrese un número válido para el umbral")

if __name__ == "__main__":
    # Verificar variables de entorno
    required_vars = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        print(f"Error: Faltan variables de entorno: {', '.join(missing)}")
        print("Asegúrate de tener un archivo .env con:")
        print("DB_HOST=localhost")
        print("DB_USER=root")
        print("DB_PASSWORD=tu_contraseña")
        print("DB_NAME=inventory_db")
        exit(1)

    inventory_manager = InventoryManager()
    main_menu(inventory_manager)

    # --- SECCIÓN DE PRUEBAS ---
    print("\n=== Ejecutando pruebas automatizadas ===")
    print("\n--- Prueba de búsqueda por rango de precio ($500-$1500) ---")
    inventory_manager.search_by_price_range(500, 1500)
    print("\n--- Prueba de búsqueda por categoría (Electrónica) ---")
    inventory_manager.search_by_category("Electrónica")
    print("\n--- Prueba de informe de stock bajo (umbral 50) ---")
    inventory_manager.low_stock_report(50)
    print("\n--- Prueba de informe de stock bajo (umbral 10) ---")
    inventory_manager.low_stock_report(10)