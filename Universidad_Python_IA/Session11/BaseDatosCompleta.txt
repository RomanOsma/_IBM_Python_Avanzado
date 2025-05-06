-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2025 at 07:51 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cursosql`
--

-- --------------------------------------------------------

--
-- Table structure for table `articulos`
--

CREATE TABLE `articulos` (
  `codigo_articulo` varchar(10) NOT NULL,
  `seccion` varchar(50) NOT NULL,
  `nombre_articulo` varchar(255) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `fecha` date NOT NULL,
  `importado` tinyint(1) DEFAULT NULL,
  `pais_origen` varchar(50) DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `articulos`
--

INSERT INTO `articulos` (`codigo_articulo`, `seccion`, `nombre_articulo`, `precio`, `fecha`, `importado`, `pais_origen`, `foto`) VALUES
('AR01', 'Electrónica', 'Apple iPhone 13', 799.00, '2021-09-24', 1, 'EEUU', 'ip13.jpg'),
('AR02', 'Electrónica', 'Sony WH-1000XM4 Auriculares', 279.99, '2020-08-15', 1, 'Japón', 'sony_wh1000xm4.jpg'),
('AR03', 'Electrónica', 'LG 75\" OLED TV', 2499.00, '2022-03-10', 1, 'Corea del Sur', 'lg_oled75.jpg'),
('AR04', 'Hogar', 'Robot aspirador Roomba i7', 349.00, '2021-11-16', 1, 'EEUU', 'roomba_i7.jpg'),
('AR05', 'Hogar', 'Cafetera Nespresso DeLonghi', 179.00, '2020-05-20', 1, 'Italia', 'nespresso_delonghi.jpg'),
('AR06', 'Electrónica', 'Samsung Galaxy S23 Ultra', 1199.00, '2023-02-01', 1, 'Corea del Sur', 'samsung_s23.jpg'),
('AR07', 'Hogar', 'Lavadora Bosch Serie 8', 899.00, '2022-11-01', 1, 'Alemania', 'bosch_lavadora.jpg'),
('AR08', 'Moda', 'Chaqueta de cuero Schott NYC', 499.00, '2023-03-01', 1, 'EEUU', 'schott_chaqueta.jpg'),
('AR09', 'Libros', 'Cien años de soledad', 22.50, '1967-05-30', 0, 'Colombia', 'cien_anios.jpg'),
('AR10', 'Música', 'Álbum Thriller de Michael Jackson', 15.99, '1982-11-30', 1, 'EEUU', 'thriller.jpg'),
('AR11', 'Herramientas', 'Taladro inalámbrico Makita', 249.00, '2023-01-15', 1, 'Japón', 'makita_taladro.jpg'),
('AR12', 'Deportes', 'Bicicleta de Montaña Rockrider ST520', 299.99, '2021-03-15', 0, 'España', 'rockrider_st520.jpg'),
('AR13', 'Deportes', 'Nike Zoom Pegasus 38', 120.00, '2021-07-10', 1, 'EEUU', 'nike_pegasus.jpg'),
('AR14', 'Jardinería', 'Cortacésped Husqvarna', 399.00, '2022-04-01', 1, 'Suecia', 'husqvarna_cortacesped.jpg'),
('AR15', 'Automóvil', 'Neumáticos Michelin Primacy 4', 120.00, '2023-02-15', 1, 'Francia', 'michelin_neumaticos.jpg'),
('AR16', 'Deportes', 'Balón de baloncesto Spalding NBA', 29.99, '2023-03-01', 0, 'EEUU', 'spalding_balon.jpg'),
('AR17', 'Oficina', 'Silla de oficina Herman Miller Aeron', 1499.00, '2022-09-01', 1, 'EEUU', 'herman_miller_silla.jpg'),
('AR18', 'Joyería', 'Reloj Rolex Submariner', 10000.00, '1954-01-01', 1, 'Suiza', 'rolex_submariner.jpg'),
('AR19', 'Alimentos', 'Jamón Ibérico de Bellota', 400.00, '2023-02-01', 0, 'España', 'jamon_iberico.jpg'),
('AR20', 'Bebidas', 'Vino tinto Rioja Gran Reserva', 50.00, '2015-01-01', 0, 'España', 'rioja_gran_reserva.jpg'),
('AR21', 'Electrónica', 'Amazon Echo Dot', 49.99, '2023-05-01', 1, 'EEUU', 'amazon_echo_dot.jpg'),
('AR22', 'Hogar', 'Dyson V11 Absolute', 699.00, '2022-10-01', 1, 'Malasia', 'dyson_v11.jpg'),
('AR23', 'Moda', 'Ray-Ban Aviator', 150.00, '1937-01-01', 1, 'Italia', 'rayban_aviator.jpg'),
('AR24', 'Libros', '1984 de George Orwell', 12.99, '1949-06-08', 0, 'Reino Unido', '1984_orwell.jpg'),
('AR25', 'Música', 'Led Zeppelin IV', 18.50, '1971-11-08', 1, 'Reino Unido', 'led_zeppelin_iv.jpg'),
('AR26', 'Deportes', 'Tabla de Surf Channel Islands', 850.00, '2023-04-15', 1, 'EEUU', 'channel_islands_surfboard.jpg'),
('AR27', 'Jardinería', 'Set de herramientas de jardinería Fiskars', 79.99, '2022-09-01', 1, 'Finlandia', 'fiskars_garden_tools.jpg'),
('AR28', 'Automóvil', 'GPS Garmin DriveSmart 66', 199.00, '2023-01-15', 1, 'Suiza', 'garmin_drivesmart.jpg'),
('AR29', 'Oficina', 'Impresora HP LaserJet Pro M404dn', 279.00, '2022-07-01', 1, 'EEUU', 'hp_laserjet_m404dn.jpg'),
('AR30', 'Alimentos', 'Aceite de oliva virgen extra Castillo de Canena', 25.00, '2023-03-01', 0, 'España', 'castillo_canena_olive_oil.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `codigoCliente` varchar(10) NOT NULL,
  `empresa` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `poblacion` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `responsable` varchar(255) DEFAULT NULL,
  `historial` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`codigoCliente`, `empresa`, `direccion`, `poblacion`, `telefono`, `responsable`, `historial`) VALUES
('CT101', 'Global Tech S.L.', 'Camino de la Paz 195', 'Madrid', '944751217', 'Juan Pérez', 'Financiado'),
('CT102', 'Industrial Norte S.A.', 'Camino de la Libertad 104', 'Murcia', '666666666', 'María García', 'En seguimiento'),
('CT103', 'Alimentos Martínez S.L.', 'Avenida del Sol 130', 'Zaragoza', '628759361', 'Carlos López', 'Factura pendiente'),
('CT104', 'Construcciones Ruiz S.A.', 'Paseo Real 65', 'Valladolid', '990785928', 'Ana Martínez', 'Descuento aplicado'),
('CT105', 'Inmobiliaria Solar S.L.', 'Plaza Gran Vía 26', 'Gijón', '654318320', 'Luis Sánchez', 'Pago al contado'),
('CT106', 'AgroFresh S.A.', 'Paseo de la Libertad 26', 'Bilbao', '652439202', 'Laura Fernández', 'En seguimiento'),
('CT107', 'Transporte Global S.L.', 'Avenida de la Paz 142', 'Murcia', '679674900', 'José Rodríguez', 'Volver a comprar'),
('CT108', 'Marketing Pro S.A.', 'Calle Gran Vía 141', 'Barcelona', '963528199', 'Marta Gómez', 'Cliente nuevo'),
('CT109', 'Consultoría Nexus S.L.', 'Paseo de la Libertad 127', 'Sevilla', '653849100', 'David Díaz', 'Factura pendiente'),
('CT110', 'Salud Integral S.A.', 'Avenida del Sol 46', 'Sevilla', '629125273', 'Carmen Ruiz', 'Financiado'),
('CT111', 'BioPharma S.L.', 'Camino Gran Vía 24', 'Málaga', '073174038', 'Javier Hernández', 'Pago al contado'),
('CT112', 'EcoLogistics S.A.', 'Calle Real 78', 'Zaragoza', '629751810', 'Sara Jiménez', 'Financiado'),
('CT113', 'Finanzas Ágora S.L.', 'Plaza del Sol 139', 'Córdoba', '99058204', 'Miguel Torres', 'Financiado'),
('CT114', 'Tech Solutions Madrid', 'Calle de la Tecnología 12', 'Madrid', '912345678', 'Elena García', 'Cliente VIP'),
('CT115', 'Gourmet Delights Barcelona', 'Avenida de la Comida 34', 'Barcelona', '938765432', 'Pere Puig', 'Pago online'),
('CT116', 'Andalusian Sun S.A.', 'Carretera del Sol 56', 'Sevilla', '954123456', 'María Rodríguez', 'En seguimiento'),
('CT117', 'Basque Country Imports', 'Calle del Puerto 78', 'Bilbao', '944987654', 'Iñaki López', 'Descuento aplicado'),
('CT118', 'Galician Seafoods', 'Plaza de la Pescadería 90', 'Vigo', '986543210', 'Rosa Pérez', 'Pago al contado'),
('CT119', 'Valencia Oranges Inc.', 'Huerta Valenciana s/n', 'Valencia', '963210987', 'Juan García', 'Cliente nuevo'),
('CT120', 'Aragón Wines S.L.', 'Carretera del Vino km 25', 'Zaragoza', '976876543', 'Isabel Martínez', 'Volver a comprar'),
('CT121', 'Asturian Cider Co.', 'Calle de la Sidra 1', 'Oviedo', '985234567', 'Carlos Fernández', 'Factura pendiente'),
('CT122', 'Balearic Boats S.A.', 'Puerto Deportivo s/n', 'Palma de Mallorca', '971876543', 'Marta Sánchez', 'Financiado'),
('CT123', 'Canary Islands Resorts', 'Playa de las Canteras 100', 'Las Palmas', '928123456', 'Pedro Rodríguez', 'Cliente VIP'),
('CT124', 'Rioja Vineyards', 'Finca La Rioja s/n', 'Logroño', '941234567', 'Sofía Martínez', 'Pago online'),
('CT125', 'Extremadura Ham S.A.', 'Dehesa Extremeña s/n', 'Cáceres', '927987654', 'Diego López', 'En seguimiento'),
('CT126', 'Murcian Vegetables S.L.', 'Huerta Murciana s/n', 'Murcia', '968543210', 'Carmen García', 'Descuento aplicado'),
('CT127', 'Cantabrian Steelworks', 'Polígono Industrial s/n', 'Santander', '942345678', 'Javier Pérez', 'Pago al contado'),
('CT128', 'Castilian Ceramics', 'Calle de la Cerámica 22', 'Toledo', '925876543', 'Elena Martínez', 'Cliente nuevo'),
('CT129', 'Navarran Forests S.L.', 'Bosque Navarro s/n', 'Pamplona', '948123456', 'David García', 'Volver a comprar'),
('CT130', 'Ceuta Free Port S.A.', 'Puerto Libre s/n', 'Ceuta', '956123456', 'María Sánchez', 'Factura pendiente'),
('CT134', 'Soluciones Informáticas', 'Calle Programadores 10', 'Sevilla', '955234567', 'Miguel Ángel López', 'Cliente ocasional'),
('CT135', 'Automoción Avanzada', 'Carretera de la Industria km 7', 'Zaragoza', '976987654', 'Laura Martínez', 'Financiado'),
('CT136', 'Construcciones El Sol', 'Avenida del Sol, 123', 'Málaga', '612345678', 'Antonio Gómez', 'Cliente regular'),
('CT137', 'Electrónica Futuro', 'Calle Luna, 45', 'Granada', '958234567', 'Ana Fernández', 'Nuevo cliente'),
('CT138', 'Textiles La Moda', 'Polígono Industrial, nave 7', 'Alicante', '965345678', 'Carlos Martínez', 'Cliente preferente'),
('CT139', 'Supermercados La Mancha', 'Plaza del Pueblo, 2', 'Ciudad Real', '926456789', 'María Sánchez', 'Pago al contado'),
('CT140', 'Joyería El Brillante', 'Calle Mayor, 10', 'Salamanca', '923567890', 'Pedro López', 'Cliente VIP'),
('CT141', 'Muebles Modernos S.L.', 'Avenida Europa, 5', 'Murcia', '667890123', 'Sofía Ruiz', 'En negociación'),
('CT142', 'Calzados El Paso', 'Calle Ancha, 20', 'Cádiz', '956789012', 'Javier Pérez', 'Descuento aplicado'),
('CT143', 'Informática Avanzada', 'Parque Tecnológico, 14', 'Valencia', '960234567', 'Isabel García', 'Cliente ocasional'),
('CT144', 'Restaurante El Buen Gusto', 'Plaza de la Constitución, 8', 'Toledo', '925345678', 'Miguel Ángel Rodríguez', 'Cliente regular'),
('CT145', 'Deportes Extremos S.A.', 'Calle Aventura, 9', 'Huesca', '974456789', 'Laura Martínez', 'Financiado'),
('CT146', 'Ferretería El Clavo', 'Calle Industria, 33', 'León', '987567890', 'Roberto Díaz', 'Nuevo cliente'),
('CT147', 'Librería Cervantes', 'Calle del Libro, 1', 'Valladolid', '983678901', 'Elena Martínez', 'Cliente preferente'),
('CT148', 'Óptica La Vista', 'Avenida Goya, 22', 'Zaragoza', '976789012', 'David García', 'Pago online'),
('CT149', 'Perfumería Esencias', 'Calle Bella, 11', 'Oviedo', '985890123', 'Carmen Fernández', 'Cliente VIP'),
('CT150', 'Agencia de Viajes MundiTour', 'Gran Vía, 44', 'Madrid', '911234567', 'Sergio Sánchez', 'Cliente ocasional'),
('CT151', 'Distribuciones Rápidas S.L.', 'Avenida del Mar, 78', 'Valencia', '963456789', 'Lucía Martínez', 'Cliente recurrente'),
('CT152', 'Talleres Mecánicos Precision', 'Calle de la Industria, 45', 'Bilbao', '944567890', 'Andrés Gómez', 'Cliente nuevo'),
('CT153', 'Hostelería Premium', 'Plaza Mayor, 12', 'Sevilla', '955678901', 'Pablo Sánchez', 'Pago aplazado'),
('CT154', 'Logística Internacional', 'Polígono Industrial Norte, nave 23', 'Barcelona', '934567890', 'Marta López', 'Cliente VIP'),
('CT155', 'Suministros Médicos S.A.', 'Calle Salud, 34', 'Madrid', '915678901', 'Jorge Fernández', 'Cliente regular'),
('CT156', 'Consultoría Estratégica', 'Torre Picasso, planta 10', 'Madrid', '916789012', 'Alicia Rodríguez', 'En seguimiento'),
('CT157', 'Materiales de Construcción', 'Carretera de Sevilla, km 3', 'Huelva', '957890123', 'Daniel García', 'Factura pendiente'),
('CT158', 'Alimentación Ecológica S.L.', 'Camino del Prado, 56', 'Valladolid', '983901234', 'Clara Hernández', 'Cliente nuevo'),
('CT159', 'Sistemas Informáticos Avanzados', 'Parque Tecnológico, edificio B', 'Valencia', '960123456', 'Raúl Jiménez', 'Cliente preferente'),
('CT160', 'Moda Contemporánea', 'Calle Serrano, 89', 'Madrid', '912345678', 'Paula Moreno', 'Descuento aplicado'),
('CT161', 'Distribuidora Farmacéutica', 'Avenida de la Salud, 67', 'Barcelona', '932345678', 'Roberto Gil', 'Cliente regular'),
('CT162', 'Electrónica Industrial', 'Polígono Tecnológico, nave 12', 'Zaragoza', '973456789', 'Mónica Torres', 'Pago al contado'),
('CT163', 'Transportes Rápidos S.L.', 'Calle Mercancías, 34', 'Málaga', '954567890', 'José Martín', 'Financiado'),
('CT164', 'Manufacturas del Sur', 'Carretera de Cádiz, km 5', 'Sevilla', '955678901', 'Carmen Vega', 'Cliente ocasional'),
('CT165', 'Mobiliario de Oficina', 'Gran Vía, 123', 'Madrid', '916789012', 'Francisco Ruiz', 'Cliente VIP'),
('CT166', 'Alimentos Congelados S.A.', 'Carretera del Frío, 78', 'Valencia', '967890123', 'Silvia Morales', 'En seguimiento'),
('CT167', 'Seguridad Integral', 'Calle Protección, 56', 'Barcelona', '938901234', 'Alberto Sánchez', 'Cliente regular'),
('CT168', 'Componentes Electrónicos', 'Parque Industrial Este, 45', 'Bilbao', '949012345', 'Marina López', 'Factura pendiente'),
('CT169', 'Distribuidora Textil', 'Avenida de la Moda, 78', 'Madrid', '910123456', 'Ignacio García', 'Pago online'),
('CT170', 'Productos Químicos S.A.', 'Polígono Químico, nave 8', 'Tarragona', '972345678', 'Laura Fernández', 'Descuento aplicado'),
('CT171', 'Asesores Financieros', 'Plaza del Ayuntamiento, 9', 'Valencia', '963456789', 'Carlos Navarro', 'Cliente VIP'),
('CT172', 'Soluciones Web', 'Calle Digital, 23', 'Barcelona', '934567890', 'Natalia Vargas', 'Cliente nuevo'),
('CT173', 'Energías Renovables S.L.', 'Avenida Solar, 45', 'Madrid', '915678901', 'Héctor Martínez', 'En negociación'),
('CT174', 'Productos de Limpieza', 'Calle Higiene, 67', 'Sevilla', '956789012', 'Isabel Domínguez', 'Cliente regular'),
('CT175', 'Servicios Audiovisuales', 'Parque Tecnológico, edificio C', 'Málaga', '957890123', 'Gonzalo Pérez', 'Pago aplazado'),
('CT176', 'Importaciones Asiáticas', 'Puerto Comercial, almacén 5', 'Barcelona', '938901234', 'Elena Wu', 'Cliente preferente'),
('CT177', 'Papelería Industrial', 'Calle del Papel, 12', 'Madrid', '919012345', 'Ramón Gutiérrez', 'Descuento aplicado'),
('CT178', 'Carpintería Metálica', 'Polígono Industrial Sur, nave 3', 'Valencia', '960123456', 'Cristina Molina', 'Cliente ocasional'),
('CT179', 'Software a Medida S.L.', 'Edificio Crystal, planta 5', 'Madrid', '912345678', 'Javier Núñez', 'Cliente VIP'),
('CT180', 'Distribuidora de Bebidas', 'Camino de los Viñedos, 78', 'La Rioja', '942345678', 'Rosa Martínez', 'Factura pendiente'),
('CT181', 'Maquinaria Pesada S.A.', 'Polígono Industrial Norte, 12', 'Bilbao', '943456789', 'Manuel González', 'Cliente regular'),
('CT182', 'Telecomunicaciones Avanzadas', 'Torre de Comunicaciones, planta 3', 'Madrid', '914567890', 'Sonia Torres', 'En seguimiento'),
('CT183', 'Productos Gourmet', 'Mercado Central, puesto 45', 'Barcelona', '935678901', 'Luis García', 'Cliente preferente');

-- --------------------------------------------------------

--
-- Table structure for table `pedidos`
--

CREATE TABLE `pedidos` (
  `codigo_pedido` int(10) UNSIGNED NOT NULL,
  `codigo_cliente` varchar(10) NOT NULL,
  `codigo_articulo` varchar(10) NOT NULL,
  `cantidad` int(10) UNSIGNED NOT NULL,
  `fecha_pedido` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pedidos`
