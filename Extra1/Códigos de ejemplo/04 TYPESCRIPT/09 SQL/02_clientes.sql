-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-04-2025 a las 22:01:49
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
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `codigoCliente` varchar(10) NOT NULL,
  `empresa` varchar(100) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `poblacion` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `responsable` varchar(100) DEFAULT NULL,
  `historial` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`codigoCliente`, `empresa`, `direccion`, `poblacion`, `telefono`, `responsable`, `historial`) VALUES
('CT101', 'Global Tech S.L.', 'Camino de la Paz 195', 'Madrid', '944751217', 'Juan Pérez', 'Financiado'),
('CT102', 'Industrial Norte S.A.', 'Camino de la Libertad 104', 'Murcia', '958056573', 'María García', 'En seguimiento'),
('CT103', 'Alimentos Martínez S.L.', 'Avenida del Sol 130', 'Zaragoza', '928756361', 'Carlos López', 'Factura pendiente'),
('CT104', 'Construcciones Ruiz S.A.', 'Paseo Real 65', 'Valladolid', '990785928', 'Ana Martínez', 'Descuento aplicado'),
('CT105', 'Inmobiliaria Soler S.L.', 'Plaza Gran Vía 26', 'Gijón', '954318320', 'Luis Sánchez', 'Pago al contado'),
('CT106', 'AgroFresh S.A.', 'Paseo de la Libertad 26', 'Bilbao', '952439202', 'Laura Fernández', 'En seguimiento'),
('CT107', 'Transporte Global S.L.', 'Avenida de la Paz 142', 'Murcia', '979974900', 'José Rodríguez', 'Volverá a comprar'),
('CT108', 'Marketing Pro S.A.', 'Calle Gran Vía 141', 'Barcelona', '963529189', 'Marta Gómez', 'Cliente nuevo'),
('CT109', 'Consultoría Nexus S.L.', 'Paseo de la Libertad 127', 'Sevilla', '953648190', 'David Díaz', 'Factura pendiente'),
('CT110', 'Salud Integral S.A.', 'Avenida del Sol 146', 'Sevilla', '929125273', 'Carmen Ruiz', 'Financiado'),
('CT111', 'BioPharma S.L.', 'Camino Gran Vía 24', 'Málaga', '978174638', 'Javier Hernández', 'Pago al contado'),
('CT112', 'EcoLogistics S.A.', 'Calle Real 78', 'Zaragoza', '926751810', 'Sara Jiménez', 'Financiado'),
('CT113', 'Finanzas Ágora S.L.', 'Plaza del Sol 139', 'Córdoba', '990958204', 'Miguel Torres', 'Financiado'),
('CT114', 'Seguros Iberia S.A.', 'Paseo de la Paz 74', 'Barcelona', '990032267', 'Patricia Ramos', 'Regular'),
('CT115', 'Moda Urbana S.L.', 'Plaza del Sol 148', 'Zaragoza', '934678442', 'José Luis Delgado', 'Reclamación abierta'),
('CT116', 'Automoción Central S.A.', 'Avenida Real 9', 'Alicante', '944904153', 'Elena Moreno', 'Pago al contado'),
('CT117', 'Electrodomésticos Delta S.L.', 'Calle del Sol 23', 'Gijón', '930072305', 'Francisco Navarro', 'Cliente nuevo'),
('CT118', 'Joyería Oro Fino S.L.', 'Calle Real 180', 'Alicante', '962518866', 'Lucía Castillo', 'Financiado'),
('CT119', 'Turismo Elite S.A.', 'Plaza del Sol 134', 'Vigo', '938883828', 'Pedro Ortiz', 'En seguimiento'),
('CT120', 'Deportes Plus S.L.', 'Camino de la Libertad 149', 'Murcia', '976123086', 'Sofía Varela', 'VIP'),
('CT121', 'Reformas Hidalgo S.L.', 'Calle Real 84', 'Barcelona', '975289435', 'Diego Molina', 'En seguimiento'),
('CT122', 'Textiles Europa S.A.', 'Plaza del Sol 49', 'Madrid', '946378099', 'Paula Rey', 'Factura pendiente'),
('CT123', 'Servicios Verdes S.L.', 'Avenida del Sol 96', 'Málaga', '967194352', 'Alberto Cruz', 'Cliente nuevo'),
('CT124', 'Hostelería Málaga S.L.', 'Calle del Sol 38', 'Madrid', '987022995', 'Monica Vega', 'Financiado'),
('CT125', 'Tecnología Infinita S.A.', 'Paseo Gran Vía 175', 'Madrid', '926702553', 'Alfredo Paredes', 'Reclamación abierta'),
('CT126', 'Café Aroma S.L.', 'Paseo Gran Vía 148', 'Bilbao', '922285197', 'Irene Ramos', 'VIP'),
('CT127', 'Veterinaria Animalia S.L.', 'Calle Real 10', 'Madrid', '936117555', 'Raúl Soto', 'Descuento aplicado'),
('CT128', 'Agencia Creativa S.L.', 'Calle del Sol 123', 'Valladolid', '918198675', 'Noelia Peña', 'Cliente nuevo'),
('CT129', 'Editorial Lectores S.L.', 'Paseo Real 109', 'Barcelona', '944885857', 'Óscar Guerrero', 'Factura pendiente'),
('CT130', 'Clínica Dental Smile S.L.', 'Avenida de la Libertad 19', 'Málaga', '968528143', 'Beatriz Ibarra', 'Descuento aplicado');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`codigoCliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
