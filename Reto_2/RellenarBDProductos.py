import mysql.connector
from mysql.connector import Error
import random
from faker import Faker

# Configuración de la base de datos (usa la misma que en tu proyecto)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aroman1984',
    'database': 'inventory_db'
}

fake = Faker('es_ES')  # Generar datos en español

CATEGORIES = ["Electrónica", "Muebles", "Alimentos", "Ropa",
              "Juguetes", "Deportes", "Libros", "Belleza"]

BRANDS = ["TechPro", "ComfortHome", "FreshFoods", "StyleWear",
          "FunToys", "ProSport", "BookHaven", "GlamBeauty"]


def generate_fake_product(existing_names):
    """Genera un producto falso con nombre único."""
    category = random.choice(CATEGORIES)
    price = round(random.uniform(9.99, 2999.99), 2)
    quantity = random.randint(1, 500)

    # Generar nombre único
    base_name = fake.word().capitalize()
    brand = random.choice(BRANDS)
    product_name = f"{base_name} {brand} {category}"

    # Asegurar unicidad del nombre
    counter = 1
    while product_name in existing_names:
        product_name = f"{base_name} {counter} {brand} {category}"
        counter += 1

    existing_names.add(product_name)
    return (product_name, quantity, price, category)


def fill_database(num_products=10000):
    """Llena la base de datos con productos falsos."""
    existing_names = set()  # Para rastrear nombres existentes
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("¡Conexión exitosa a la base de datos!")

            cursor = connection.cursor()

            # Borrar datos de forma segura
            cursor.execute("DELETE FROM price_history;")
            cursor.execute("DELETE FROM products;")
            connection.commit()

            # Insertar productos falsos
            query = """INSERT INTO products 
                      (name, quantity, price, category) 
                      VALUES (%s, %s, %s, %s)"""

            products = []
            for _ in range(num_products):
                product = generate_fake_product(existing_names)
                products.append(product)

                # Insertar en lotes de 1000 para mejorar rendimiento
                if len(products) % 1000 == 0:
                    cursor.executemany(query, products)
                    connection.commit()
                    products = []
                    print(f"Insertados {len(products)} productos de {num_products}")

            # Insertar el último lote
            if products:
                cursor.executemany(query, products)
                connection.commit()

            print(f"\n¡Base de datos rellenada con {num_products} productos!")

    except Error as e:
        print(f"Error al rellenar la base de datos: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    fill_database(500)  # Cambia este número para insertar más/menos productos