"""

Python y MySQL: Guía Completa - Versión Unificada

Este archivo combina todo el material de los cursos de Python con MySQL, incluyendo:

1. Operaciones CRUD básicas y avanzadas

2. Pool de conexiones para mejor rendimiento

3. Implementación del patrón DAO (Data Access Object)

4. Aplicación completa de gestión de clientes (Zona Fit)

5. Ejemplos de transacciones y procedimientos almacenados

Contiene todas las variantes de implementación, explicaciones didácticas y ejercicios

de ambas versiones del curso, eliminando solo duplicados exactos.

Autor: Angel Roman Osma (versión unificada)

Fecha: 21/04/2025

Versión: 2.0

"""

from typing import List, Tuple

import mysql.connector
from mysql.connector import pooling, Error
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

######################################################################

# PARTE 1: FUNDAMENTOS MySQL #

######################################################################

"""

FUNDAMENTOS DE MYSQL

MySQL es un sistema de gestión de bases de datos relacional ampliamente utilizado.

Antes de iniciar con Python, es importante comprender las operaciones CRUD básicas en SQL:

- CREATE: Crear tablas y bases de datos

- READ: Leer o consultar datos (SELECT)

- UPDATE: Actualizar o modificar datos existentes

- DELETE: Eliminar registros

Configuración inicial de las bases de datos:

"""

# Script SQL para crear las bases de datos y tablas necesarias

"""

-- Base de datos para ejemplos básicos

CREATE DATABASE IF NOT EXISTS personas_db;

USE personas_db;

CREATE TABLE IF NOT EXISTS personas (

id INT AUTO_INCREMENT PRIMARY KEY,

nombre VARCHAR(50) NOT NULL,

apellido VARCHAR(50) NOT NULL,

edad INT

);

-- Base de datos para la aplicación Zona Fit

CREATE DATABASE IF NOT EXISTS zona_fit_db;

USE zona_fit_db;

CREATE TABLE IF NOT EXISTS cliente (

id INT AUTO_INCREMENT PRIMARY KEY,

nombre VARCHAR(50) NOT NULL,

apellido VARCHAR(50) NOT NULL,

membresia VARCHAR(20) NOT NULL

);

"""

######################################################################

# PARTE 2: CONEXIÓN PYTHON-MYSQL #

######################################################################

"""

CONEXIÓN BÁSICA A MYSQL DESDE PYTHON

Para conectar Python con MySQL, utilizamos el conector oficial 'mysql-connector-python'.

Este conector proporciona una API para interactuar con bases de datos MySQL.

Instalación:

pip install mysql-connector-python

o

python -m pip install mysql-connector-python

"""

# Variante 1: Conexión básica directa

def ejemplo_conexion_basica():

    """

    Ejemplo básico de conexión a MySQL y consulta SELECT.

    Muestra:

    - Cómo establecer una conexión básica

    - Cómo ejecutar una consulta SELECT

    - Cómo recuperar y mostrar resultados

    Credenciales usadas:

    - Usuario: root

    - Contraseña: Aroman1984

    - Base de datos: zona_fit_db

    """

    try:

        # Establecer conexión

        conexion = mysql.connector.connect(

            host='localhost',

            user='root',

            password='Aroman1984',

            database='zona_fit_db'

        )

        # Crear cursor y ejecutar consulta

        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM cliente')

        # Recuperar y mostrar resultados

        resultados = cursor.fetchall()

        print("\nResultados de la consulta:")

        for fila in resultados:

            print(fila)

    except Error as e:

        print(f"Error al conectar a MySQL: {e}")

    finally:

        # Cerrar cursor y conexión

        if 'conexion' in locals() and conexion.is_connected():

            cursor.close()

            conexion.close()

            print("\nConexión cerrada.")

# Variante 2: Función genérica para crear conexiones

def crear_conexion(host='localhost', user='root', password='Aroman1984',

                    database='zona_fit_db') -> PooledMySQLConnection | MySQLConnectionAbstract:

    """

    Crea y devuelve una conexión a la base de datos MySQL.

    Args:

        host (str): Dirección del servidor MySQL (por defecto: 'localhost')

        user (str): Nombre de usuario (por defecto: 'root')

        password (str): Contraseña (por defecto: 'Aroman1984')

        database (str): Nombre de la base de datos (por defecto: 'personas_db')

    Returns:

        MySQLConnection: Objeto de conexión a la base de datos

    Raises:

        Error: Si ocurre un error en la conexión

    """

    try:

        conexion = mysql.connector.connect(

            host='localhost',

            user='root',

            password='Aroman1984',

            database='personas_db'

        )

        print(f"Conexión exitosa a la base de datos {database}")

        return conexion

    except Error as e:

        print(f"Error al conectar a MySQL: {e}")

        raise

