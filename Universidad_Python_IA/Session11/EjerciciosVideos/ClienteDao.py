from connexion import Conexion
from cliente import Cliente

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