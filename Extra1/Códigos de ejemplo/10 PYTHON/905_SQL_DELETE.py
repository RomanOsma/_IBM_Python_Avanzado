#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------
# delete_cursosql.py
#
# Elimina registros de las tablas 'clientes' y 'articulos'.
#
# Requisitos:
#   pip install mysql-connector-python
#
# Uso:
#   python3 delete_cursosql.py
# ------------------------------------------------------------------

import mysql.connector

def main():
    try:
        # 1) Conexión
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='cursosql'
        )
        print("✔ Conectado a cursosql.")

        # 2) Cursor
        cursor = cnx.cursor()

        # 3) Definir sentencias DELETE
        # -----------------------------
        # a) Borrar un cliente concreto
        sql_delete_cliente = """
            DELETE FROM clientes
            WHERE codigoCliente = %s
        """
        datos_cliente = ('CT131',)  # cliente a eliminar

        # b) Borrar un artículo concreto
        sql_delete_articulo = """
            DELETE FROM articulos
            WHERE codigo_articulo = %s
        """
        datos_articulo = ('AR31',)  # artículo a eliminar

        # 4) Ejecutar deletes
        cursor.execute(sql_delete_cliente, datos_cliente)
        cursor.execute(sql_delete_articulo, datos_articulo)
        cnx.commit()
        print("✔ DELETEs ejecutados y commit realizado.")

    except mysql.connector.Error as err:
        print("❌ Error al DELETE:", err)

    finally:
        # 5) Cerrar recursos
        try:
            cursor.close()
            cnx.close()
            print("✔ Recursos cerrados.")
        except NameError:
            pass

if __name__ == "__main__":
    main()