def cerrar_conexion(conexion):

    """

    Cierra una conexión a la base de datos MySQL.

    Args:

        conexion (MySQLConnection): Conexión a cerrar

    """

    if conexion and conexion.is_connected():

        conexion.close()

        print("Conexión cerrada")

######################################################################

# PARTE 3: OPERACIONES CRUD EN PYTHON #

######################################################################

"""

OPERACIONES CRUD DESDE PYTHON

Una vez establecida la conexión, podemos realizar operaciones CRUD.

A continuación, se muestran ejemplos de estas operaciones con diferentes niveles de complejidad.

"""

# ------------------------- Versión Básica ---------------------------

def ejemplo_insertar():

    """

    Ejemplo de inserción de datos con parámetros en la base de datos 'personas_db'.

    Muestra:

    - Uso de parámetros en consultas SQL

    - Uso de commit() para confirmar cambios

    - Manejo seguro de valores en consultas

    """

    try:

        conexion = mysql.connector.connect(

            host='localhost',

            user='root',

            password='Aroman1984',

            database='personas_db'

        )

        cursor = conexion.cursor()

        # Consulta con parámetros (%s como marcadores)

        sql = "INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)"

        valores = ('Juan', 'Pérez', 30)

        cursor.execute(sql, valores)

        conexion.commit()  # Importante para confirmar cambios

        print(f"\nRegistro insertado: {valores}")

        print(f"ID generado: {cursor.lastrowid}")

    except Error as e:

        print(f"Error al insertar: {e}")

    finally:

        if 'conexion' in locals() and conexion.is_connected():

            cursor.close()

            conexion.close()

def ejemplo_actualizar():

    """

    Ejemplo de actualización de registros en la base de datos 'personas_db'.

    Muestra:

    - Uso de WHERE para seleccionar registros específicos

    - Uso de parámetros en cláusulas UPDATE

    - Verificación del número de filas afectadas

    """

    try:

        conexion = mysql.connector.connect(

            host='localhost',

            user='root',

            password='Aroman1984',

            database='personas_db'

        )

        cursor = conexion.cursor()

        sql = "UPDATE personas SET edad = %s WHERE nombre = %s"

        valores = (35, 'Juan')

        cursor.execute(sql, valores)

        conexion.commit()

        # Verificar cuántas filas fueron afectadas

        filas_afectadas = cursor.rowcount

        print(f"\nRegistros actualizados: {filas_afectadas}")

    except Error as e:

        print(f"Error al actualizar: {e}")

    finally:

        if 'conexion' in locals() and conexion.is_connected():

            cursor.close()

            conexion.close()

def ejemplo_eliminar():

    """

    Ejemplo de eliminación de registros en la base de datos 'personas_db'.

    Muestra:

    - Uso de DELETE con condiciones

    - Manejo seguro de operaciones de eliminación

    - Verificación de filas afectadas

    """

    try:

        conexion = mysql.connector.connect(

            host='localhost',

            user='root',

            password='Aroman1984',

            database='personas_db'

        )

        cursor = conexion.cursor()

        sql = "DELETE FROM personas WHERE nombre = %s AND apellido = %s"

        valores = ('Juan', 'Pérez')

        cursor.execute(sql, valores)

        conexion.commit()

        filas_afectadas = cursor.rowcount

        print(f"\nRegistros eliminados: {filas_afectadas}")

    except Error as e:

        print(f"Error al eliminar: {e}")

    finally:

        if 'conexion' in locals() and conexion.is_connected():

            cursor.close()

            conexion.close()

# ------------------------- Versión Avanzada ---------------------------

def select_personas(conexion=None, close_conn=True) -> List[Tuple]:

    """

    Ejecuta una consulta SELECT para obtener todas las personas.

    Args:

        conexion (MySQLConnection, optional): Conexión a la base de datos.

            Si es None, se crea una nueva.

        close_conn (bool): Indica si se debe cerrar la conexión al finalizar.

    Returns:

        List[Tuple]: Lista de tuplas con los datos de las personas

    """

    conn_propia = False

    if conexion is None:

        conexion = crear_conexion()

        conn_propia = True

    try:

        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM personas')

        resultados = cursor.fetchall()

        # Mostrar resultados

        print("\n--- Personas en la base de datos ---")

        for persona in resultados:

            print(f"ID: {persona[0]}, Nombre: {persona[1]}, Apellido: {persona[2]}, Edad: {persona[3]}")

        return resultados

    except Error as e:

        print(f"Error al ejecutar SELECT: {e}")

        return []

    finally:

        if 'cursor' in locals() and close_conn and conn_propia:

            cursor.close()

            cerrar_conexion(conexion)

