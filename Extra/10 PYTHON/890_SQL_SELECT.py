#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------
# consulta_cursosql.py
#
# Conecta a la base de datos 'cursosql' y hace SELECTs
# sobre las tablas 'clientes' y 'articulos'.
#
# Requisitos:
#   pip install mysql-connector-python
#
# ------------------------------------------------------------------

import mysql.connector  # Cliente oficial de MySQL para Python

def main():
    """
    1) Conectar a MySQL
    2) Crear un cursor
    3) Ejecutar SELECT sobre 'clientes'
    4) Ejecutar SELECT sobre 'articulos'
    5) Mostrar resultados
    6) Manejo de errores y cierre de recursos
    """
    try:
        # ----------------------------------------------------------
        # 1) Establecer conexión con la BBDD
        # ----------------------------------------------------------
        # host='localhost'  → servidor local
        # user='root'       → usuario ROOT
        # password=''       → sin contraseña
        # database='cursosql' → nombre de la BBDD
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='cursosql'
        )
        print("✔ Conexión establecida con 'cursosql' (root, sin password).")

        # ----------------------------------------------------------
        # 2) Crear cursor en modo diccionario
        # ----------------------------------------------------------
        # dictionary=True → cada fila vendrá como dict {columna: valor}
        cursor = cnx.cursor(dictionary=True)

        # ----------------------------------------------------------
        # 3) Definir y ejecutar los SELECTs
        # ----------------------------------------------------------
        consultas = [
            ("Clientes", "SELECT * FROM clientes ORDER BY codigoCliente;"),
            ("Artículos", "SELECT * FROM articulos ORDER BY codigo_articulo;")
        ]

        for nombre, sql in consultas:
            print(f"\n--- {nombre} ---")
            # Ejecuta la consulta SQL
            cursor.execute(sql)
            # Obtiene todas las filas resultantes
            filas = cursor.fetchall()

            # ------------------------------------------------------
            # 4) Mostrar resultados
            # ------------------------------------------------------
            if filas:
                # Imprime cada fila como diccionario
                for fila in filas:
                    # Convertimos el dict en una línea legible
                    # ej: Cliente CT101 – Global Tech S.L. – … 
                    detalles = " – ".join(f"{k}: {v}" for k, v in fila.items())
                    print(detalles)
            else:
                print("  (sin resultados)")

    except mysql.connector.Error as err:
        # ----------------------------------------------------------
        # 5) Manejo de errores de conexión o de consulta
        # ----------------------------------------------------------
        print("❌ Ha ocurrido un error:", err)

    finally:
        # ----------------------------------------------------------
        # 6) Cierre de cursor y conexión (liberamos recursos)
        # ----------------------------------------------------------
        try:
            cursor.close()
            cnx.close()
            print("\n✔ Cursor y conexión cerrados.")
        except NameError:
            # Si cursor o cnx no existen, no hacemos nada
            pass

if __name__ == "__main__":
    main()