--

INSERT INTO `pedidos` (`codigo_pedido`, `codigo_cliente`, `codigo_articulo`, `cantidad`, `fecha_pedido`) VALUES
(1, 'CT101', 'AR01', 2, '2025-01-10'),
(2, 'CT101', 'AR03', 1, '2025-01-15'),
(3, 'CT102', 'AR02', 3, '2025-01-20'),
(4, 'CT103', 'AR05', 2, '2025-01-25'),
(5, 'CT104', 'AR04', 1, '2025-02-01'),
(6, 'CT105', 'AR01', 5, '2025-02-05'),
(7, 'CT106', 'AR02', 2, '2025-02-10'),
(8, 'CT107', 'AR03', 3, '2025-02-15'),
(9, 'CT108', 'AR04', 4, '2025-02-20'),
(10, 'CT109', 'AR05', 1, '2025-02-25'),
(11, 'CT110', 'AR01', 2, '2025-03-01'),
(12, 'CT111', 'AR02', 3, '2025-03-05'),
(13, 'CT112', 'AR03', 1, '2025-03-10'),
(14, 'CT113', 'AR04', 2, '2025-03-15'),
(15, 'CT114', 'AR12', 1, '2025-03-20'),
(16, 'CT115', 'AR13', 2, '2025-03-25'),
(17, 'CT101', 'AR01', 1, '2025-04-01'),
(18, 'CT102', 'AR02', 2, '2025-04-05'),
(19, 'CT103', 'AR03', 3, '2025-04-10'),
(20, 'CT104', 'AR04', 1, '2025-04-15'),
(21, 'CT105', 'AR05', 2, '2025-04-20'),
(22, 'CT106', 'AR12', 1, '2025-04-25'),
(23, 'CT107', 'AR13', 3, '2025-05-01'),
(24, 'CT108', 'AR01', 2, '2025-05-05'),
(25, 'CT109', 'AR02', 1, '2025-05-10'),
(26, 'CT110', 'AR03', 4, '2025-05-15'),
(27, 'CT111', 'AR04', 2, '2025-05-20'),
(28, 'CT112', 'AR05', 1, '2025-05-25'),
(29, 'CT113', 'AR12', 2, '2025-06-01'),
(30, 'CT114', 'AR13', 1, '2025-06-05'),
(31, 'CT115', 'AR01', 3, '2025-06-10'),
(32, 'CT116', 'AR02', 1, '2025-06-15'),
(33, 'CT117', 'AR03', 2, '2025-06-20'),
(34, 'CT118', 'AR04', 3, '2025-06-25'),
(35, 'CT119', 'AR05', 1, '2025-07-01'),
(36, 'CT120', 'AR12', 2, '2025-07-05'),
(37, 'CT121', 'AR13', 1, '2025-07-10'),
(38, 'CT122', 'AR01', 4, '2025-07-15'),
(39, 'CT123', 'AR02', 2, '2025-07-20'),
(40, 'CT124', 'AR03', 1, '2025-07-25'),
(41, 'CT125', 'AR04', 3, '2025-08-01'),
(42, 'CT126', 'AR05', 1, '2025-08-05'),
(43, 'CT127', 'AR12', 2, '2025-08-10'),
(44, 'CT128', 'AR13', 1, '2025-08-15'),
(45, 'CT129', 'AR01', 2, '2025-08-20'),
(46, 'CT130', 'AR02', 3, '2025-08-25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articulos`
--
ALTER TABLE `articulos`
  ADD PRIMARY KEY (`codigo_articulo`);

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`codigoCliente`);

--
-- Indexes for table `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`codigo_pedido`),
  ADD KEY `codigo_cliente` (`codigo_cliente`),
  ADD KEY `codigo_articulo` (`codigo_articulo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `codigo_pedido` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=125;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`codigo_cliente`) REFERENCES `clientes` (`codigoCliente`),
  ADD CONSTRAINT `pedidos_ibfk_2` FOREIGN KEY (`codigo_articulo`) REFERENCES `articulos` (`codigo_articulo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