######################################################################

# PARTE 4: POOL DE CONEXIONES #

######################################################################

"""

POOL DE CONEXIONES

Un pool de conexiones es una técnica que permite mantener un conjunto de conexiones a la base de datos abiertas

y listas para ser utilizadas, en lugar de crear una nueva conexión cada vez que se necesita.

Esto mejora significativamente el rendimiento, especialmente en aplicaciones con alta concurrencia.

"""

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

        """Obtiene una conexión del pool."""

        return cls.obtener_pool().get_connection()

    @classmethod

    def liberar_conexion(cls, conexion):

        """Libera la conexión devolviéndola al pool."""

        conexion.close()

######################################################################

# PARTE 5: PATRÓN DAO (DATA ACCESS OBJECT) #

######################################################################

"""

PATRÓN DAO (DATA ACCESS OBJECT)

El patrón DAO es un patrón de diseño que proporciona una capa de abstracción entre la aplicación y la base de datos.

Esto permite separar la lógica de acceso a datos de la lógica de negocio, facilitando el mantenimiento y la escalabilidad.

"""

class Cliente:

    """

    Esta clase representa una entidad cliente.

    Attributes:

        id (int): ID del cliente.

        nombre (str): Nombre del cliente.

        apellido (str): Apellido del cliente.

        membresia (int): Tipo de membresía del cliente.

    """

    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):

        self.id = id

        self.nombre = nombre

        self.apellido = apellido

        self.membresia = membresia

    def __str__(self):

        """Retorna una representación en string del cliente."""

        return (f'Id: {self.id}, Nombre: {self.nombre}, '

                f'Apellido: {self.apellido}, Membresia: {self.membresia}')

class ClienteDAO:

    """Data Access Object para gestionar registros de clientes en la base de datos."""

    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'

    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'

    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'

    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod

    def seleccionar(cls):

        """Recupera todos los clientes de la base de datos."""

        conexion = None

        try:

            conexion = Conexion.obtener_conexion()

            cursor = conexion.cursor()

            cursor.execute(cls.SELECCIONAR)

            registros = cursor.fetchall()

            clientes = [Cliente(*registro) for registro in registros]  # Desempaquetado de los registros en objetos Cliente

            return clientes

        except Exception as e:

            print(f'Error al recuperar clientes: {e}')

        finally:

            if conexion is not None:

                cursor.close()

                Conexion.liberar_conexion(conexion)

    @classmethod

    def insertar(cls, cliente):

        """Inserta un nuevo registro de cliente en la base de datos."""

        conexion = None

        try:

            conexion = Conexion.obtener_conexion()

            cursor = conexion.cursor()

            valores = (cliente.nombre, cliente.apellido, cliente.membresia)

            cursor.execute(cls.INSERTAR, valores)

            conexion.commit()

            return cursor.rowcount

        except Exception as e:

            print(f'Error al insertar cliente: {e}')

        finally:

            if conexion is not None:

                cursor.close()

                Conexion.liberar_conexion(conexion)

    @classmethod

    def actualizar(cls, cliente):

        """Actualiza un registro de cliente existente en la base de datos."""

        conexion = None

        try:

            conexion = Conexion.obtener_conexion()

            cursor = conexion.cursor()

            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)

            cursor.execute(cls.ACTUALIZAR, valores)

            conexion.commit()

            return cursor.rowcount

        except Exception as e:

            print(f'Error al actualizar cliente: {e}')

        finally:

            if conexion is not None:

                cursor.close()

                Conexion.liberar_conexion(conexion)

    @classmethod

    def eliminar(cls, cliente):

        """Elimina un registro de cliente de la base de datos."""

        conexion = None

        try:

            conexion = Conexion.obtener_conexion()

            cursor = conexion.cursor()

            valores = (cliente.id,)

            cursor.execute(cls.ELIMINAR, valores)

            conexion.commit()

            return cursor.rowcount

        except Exception as e:

            print(f'Error al eliminar cliente: {e}')

        finally:

            if conexion is not None:

                cursor.close()

                Conexion.liberar_conexion(conexion)

######################################################################

# PARTE 6: TEMAS AVANZADOS (TRANSACCIONES Y PROCEDIMIENTOS ALMACENADOS) #

######################################################################

