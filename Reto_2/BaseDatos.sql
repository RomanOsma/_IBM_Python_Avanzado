CREATE DATABASE inventory_db;
USE inventory_db;
 
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(255)
);

CREATE TABLE price_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    new_price DECIMAL(10,2),
    change_date DATETIME,
    FOREIGN KEY (product_name) REFERENCES products(name)
);


INSERT INTO products (name, quantity, price, category)
VALUES ('Smartwatch TechPro', 100, 299.99, 'Electrónica');

-- Ver historial de precios de un producto
SELECT * FROM products 
WHERE name = 'Smartwatch TechPro';

ALTER TABLE price_history
DROP FOREIGN KEY price_history_ibfk_1,
ADD CONSTRAINT price_history_ibfk_1
FOREIGN KEY (product_name) REFERENCES products(name)
ON DELETE CASCADE;

SHOW CREATE TABLE price_history;

ALTER TABLE price_history
DROP FOREIGN KEY price_history_ibfk_1;

ALTER TABLE price_history
ADD CONSTRAINT price_history_ibfk_1
FOREIGN KEY (product_name) REFERENCES products(name)
ON DELETE CASCADE;

-- 1. Verificar el nombre de la restricción
SHOW CREATE TABLE price_history;

-- 2. Eliminar la restricción existente (si es necesario)
ALTER TABLE price_history
DROP FOREIGN KEY price_history_ibfk_1;

-- 3. Crear la nueva restricción con ON DELETE CASCADE
ALTER TABLE price_history
ADD CONSTRAINT price_history_ibfk_1
FOREIGN KEY (product_name) REFERENCES products(name)
ON DELETE CASCADE;