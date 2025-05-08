# Insertar registros desde python a mysql

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='Aroman1984',
    database='personas_db'
)

# ejecutar la sentencia insert
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)'
valores = ('Alba', 'Perez', 63)
cursor.execute(sentencia_sql, valores)
personas_db.commit() # guardar los cambios en la bd
print(f'Se ha agregado el nuevo registro a la bd : {valores}')
cursor.close()
personas_db.close()