"""

TRANSACCIONES EN MYSQL

Las transacciones son un conjunto de operaciones que se ejecutan como una sola unidad lógica de trabajo.

Si una operación falla, toda la transacción se revierte, garantizando la integridad de los datos.

"""

def ejemplo_transacciones():

    """

    Ejemplo de uso de transacciones en MySQL.

    Muestra:

    - Cómo iniciar una transacción

    - Cómo hacer commit o rollback según el resultado de operaciones

    - Manejo seguro de múltiples operaciones relacionadas

    """

    conexion = None

    try:

        conexion = mysql.connector.connect(

            host='localhost',

            user='root',

            password='Aroman1984',

            database='zona_fit_db'

        )

        # Desactivar autocommit para manejar transacciones manualmente

        conexion.autocommit = False

        cursor = conexion.cursor()

        # Ejemplo: transferir membresía entre clientes

        try:

            # Operación 1: Actualizar el cliente 1

            sql1 = "UPDATE cliente SET membresia = 'Premium' WHERE id = 1"

            cursor.execute(sql1)

            # Operación 2: Actualizar el cliente 2

            sql2 = "UPDATE cliente SET membresia = 'Básica' WHERE id = 2"

            cursor.execute(sql2)

            # Si ambas operaciones son exitosas, hacemos commit

            conexion.commit()

            print("\nTransacción completada exitosamente.")

        except Error as e:

            # Si hay algún error, revertimos los cambios

            conexion.rollback()

            print(f"\nError en la transacción, se ha realizado rollback: {e}")

    except Error as e:

        print(f"Error al conectar a MySQL: {e}")

    finally:

        if conexion is not None and conexion.is_connected():

            cursor.close()

            conexion.close()

            print("Conexión cerrada.")

"""

PROCEDIMIENTOS ALMACENADOS

Los procedimientos almacenados son un conjunto de instrucciones SQL que se almacenan en la base de datos

y se pueden ejecutar como una sola unidad.

Esto mejora el rendimiento y la seguridad, ya que la lógica se ejecuta en el servidor de la base de datos.



Ejemplo de uso de procedimientos almacenados en MySQL desde Python.

Nota: Este ejemplo asume que existe un procedimiento almacenado llamado

'ObtenerClientesPorMembresia' en la base de datos.

Muestra:

- Cómo llamar a un procedimiento almacenado

- Cómo pasar parámetros a un procedimiento

- Cómo recuperar resultados de un procedimiento

DELIMITER $$

CREATE PROCEDURE ObtenerClientesPorMembresia(IN tipo_membresia VARCHAR(50))
BEGIN
    SELECT * FROM cliente WHERE membresia = tipo_membresia;
END$$

DELIMITER ;

"""


def ejemplo_procedimiento_almacenado():
    """
    Ejemplo actualizado de uso de procedimientos almacenados en MySQL desde Python.
    Muestra:
    - Cómo llamar al procedimiento almacenado 'ObtenerClientesPorMembresia'
    - Cómo manejar los resultados de forma segura
    - Compatible con versiones futuras del conector

    Ejemplo de uso de procedimientos almacenados en MySQL desde Python.

    Asume que existe el procedimiento almacenado:
    'ObtenerClientesPorMembresia(IN tipo_membresia VARCHAR(50))'
    """
    conexion = None

    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Aroman1984',
            database='zona_fit_db'
        )

        cursor = conexion.cursor()

        tipo_membresia = 'Premium'
        args = (tipo_membresia,)

        # Llamada al procedimiento almacenado
        cursor.callproc('ObtenerClientesPorMembresia', args)

        # Compatibilidad con diferentes versiones del conector
        if hasattr(cursor, 'stored_results') and callable(cursor.stored_results):
            # Versión actual con método
            results = cursor.stored_results()
        elif hasattr(cursor, 'stored_results'):
            # Futura versión con propiedad
            results = cursor.stored_results
        else:
            results = []

        for result in results:
            print(f"\nClientes con membresía {tipo_membresia}:")
            for fila in result.fetchall():
                print(fila)

    except Error as e:
        print(f"Error al ejecutar el procedimiento almacenado: {e}")

    finally:
        if conexion is not None and conexion.is_connected():
            cursor.close()
            conexion.close()


######################################################################

# PARTE 7: APLICACIÓN ZONA FIT (GESTIÓN DE CLIENTES) #

######################################################################

"""

APLICACIÓN COMPLETA: GESTIÓN DE CLIENTES PARA UN GIMNASIO (ZONA FIT)

Esta sección implementa una aplicación completa para gestionar clientes de un gimnasio.

Incluye un menú interactivo por consola y operaciones CRUD completas.

"""

