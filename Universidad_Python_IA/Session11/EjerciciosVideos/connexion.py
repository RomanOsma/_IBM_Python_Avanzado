from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    """
    Esta clase gestiona el pool de conexiones a la base de datos MySQL.
    Attributes:
        DATABASE (str): Nombre de la base de datos.
        USERNAME (str): Usuario MySQL.
        PASSWORD (str): Contraseña MySQL.
        DB_PORT (str): Puerto MySQL, por defecto 3306.
        HOST (str): Host donde se encuentra el servidor de base de datos.
        POOL_SIZE (int): Tamaño del pool de conexiones.
        POOL_NAME (str): Nombre del pool de conexiones.
    """
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'Aroman1984' # Credenciales base datos 2
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None
    @classmethod
    def obtener_pool(cls):
        """Retorna el pool de conexiones, creándolo si no existe."""
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
            except Error as e:
                print(f'Error al crear el pool de conexiones: {e}')
        return cls.pool
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')
