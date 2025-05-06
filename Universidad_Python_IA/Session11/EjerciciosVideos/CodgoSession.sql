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
INSERT INTO C(nombre, apellido, edad) VALUES('Carmen', 'Reyes', 31);
INSERT INTO personas(nombre, apellido, edad) VALUES('Martha', 'Diaz', 22);
INSERT INTO personas(nombre, apellido, edad) VALUES('Maria', 'Perez', 31);
INSERT INTO personas(nombre, apellido, edad) VALUES('Sonia', 'Roman', 40);
INSERT INTO personas(nombre, apellido, edad) VALUES('Silvia', 'Castaño', 35);
INSERT INTO personas(nombre, apellido, edad) VALUES('Angela', 'Lopez', 30);

# SELECT: Consulta para obtener todos los registros
SELECT * FROM personas;
SELECT * FROM personas;
SELECT nombre, apellido, edad FROM personas;
SELECT * FROM personas WHERE edad > 30;

# UPDATE: Actualizar registros existentes
UPDATE personas SET nombre = 'Carmen2', apellido = 'Reyes2' WHERE id = 1;

# DELETE: Eliminar registros
DELETE FROM personas WHERE id = 2;


-- Base de datos para la aplicación Zona Fit

CREATE DATABASE IF NOT EXISTS zona_fit_db;
USE zona_fit_db;

CREATE TABLE IF NOT EXISTS cliente (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(50) NOT NULL,
membresia VARCHAR(20) NOT NULL
);


SELECT * FROM cliente ORDER BY id;

INSERT INTO cliente(nombre, apellido, membresia) VALUES(Silvia, Iglesias, Básico);

UPDATE cliente SET nombre=Angel, apellido=Roman, membresia=Premium WHERE id=1;

DELETE FROM cliente WHERE id=2;

DELIMITER $$

CREATE PROCEDURE ObtenerClientesPorMembresia(IN tipo_membresia VARCHAR(50))
BEGIN
    SELECT * FROM cliente WHERE membresia = tipo_membresia;
END$$

DELIMITER ;

SHOW PROCEDURE STATUS LIKE 'ObtenerClientesPorMembresia';

CALL ObtenerClientesPorMembresia('Premium');
