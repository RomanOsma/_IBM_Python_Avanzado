-- CRUD - Create (insert) - Read (select) - Update - Delete
SELECT nombre, apellido, edad FROM personas;
INSERT INTO personas(nombre, apellido, edad) VALUES('Carmen', 'Reyes', 31);
INSERT INTO personas(nombre, apellido, edad) VALUES('Martha', 'Diaz', 22);
UPDATE personas SET nombre = 'Carmen2', apellido = 'Reyes2' WHERE id = 1;
DELETE FROM personas WHERE id = 2;