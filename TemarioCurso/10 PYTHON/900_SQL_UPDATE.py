#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------
# update_cursosql.py
#
# Actualiza registros en las tablas 'clientes' y 'articulos'.
#
# Requisitos:
#   pip install mysql-connector-python
#
# Uso:
#   python3 update_cursosql.py
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

        # 3) Definir sentencias UPDATE
        # -----------------------------
        # a) Cambiar el teléfono de un cliente
        sql_update_cliente = """
            UPDATE clientes
            SET telefono = %s
            WHERE codigoCliente = %s
        """
        datos_cliente = (
            '666666666',  # nuevo teléfono
            'CT102'       # cliente a actualizar
        )

        # b) Subir el precio de un artículo un 10%
        sql_update_articulo = """
            UPDATE articulos
            SET precio = precio * 1.10
            WHERE codigo_articulo = %s
        """
        datos_articulo = ('AR31',)  # artículo a actualizar

        # 4) Ejecutar updates
        cursor.execute(sql_update_cliente, datos_cliente)
        cursor.execute(sql_update_articulo, datos_articulo)
        cnx.commit()
        print("✔ UPDATEs ejecutados y commit realizado.")

    except mysql.connector.Error as err:
        print("❌ Error al UPDATE:", err)

    finally:
        # 5) Cerrar cursor y conexión
        try:
            cursor.close()
            cnx.close()
            print("✔ Recursos cerrados.")
        except NameError:
            pass

if __name__ == "__main__":
    main()
