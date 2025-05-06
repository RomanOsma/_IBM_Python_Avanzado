#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------
# insert_cursosql.py
#
# Inserta un nuevo registro en las tablas 'clientes' y 'articulos'.
#
# Requisitos:
#   pip install mysql-connector-python
#
# Uso:
#   python3 insert_cursosql.py
# ------------------------------------------------------------------

import mysql.connector

def main():
    try:
        # 1) Conexión a la BBDD
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='cursosql'
        )
        print("✔ Conectado a cursosql (root, sin password).")

        # 2) Crear cursor
        cursor = cnx.cursor()

        # 3) Definir sentencias INSERT
        # -----------------------------
        # Ejemplo para 'clientes'
        sql_insert_cliente = """
            INSERT INTO clientes
                (codigoCliente, empresa, direccion, poblacion, telefono, responsable, historial)
            VALUES
                (%s, %s, %s, %s, %s, %s, %s)
        """
        datos_cliente = (
            'CT131',                     # nuevo código
            'ACME',       # empresa
            'Calle Nueva 12',            # dirección
            'Sevilla',                   # población
            '954123456',                 # teléfono
            'Laura Torres',              # responsable
            'Cliente nuevo'              # historial
        )

        # Ejemplo para 'articulos'
        sql_insert_articulo = """
            INSERT INTO articulos
                (codigo_articulo, seccion, nombre_articulo, precio, fecha, importado, pais_origen, foto)
            VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        datos_articulo = (
            'AR31',                      # código artículo
            'Juguetes',                   # sección
            'Silla ergonómica',         # nombre
            149.9900,                    # precio
            '2025-04-19',                # fecha
            0,                           # importado (0=no, 1=sí)
            'España',                    # país origen
            'ar05.jpg'                   # nombre de la foto
        )

        # 4) Ejecutar inserts
        cursor.execute(sql_insert_cliente, datos_cliente)
        cursor.execute(sql_insert_articulo, datos_articulo)
        # 5) Confirmar cambios en la BBDD
        cnx.commit()
        print("✔ INSERTs ejecutados y compromiso realizado (commit).")

    except mysql.connector.Error as err:
        print("❌ Error al INSERT:", err)

    finally:
        # 6) Cierre de recursos
        try:
            cursor.close()
            cnx.close()
            print("✔ Cursor y conexión cerrados.")
        except NameError:
            pass

if __name__ == "__main__":
    main()