def main():

    """Función principal para ejecutar la aplicación de gestión de clientes."""

    print('*** Clientes Zona Fit (GYM) ***')

    opcion = None

    while opcion != 5:

        print('''

Menu:

1. Listar clientes

2. Agregar cliente

3. Modificar cliente

4. Eliminar cliente

5. Salir

''')

        try:

            opcion = int(input('Escribe tu opcion (1-5): '))

            if opcion == 1:

                # Listar clientes

                clientes = ClienteDAO.seleccionar()

                print('\n*** Listado de Clientes ***')

                for cliente in clientes:

                    print(cliente)

            elif opcion == 2:

                # Agregar cliente

                nombre_var = input('Escribe el nombre: ')

                apellido_var = input('Escribe el apellido: ')

                membresia_var = input('Escribe la membresia: ')

                cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)

                clientes_insertados = ClienteDAO.insertar(cliente)

                print(f'Clientes insertados: {clientes_insertados}')

            elif opcion == 3:

                # Modificar cliente

                id_cliente_var = int(input('Escribe el id del cliente a modificar: '))

                nombre_var = input('Escribe el nuevo nombre: ')

                apellido_var = input('Escribe el nuevo apellido: ')

                membresia_var = input('Escribe la nueva membresia: ')

                cliente = Cliente(id=id_cliente_var, nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)

                clientes_actualizados = ClienteDAO.actualizar(cliente)

                print(f'Clientes actualizados: {clientes_actualizados}')

            elif opcion == 4:

                # Eliminar cliente

                id_cliente_var = int(input('Escribe el id del cliente a eliminar: '))

                cliente = Cliente(id=id_cliente_var)

                clientes_eliminados = ClienteDAO.eliminar(cliente)

                print(f'Clientes eliminados: {clientes_eliminados}')

            elif opcion == 5:

                print('Salimos de la aplicacion...')

            else:

                print('Opción no válida, elige una opción entre 1 y 5.')

        except ValueError:

            print("Por favor, ingrese un número válido.")

######################################################################

# PARTE 8: FUNCIONES DE SOPORTE #

######################################################################

"""

FUNCIONES DE SOPORTE

Esta sección incluye funciones adicionales que facilitan la interacción con la base de datos

y la visualización de los resultados.

"""

def imprimir_resultados(resultados: List[Tuple], descripcion: str = "Resultados") -> None:

    """

    Imprime los resultados de una consulta SELECT.

    Args:

        resultados (List[Tuple]): Lista de tuplas con los datos a imprimir.

        descripcion (str, optional): Descripción de los resultados. Por defecto es "Resultados".

    """

    if resultados:

        print(f"\n--- {descripcion} ---")

        for fila in resultados:

            print(fila)

    else:

        print("\nNo se encontraron resultados.")

def generar_datos_prueba(conexion, num_personas=5):

    """

    Genera datos de prueba para la tabla personas.

    Args:

        conexion (MySQLConnection): Conexión a la base de datos.

        num_personas (int): Número de personas a generar.

    """

    try:

        cursor = conexion.cursor()

        sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"

        valores = [

            ('Ana', 'García', 25),

            ('Carlos', 'Rodríguez', 30),

            ('Sofía', 'Martínez', 22),

            ('David', 'López', 28),

            ('Elena', 'Sánchez', 35)

        ]

        cursor.executemany(sql, valores)

        conexion.commit()

        print(f"\nSe generaron {num_personas} personas de prueba.")

    except Error as e:

        print(f"Error al generar datos de prueba: {e}")

    finally:

        if 'cursor' in locals():

            cursor.close()

######################################################################

# BLOQUE PRINCIPAL #

######################################################################

"""

BLOQUE PRINCIPAL

En esta sección, se define el bloque principal del programa, que se ejecuta al iniciar la aplicación.

Aquí puedes descomentar las funciones que deseas probar o ejecutar.

"""

if __name__ == '__main__':

    # Descomentar las funciones que se deseen ejecutar

    # Ejemplos básicos de conexión y CRUD

    ejemplo_conexion_basica()

    ejemplo_insertar()

    ejemplo_actualizar()

    ejemplo_eliminar()

    # Ejemplo avanzado de SELECT

    conexion = crear_conexion()

    select_personas(conexion)

    cerrar_conexion(conexion)

    # Ejemplos de transacciones y procedimientos almacenados

    ejemplo_transacciones()

    ejemplo_procedimiento_almacenado

    #Iniciar la aplicación completa de gestión de clientes

    main()
