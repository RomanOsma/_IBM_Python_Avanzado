CREATE DATABASE IF NOT EXISTS personas_db;

# USE: BD que usaremos
USE personas_db;

CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    edad INT
);

# INSERT: Insertar nuevos registros
INSERT INTO personas(nombre, apellido, edad) VALUES('Alba', 'Reyes', 31);
INSERT INTO personas(nombre, apellido, edad) VALUES('Juana', 'Diaz', 40);
INSERT INTO personas(nombre, apellido, edad) VALUES('Lucia', 'Perez', 31);
INSERT INTO personas(nombre, apellido, edad) VALUES('Pilar', 'Roman', 40);
INSERT INTO personas(nombre, apellido, edad) VALUES('Ana', 'Castaño', 15);

# SELECT: Consulta para obtener todos los registros
SELECT * FROM personas;
SELECT * FROM personas;
SELECT nombre, apellido, edad FROM personas;
SELECT * FROM personas WHERE edad > 30;

# UPDATE: Actualizar registros existentes
UPDATE personas SET nombre = 'Pamela', apellido = 'Andernos' WHERE id = 1;

# DELETE: Eliminar registros
DELETE FROM personas WHERE id = 7;