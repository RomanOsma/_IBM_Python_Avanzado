-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-04-2025 a las 22:01:56
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cursosql`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulos`
--

CREATE TABLE `articulos` (
  `codigo_articulo` varchar(10) NOT NULL,
  `seccion` varchar(50) NOT NULL,
  `nombre_articulo` varchar(100) NOT NULL,
  `precio` decimal(10,4) NOT NULL,
  `fecha` date NOT NULL,
  `importado` tinyint(1) NOT NULL,
  `pais_origen` varchar(50) NOT NULL,
  `foto` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `articulos`
--

INSERT INTO `articulos` (`codigo_articulo`, `seccion`, `nombre_articulo`, `precio`, `fecha`, `importado`, `pais_origen`, `foto`) VALUES
('AR01', 'Electrónica', 'Apple iPhone 13', 799.0000, '2021-09-24', 0, 'EE.UU.', 'ar01.jpg'),
('AR02', 'Electrónica', 'Sony WH-1000XM4 Auriculares', 349.9900, '2020-08-06', 0, 'Japón', 'ar02.jpg'),
('AR03', 'Electrónica', 'LG TV OLED 55\"', 1299.0000, '2022-03-10', 0, 'Corea del Sur', 'ar03.jpg'),
('AR04', 'Hogar', 'Robot aspirador Roomba i7', 599.9900, '2019-11-15', 1, 'EE.UU.', 'ar04.jpg'),
('AR05', 'Hogar', 'Cafetera Nespresso DeLonghi', 179.0000, '2020-02-20', 0, 'Suiza', 'ar05.jpg'),
('AR06', 'Ferretería', 'Taladro Bosch Professional GSB 13 RE', 89.9500, '2018-07-05', 0, 'Alemania', 'ar06.jpg'),
('AR07', 'Ferretería', 'Juego de llaves inglesas Stanley', 29.9900, '2017-10-12', 0, 'EE.UU.', 'ar07.jpg'),
('AR08', 'Confección', 'Camisa Hugo Boss Slim Fit', 99.9900, '2021-04-30', 0, 'Italia', 'ar08.jpg'),
('AR09', 'Confección', 'Pantalón Levi\'s 501 Original', 89.9900, '2020-05-18', 0, 'EE.UU.', 'ar09.jpg'),
('AR10', 'Confección', 'Chaqueta The North Face', 149.9900, '2021-11-01', 0, 'EE.UU.', 'ar10.jpg'),
('AR11', 'Juguetería', 'LEGO Technic Bugatti Chiron', 349.9900, '2019-01-01', 0, 'Dinamarca', 'ar11.jpg'),
('AR12', 'Juguetería', 'Barbie Casa de Ensueño', 199.9900, '2021-06-15', 0, 'EE.UU.', 'ar12.jpg'),
('AR13', 'Deportes', 'Bicicleta Decathlon Rockrider ST 520', 299.9900, '2020-03-22', 0, 'Francia', 'ar13.jpg'),
('AR14', 'Deportes', 'Nike Air Zoom Pegasus 38', 120.0000, '2021-07-10', 0, 'EE.UU.', 'ar14.jpg'),
('AR15', 'Deportes', 'Raqueta Wilson Pro Staff RF97', 229.9900, '2019-08-30', 0, 'EE.UU.', 'ar15.jpg'),
('AR16', 'Oficina', 'Silla ergonómica Herman Miller Aeron', 1399.9900, '2020-10-05', 0, 'EE.UU.', 'ar16.jpg'),
('AR17', 'Oficina', 'Impresora HP LaserJet Pro M404dn', 249.9900, '2021-02-12', 0, 'China', 'ar17.jpg'),
('AR18', 'Oficina', 'Escritorio regulable FlexiSpot Stand Up', 299.9900, '2022-01-20', 1, 'China', 'ar18.jpg'),
('AR19', 'Belleza', 'Plancha de pelo GHD Platinum+', 249.0000, '2019-09-23', 0, 'Reino Unido', 'ar19.jpg'),
('AR20', 'Belleza', 'Crema facial La Roche-Posay Hyalu B5', 29.9900, '2021-03-10', 0, 'Francia', 'ar20.jpg'),
('AR21', 'Alimentación', 'Aceite de Oliva Virgen Extra 1L', 12.5000, '2022-04-01', 0, 'España', 'ar21.jpg'),
('AR22', 'Alimentación', 'Jamón ibérico de bellota acorn-fed', 79.9900, '2021-12-15', 0, 'España', 'ar22.jpg'),
('AR23', 'Alimentación', 'Queso Manchego DOP 300g', 5.9900, '2022-02-10', 0, 'España', 'ar23.jpg'),
('AR24', 'Alimentación', 'Café en grano Starbucks Colombia 1kg', 19.9900, '2021-09-01', 0, 'EE.UU.', 'ar24.jpg'),
('AR25', 'Automoción', 'Neumático Michelin Pilot Sport 4 225/45 R17', 129.9900, '2020-06-20', 0, 'Francia', 'ar25.jpg'),
('AR26', 'Automoción', 'Aceite Mobil 1 5W-30 4L', 39.9900, '2021-05-05', 0, 'EE.UU.', 'ar26.jpg'),
('AR27', 'Automoción', 'Batería Varta Silver Dynamic 12V 70Ah', 119.9900, '2019-11-11', 0, 'Alemania', 'ar27.jpg'),
('AR28', 'Juguetería', 'Drone DJI Mini 2', 449.9900, '2020-11-10', 0, 'China', 'ar28.jpg'),
('AR29', 'Electrónica', 'Tablet Apple iPad Air (2022)', 599.9900, '2022-03-18', 0, 'China', 'ar29.jpg'),
('AR30', 'Electrónica', 'Auriculares JBL Tune 225TWS', 79.9900, '2021-08-05', 0, 'China', 'ar30.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articulos`
--
ALTER TABLE `articulos`
  ADD PRIMARY KEY (`codigo_articulo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
