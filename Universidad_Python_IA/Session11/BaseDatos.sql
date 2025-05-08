-- ========================
-- DDL: Data Definition Language
-- ========================

-- Crear base de datos personas_db
CREATE DATABASE IF NOT EXISTS personas_db;
USE personas_db;

-- Crear tabla personas
CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Clave primaria autoincremental
    nombre VARCHAR(50) NOT NULL,       -- Nombre de la persona
    apellido VARCHAR(50) NOT NULL,     -- Apellido de la persona
    edad INT                           -- Edad de la persona
);

-- Crear base de datos zona_fit_db
CREATE DATABASE IF NOT EXISTS zona_fit_db;
USE zona_fit_db;

-- Crear tabla cliente
CREATE TABLE IF NOT EXISTS cliente (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Clave primaria autoincremental
    nombre VARCHAR(50) NOT NULL,       -- Nombre del cliente
    apellido VARCHAR(50) NOT NULL,     -- Apellido del cliente
    membresia VARCHAR(20)              -- Tipo de membresía (Premium, Básica, etc.)
);

-- ========================
-- DML: Data Manipulation Language
-- ========================

-- Insertar datos en personas (personas_db)
USE personas_db;
INSERT INTO personas (nombre, apellido, edad) VALUES
('Carmen', 'Reyes2', 31),
('Maria', 'Perez', 31),
('Sonia', 'Roman', 40),
('Victoria', 'Flores', 46),
('Angela', 'Lopez', 30),
('Victor', 'Ramos', 46),
('Angel', 'Roman', 40);

-- Consultar datos
SELECT * FROM personas;

-- Actualizar datos
UPDATE personas SET edad = 32 WHERE nombre = 'Carmen';

-- Eliminar datos
DELETE FROM personas WHERE nombre = 'Victor';

-- Insertar datos en cliente (zona_fit_db)
USE zona_fit_db;
INSERT INTO cliente (nombre, apellido, membresia) VALUES
('Maria', 'Roman', 'Premium'),
('Jose', 'Perez', 'Básica'),
('Alejandra', 'Tellez', 'Premium'),
('Josefa', 'Martinez', 'Premium');

-- Consultar datos
SELECT * FROM cliente;

-- ========================
-- DCL: Data Control Language
-- ========================

-- Crear usuario y otorgar permisos
CREATE USER IF NOT EXISTS 'usuario_estudio'@'localhost' IDENTIFIED BY 'tu_contraseña';

-- Otorgar permisos de solo lectura sobre personas_db
GRANT SELECT ON personas_db.* TO 'usuario_estudio'@'localhost';

-- Otorgar todos los permisos sobre zona_fit_db
GRANT ALL PRIVILEGES ON zona_fit_db.* TO 'usuario_estudio'@'localhost';

-- Revocar permisos
REVOKE ALL PRIVILEGES ON personas_db.* FROM 'usuario_estudio'@'localhost';

-- Aplicar cambios de permisos
FLUSH PRIVILEGES;

-- ========================
-- TCL: Transaction Control Language
-- ========================

-- Ejemplo de transacción
USE personas_db;
START TRANSACTION; -- Inicia la transacción

UPDATE personas SET edad = 35 WHERE nombre = 'Sonia';
DELETE FROM personas WHERE nombre = 'Angela';

-- Si todo está correcto, confirmamos los cambios
COMMIT;

-- Si hay un error y queremos deshacer los cambios
-- ROLLBACK;

-- ========================
-- Notas de uso
-- ========================
-- Cambia 'tu_contraseña' por una contraseña segura.
-- Puedes ejecutar cada bloque por separado en MySQL Workbench.
-- Siempre verifica en qué base de datos estás trabajando con USE nombre_db;
