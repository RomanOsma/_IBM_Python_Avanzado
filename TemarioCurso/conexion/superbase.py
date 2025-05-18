# Operaciones básicas con Supabase PostgreSQL
import psycopg2
from psycopg2 import sql

# Configuración de conexión
CONEXION = "postgresql://postgres.kvfdzkuqwcsvqvjquvbk:12345678910111213141516171819@aws-0-eu-west-2.pooler.supabase.com:6543/postgres"


def conectar_base_datos():
    """Establecer conexión con la base de datos"""
    try:
        return psycopg2.connect(CONEXION)
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def listar_usuarios():
    """Listar todos los usuarios de la tabla usuarios"""
    conexion = conectar_base_datos()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()

        print("\n=== Usuarios ===")
        if not usuarios:
            print("No hay usuarios en la tabla.")
        else:
            # Obtener nombres de columnas
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'usuarios'")
            columnas = [col[0] for col in cursor.fetchall()]

            # Imprimir encabezados
            print(" | ".join(columnas))
            print("-" * 50)

            # Imprimir datos
            for usuario in usuarios:
                print(" | ".join(str(campo) for campo in usuario))

        cursor.close()
    except psycopg2.Error as e:
        print(f"Error al listar usuarios: {e}")
    finally:
        if conexion:
            conexion.close()


def agregar_usuario(nombre, email):
    """Agregar un nuevo usuario a la tabla usuarios"""
    conexion = conectar_base_datos()
    if not conexion:
        return False

    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)",
            (nombre, email)
        )
        conexion.commit()
        print(f"\n✅ Usuario {nombre} agregado exitosamente.")
        return True
    except psycopg2.Error as e:
        conexion.rollback()
        print(f"Error al agregar usuario: {e}")
        return False
    finally:
        if conexion:
            cursor.close()
            conexion.close()


def buscar_usuario_por_nombre(nombre):
    """Buscar usuario por nombre"""
    conexion = conectar_base_datos()
    if not conexion:
        return None

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE %s", (f'%{nombre}%',))
        resultados = cursor.fetchall()

        print(f"\n=== Resultados para búsqueda de '{nombre}' ===")
        if not resultados:
            print("No se encontraron usuarios.")
        else:
            # Obtener nombres de columnas
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'usuarios'")
            columnas = [col[0] for col in cursor.fetchall()]

            # Imprimir encabezados
            print(" | ".join(columnas))
            print("-" * 50)

            # Imprimir datos
            for usuario in resultados:
                print(" | ".join(str(campo) for campo in usuario))

        return resultados
    except psycopg2.Error as e:
        print(f"Error al buscar usuario: {e}")
        return None
    finally:
        if conexion:
            cursor.close()
            conexion.close()


def main():
    """Menú principal de operaciones"""
    while True:
        print("\n=== Menú de Operaciones con Base de Datos ===")
        print("1. Listar Usuarios")
        print("2. Agregar Usuario")
        print("3. Buscar Usuario")
        print("4. Salir")

        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == '1':
            listar_usuarios()
        elif opcion == '2':
            nombre = input("Ingrese el nombre del usuario: ")
            email = input("Ingrese el email del usuario: ")
            agregar_usuario(nombre, email)
        elif opcion == '3':
            nombre = input("Ingrese el nombre a buscar: ")
            buscar_usuario_por_nombre(nombre)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecución del script
if __name__ == "__main__":
    main()