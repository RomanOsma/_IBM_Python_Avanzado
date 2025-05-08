# Eliminar registros desde python a mysql

import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',  # 127.0.0.1
    user='root',
    password='Aroman1984',
    database='personas_db'
)

# ejecutar la sentencia delete
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (9,)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha eliminado el registro')
cursor.close()
personas_db.close()