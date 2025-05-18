# Versión compatible con Python 3.13
import sys
import platform

# Verificar la versión de Python
print(f"Versión de Python: {platform.python_version()}")

# Instalación de dependencias
print("\nAsegúrate de tener instaladas las siguientes dependencias:")
print("pip install psycopg2-binary")

# Importaciones con manejo de compatibilidad
try:
    import psycopg2
    from urllib.parse import urlparse
except ImportError as e:
    print(f"Error de importación: {e}")
    print("Instala las dependencias necesarias con:")
    print("pip install psycopg2-binary")
    sys.exit(1)

# Configuración de conexión
CONEXIONES = {
    "direct": "postgresql://postgres:12345678910111213141516171819@db.kvfdzkuqwcsvqvjquvbk.supabase.co:5432/postgres",
    "transaction": "postgresql://postgres.kvfdzkuqwcsvqvjquvbk:12345678910111213141516171819@aws-0-eu-west-2.pooler.supabase.com:6543/postgres",
    "session": "postgresql://postgres.kvfdzkuqwcsvqvjquvbk:12345678910111213141516171819@aws-0-eu-west-2.pooler.supabase.com:5432/postgres"
}


def conectar_supabase(tipo_conexion="direct"):
    """
    Conectar a Supabase con manejo de errores detallado
    """
    # Seleccionar URL de conexión
    url = CONEXIONES.get(tipo_conexion)
    if not url:
        print(f"Tipo de conexión inválido: {tipo_conexion}")
        print("Tipos válidos:", ", ".join(CONEXIONES.keys()))
        return None

    try:
        # Parsear la URL de conexión
        parsed_url = urlparse(url)

        # Parámetros de conexión
        params = {
            "database": parsed_url.path[1:],  # Quitar el '/' inicial
            "user": parsed_url.username,
            "password": parsed_url.password,
            "host": parsed_url.hostname,
            "port": parsed_url.port
        }

        # Establecer la conexión con información de depuración
        print("\nIntentando conectar...")
        print(f"Host: {params['host']}")
        print(f"Puerto: {params['port']}")
        print(f"Base de datos: {params['database']}")
        print(f"Usuario: {params['user']}")

        # Conexión
        conexion = psycopg2.connect(**params)

        # Crear cursor
        cursor = conexion.cursor()

        # Consultas de prueba
        print("\nConsultas de prueba:")

        # Versión de PostgreSQL
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print("Versión de PostgreSQL:", version[0])

        # Listar tablas
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)
        tablas = cursor.fetchall()

        print("\nTablas en la base de datos:")
        if tablas:
            for tabla in tablas:
                print(tabla[0])
        else:
            print("No se encontraron tablas en el esquema público.")

        # Cerrar cursor y conexión
        cursor.close()
        conexion.close()

        return True

    except psycopg2.Error as e:
        print("\n=== Error de Conexión de PostgreSQL ===")
        print(f"Código de error: {e.pgcode}")
        print(f"Mensaje de error: {e}")

        # Diagnóstico de errores comunes
        if "connection refused" in str(e).lower():
            print("\nPosibles causas:")
            print("1. Firewall bloqueando la conexión")
            print("2. Servicio de base de datos no iniciado")
            print("3. Puerto incorrecto")

        return False

    except Exception as e:
        print("\n=== Error Inesperado ===")
        print(f"Tipo de error: {type(e)}")
        print(f"Mensaje de error: {e}")

        return False


# Función principal
def main():
    print("=== Prueba de Conexión a Supabase ===")

    # Intentar conexiones alternativas
    tipos_conexion = ["transaction", "session", "direct"]

    for tipo in tipos_conexion:
        print(f"\nProbando conexión: {tipo}")
        exito = conectar_supabase(tipo)

        if exito:
            print(f"\n✅ Conexión {tipo} exitosa!")
            break
        else:
            print(f"❌ Conexión {tipo} fallida.")

    print("\nFin del diagnóstico.")


# Ejecutar script
if __name__ == "__main__":
    main()