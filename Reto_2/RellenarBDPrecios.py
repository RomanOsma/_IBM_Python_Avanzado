import mysql.connector
from mysql.connector import Error
import random
from faker import Faker
from datetime import datetime, timedelta

# Configuración de la base de datos (usa la misma que en tu proyecto)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aroman1984',
    'database': 'inventory_db'
}

fake = Faker('es_ES')  # Generar datos en español


def generate_price_history(product_name):
    """Genera un historial de precios falso para un producto."""
    price_history = []
    current_price = random.uniform(10, 3000)  # Precio inicial aleatorio

    # Generar 5-15 cambios de precio para el producto
    for _ in range(random.randint(5, 15)):
        # Variar el precio entre -50% y +50% del precio actual
        price_change = current_price * random.uniform(-0.5, 0.5)
        new_price = round(current_price + price_change, 2)
        new_price = max(new_price, 1)  # Asegurar precio mínimo de $1

        # Generar fecha aleatoria en los últimos 2 años
        change_date = fake.date_time_between(
            start_date='-2y',
            end_date='now'
        ).strftime('%Y-%m-%d %H:%M:%S')

        price_history.append((product_name, new_price, change_date))
        current_price = new_price

    return price_history


def fill_price_history(num_changes_per_product=10):
    """Llena la tabla price_history con cambios de precios falsos."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("¡Conexión exitosa a la base de datos!")

            cursor = connection.cursor()

            # Borrar datos existentes en price_history
            cursor.execute("TRUNCATE TABLE price_history;")

            # Obtener todos los productos
            cursor.execute("SELECT name FROM products;")
            products = [row[0] for row in cursor.fetchall()]

            # Insertar historial de precios para cada producto
            query = """INSERT INTO price_history 
                      (product_name, new_price, change_date)
                      VALUES (%s, %s, %s)"""

            total_changes = 0
            for product in products:
                changes = generate_price_history(product)
                cursor.executemany(query, changes)
                total_changes += len(changes)
                print(f"Generados {len(changes)} cambios para {product}")

            connection.commit()
            print(f"\n¡Historial de precios rellenado con {total_changes} cambios!")

    except Error as e:
        print(f"Error al rellenar el historial de precios: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")


if __name__ == "__main__":
    fill_price_history()