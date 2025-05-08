-- ###############################################
-- SCRIPT COMPLETO: 5 tablas con 50 registros cada
-- ###############################################

DROP TABLE IF EXISTS `articulos`;
CREATE TABLE `articulos` (
  `codigo_articulo` varchar(10) NOT NULL,
  `seccion` varchar(100) NOT NULL,
  `nombre_articulo` varchar(200) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `fecha` date NOT NULL,
  `importado` tinyint(1) NOT NULL,
  `pais_origen` varchar(100) DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`codigo_articulo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR001', 'Deporte', 'Bicicleta 716', '1640.7', '2024-01-24', '1', 'España', 'pr001.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR002', 'Deporte', 'Taladro 616', '1408.7', '2023-09-26', '0', 'España', 'pr002.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR003', 'Ferretería', 'Portátil 170', '1688.73', '2024-04-29', '0', 'Italia', 'pr003.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR004', 'Electrónica', 'Smartphone 204', '1543.02', '2024-01-02', '0', 'Japón', 'pr004.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR005', 'Hogar', 'Taladro 624', '607.33', '2024-02-09', '1', 'Alemania', 'pr005.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR006', 'Ferretería', 'Cafetera 377', '1607.33', '2023-05-07', '1', 'Italia', 'pr006.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR007', 'Hogar', 'Portátil 701', '1544.46', '2023-12-15', '0', 'España', 'pr007.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR008', 'Electrónica', 'Auriculares 592', '123.65', '2023-01-21', '0', 'China', 'pr008.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR009', 'Ferretería', 'Smartphone 819', '1491.6', '2023-01-10', '0', 'Italia', 'pr009.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR010', 'Deporte', 'Portátil 573', '187.18', '2023-10-02', '0', 'España', 'pr010.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR011', 'Ferretería', 'Sudadera 832', '1994.57', '2023-03-29', '1', 'Alemania', 'pr011.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR012', 'Confección', 'Smartphone 219', '1879.72', '2024-01-27', '1', 'Alemania', 'pr012.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR013', 'Confección', 'Bicicleta 943', '1556.62', '2023-09-29', '1', 'Alemania', 'pr013.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR014', 'Ferretería', 'Zapatillas running 604', '1921.27', '2024-01-23', '0', 'Alemania', 'pr014.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR015', 'Ferretería', 'Sudadera 452', '1099.12', '2023-12-18', '1', 'China', 'pr015.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR016', 'Deporte', 'Taladro 444', '1641.72', '2024-02-16', '0', 'España', 'pr016.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR017', 'Electrónica', 'Sudadera 375', '447.45', '2024-03-11', '1', 'Alemania', 'pr017.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR018', 'Deporte', 'Portátil 740', '725.64', '2024-05-07', '0', 'EE.UU.', 'pr018.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR019', 'Hogar', 'Zapatillas running 217', '358.72', '2023-02-24', '1', 'Italia', 'pr019.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR020', 'Confección', 'Sudadera 788', '132.16', '2024-03-20', '0', 'Italia', 'pr020.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR021', 'Confección', 'Zapatillas running 824', '930.83', '2023-05-03', '0', 'China', 'pr021.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR022', 'Confección', 'Portátil 761', '919.66', '2024-04-03', '1', 'Italia', 'pr022.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR023', 'Confección', 'Cafetera 528', '743.5', '2023-11-08', '0', 'China', 'pr023.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR024', 'Deporte', 'Auriculares 112', '1332.13', '2024-03-14', '0', 'EE.UU.', 'pr024.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR025', 'Hogar', 'Bicicleta 747', '423.73', '2024-03-07', '1', 'Italia', 'pr025.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR026', 'Ferretería', 'Televisor 624', '208.77', '2024-02-24', '0', 'España', 'pr026.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR027', 'Deporte', 'Zapatillas running 936', '1595.58', '2023-04-24', '0', 'Alemania', 'pr027.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR028', 'Ferretería', 'Cafetera 472', '338.44', '2024-03-10', '0', 'Alemania', 'pr028.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR029', 'Confección', 'Televisor 546', '1177.41', '2023-03-16', '0', 'Alemania', 'pr029.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR030', 'Ferretería', 'Bicicleta 611', '814.67', '2023-09-14', '0', 'Italia', 'pr030.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR031', 'Hogar', 'Taladro 640', '320.62', '2023-07-02', '0', 'Italia', 'pr031.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR032', 'Electrónica', 'Robot aspirador 655', '1367.06', '2024-02-04', '0', 'Italia', 'pr032.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR033', 'Hogar', 'Taladro 971', '531.53', '2023-02-10', '0', 'Italia', 'pr033.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR034', 'Hogar', 'Auriculares 615', '1621.24', '2023-02-28', '1', 'China', 'pr034.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR035', 'Ferretería', 'Auriculares 671', '1826.01', '2023-10-11', '0', 'Alemania', 'pr035.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR036', 'Hogar', 'Sudadera 929', '1113.69', '2023-03-28', '1', 'Alemania', 'pr036.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR037', 'Hogar', 'Taladro 818', '1662.18', '2024-03-20', '1', 'China', 'pr037.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR038', 'Hogar', 'Auriculares 115', '523.02', '2023-03-01', '1', 'España', 'pr038.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR039', 'Ferretería', 'Smartphone 141', '699.98', '2024-03-02', '0', 'Italia', 'pr039.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR040', 'Ferretería', 'Smartphone 895', '1815.56', '2024-01-15', '0', 'Japón', 'pr040.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR041', 'Ferretería', 'Zapatillas running 106', '1255.57', '2023-08-17', '0', 'EE.UU.', 'pr041.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR042', 'Electrónica', 'Zapatillas running 670', '1474.59', '2023-05-25', '1', 'Italia', 'pr042.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR043', 'Electrónica', 'Robot aspirador 613', '1570.3', '2023-06-01', '0', 'Italia', 'pr043.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR044', 'Ferretería', 'Cafetera 415', '1264.58', '2023-08-05', '0', 'Alemania', 'pr044.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR045', 'Confección', 'Portátil 358', '1151.53', '2023-10-11', '0', 'Japón', 'pr045.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR046', 'Hogar', 'Bicicleta 811', '546.04', '2023-06-14', '0', 'China', 'pr046.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR047', 'Confección', 'Bicicleta 125', '1333.62', '2024-02-13', '0', 'China', 'pr047.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR048', 'Electrónica', 'Auriculares 623', '335.24', '2023-03-12', '1', 'China', 'pr048.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR049', 'Hogar', 'Taladro 335', '1666.4', '2023-02-20', '1', 'España', 'pr049.jpg');
INSERT INTO `articulos` (`codigo_articulo`,`seccion`,`nombre_articulo`,`precio`,`fecha`,`importado`,`pais_origen`,`foto`) VALUES ('PR050', 'Electrónica', 'Robot aspirador 657', '63.44', '2023-12-05', '0', 'China', 'pr050.jpg');


DROP TABLE IF EXISTS `clientes`;
CREATE TABLE `clientes` (
  `codigoCliente` varchar(10) NOT NULL,
  `empresa` varchar(100) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `poblacion` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `responsable` varchar(100) DEFAULT NULL,
  `historial` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`codigoCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL001', 'Empresa 001', 'Calle F Nº157', 'Palma', '689376390', 'Sergio Sánchez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL002', 'Empresa 002', 'Calle D Nº158', 'Bilbao', '656389214', 'Pedro López', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL003', 'Empresa 003', 'Calle D Nº15', 'Murcia', '619370618', 'Luis Sánchez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL004', 'Empresa 004', 'Calle V Nº26', 'Zaragoza', '675122851', 'Ana López', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL005', 'Empresa 005', 'Calle A Nº136', 'Zaragoza', '631634817', 'Luis Rodríguez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL006', 'Empresa 006', 'Calle R Nº168', 'Palma', '794953371', 'María Fernández', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL007', 'Empresa 007', 'Calle U Nº48', 'Bilbao', '769703216', 'Ana López', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL008', 'Empresa 008', 'Calle S Nº38', 'Madrid', '621794657', 'María Pérez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL009', 'Empresa 009', 'Calle X Nº121', 'Valencia', '690185518', 'Carlos Gómez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL010', 'Empresa 010', 'Calle B Nº174', 'Madrid', '629452725', 'María Rodríguez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL011', 'Empresa 011', 'Calle L Nº127', 'Málaga', '776975582', 'Sergio Martínez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL012', 'Empresa 012', 'Calle H Nº90', 'Zaragoza', '721904120', 'Jorge Martínez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL013', 'Empresa 013', 'Calle X Nº6', 'Málaga', '783393453', 'Sara Sánchez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL014', 'Empresa 014', 'Calle Q Nº91', 'Valencia', '623552990', 'Pedro Rodríguez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL015', 'Empresa 015', 'Calle Q Nº114', 'Valencia', '785640357', 'Laura López', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL016', 'Empresa 016', 'Calle D Nº66', 'Bilbao', '767955948', 'Ana Díaz', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL017', 'Empresa 017', 'Calle B Nº158', 'Bilbao', '771270073', 'Laura González', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL018', 'Empresa 018', 'Calle E Nº74', 'Valencia', '670629430', 'Sara García', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL019', 'Empresa 019', 'Calle S Nº173', 'Zaragoza', '778546210', 'Jorge García', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL020', 'Empresa 020', 'Calle R Nº131', 'Bilbao', '678749227', 'Jorge Gómez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL021', 'Empresa 021', 'Calle K Nº82', 'Palma', '623106404', 'Sergio Rodríguez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL022', 'Empresa 022', 'Calle Y Nº16', 'Bilbao', '711663685', 'Sara Díaz', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL023', 'Empresa 023', 'Calle U Nº122', 'Barcelona', '637357845', 'Sergio Sánchez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL024', 'Empresa 024', 'Calle B Nº73', 'Valencia', '765509861', 'Lucía Pérez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL025', 'Empresa 025', 'Calle A Nº30', 'Valencia', '659279542', 'María García', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL026', 'Empresa 026', 'Calle S Nº6', 'Bilbao', '789564779', 'Ana Pérez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL027', 'Empresa 027', 'Calle L Nº23', 'Madrid', '686832769', 'Sergio Pérez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL028', 'Empresa 028', 'Calle T Nº162', 'Bilbao', '681460072', 'Lucía García', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL029', 'Empresa 029', 'Calle W Nº71', 'Madrid', '611877840', 'María López', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL030', 'Empresa 030', 'Calle Q Nº172', 'Bilbao', '723957650', 'Sara Díaz', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL031', 'Empresa 031', 'Calle U Nº193', 'Murcia', '798714945', 'Laura Martínez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL032', 'Empresa 032', 'Calle R Nº123', 'Bilbao', '763318288', 'Sara Sánchez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL033', 'Empresa 033', 'Calle G Nº13', 'Barcelona', '679633522', 'Laura Gómez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL034', 'Empresa 034', 'Calle O Nº149', 'Valencia', '638429827', 'Carlos Gómez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL035', 'Empresa 035', 'Calle K Nº76', 'Zaragoza', '792507044', 'Sergio Martínez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL036', 'Empresa 036', 'Calle S Nº164', 'Sevilla', '618275434', 'Jorge Gómez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL037', 'Empresa 037', 'Calle S Nº59', 'Palma', '656221616', 'Laura Pérez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL038', 'Empresa 038', 'Calle Y Nº184', 'Zaragoza', '693107158', 'Pedro Gómez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL039', 'Empresa 039', 'Calle J Nº39', 'Palma', '655679124', 'Laura Gómez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL040', 'Empresa 040', 'Calle A Nº154', 'Palma', '786837527', 'Luis González', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL041', 'Empresa 041', 'Calle P Nº128', 'Barcelona', '712718596', 'Laura Fernández', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL042', 'Empresa 042', 'Calle P Nº18', 'Granada', '625493095', 'Pedro García', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL043', 'Empresa 043', 'Calle S Nº33', 'Barcelona', '757506540', 'Jorge López', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL044', 'Empresa 044', 'Calle E Nº95', 'Málaga', '701955391', 'Laura García', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL045', 'Empresa 045', 'Calle P Nº2', 'Sevilla', '771680792', 'María Gómez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL046', 'Empresa 046', 'Calle W Nº45', 'Barcelona', '753323153', 'Pedro García', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL047', 'Empresa 047', 'Calle A Nº29', 'Málaga', '750218799', 'María García', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL048', 'Empresa 048', 'Calle F Nº116', 'Palma', '608113148', 'Laura González', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL049', 'Empresa 049', 'Calle Q Nº29', 'Barcelona', '601270939', 'Sergio Martínez', 'Cliente desde 2024');
INSERT INTO `clientes` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('CL050', 'Empresa 050', 'Calle K Nº125', 'Palma', '756700194', 'María Pérez', 'Cliente desde 2024');


DROP TABLE IF EXISTS `clientesVip`;
CREATE TABLE `clientesVip` (
  `codigoCliente` varchar(10) NOT NULL,
  `empresa` varchar(100) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `poblacion` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `responsable` varchar(100) DEFAULT NULL,
  `historial` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`codigoCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP001', 'Empresa 001', 'Calle T Nº199', 'Madrid', '731556290', 'Luis López', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP002', 'Empresa 002', 'Calle O Nº191', 'Barcelona', '643736268', 'Pedro Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP003', 'Empresa 003', 'Calle Z Nº127', 'Málaga', '726351985', 'Pedro Martínez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP004', 'Empresa 004', 'Calle D Nº167', 'Bilbao', '664597659', 'Pedro Martínez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP005', 'Empresa 005', 'Calle G Nº139', 'Barcelona', '798592975', 'Laura Martínez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP006', 'Empresa 006', 'Calle O Nº40', 'Valencia', '748989975', 'Sara Martínez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP007', 'Empresa 007', 'Calle E Nº133', 'Madrid', '658454940', 'Luis Martínez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP008', 'Empresa 008', 'Calle S Nº64', 'Murcia', '702495500', 'Sergio Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP009', 'Empresa 009', 'Calle Q Nº84', 'Málaga', '706546459', 'Pedro Díaz', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP010', 'Empresa 010', 'Calle U Nº168', 'Murcia', '742158210', 'Jorge Díaz', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP011', 'Empresa 011', 'Calle F Nº151', 'Bilbao', '630427421', 'Pedro Rodríguez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP012', 'Empresa 012', 'Calle F Nº115', 'Zaragoza', '771775237', 'Sergio López', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP013', 'Empresa 013', 'Calle K Nº14', 'Murcia', '616575839', 'Lucía García', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP014', 'Empresa 014', 'Calle Z Nº116', 'Valencia', '707397910', 'Ana Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP015', 'Empresa 015', 'Calle B Nº12', 'Murcia', '797688667', 'Laura Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP016', 'Empresa 016', 'Calle X Nº116', 'Granada', '781667195', 'Carlos Gómez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP017', 'Empresa 017', 'Calle T Nº70', 'Madrid', '649850910', 'Luis Gómez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP018', 'Empresa 018', 'Calle F Nº159', 'Barcelona', '743905353', 'Pedro Pérez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP019', 'Empresa 019', 'Calle P Nº38', 'Sevilla', '652828887', 'Ana Sánchez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP020', 'Empresa 020', 'Calle J Nº29', 'Madrid', '636846384', 'Sergio López', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP021', 'Empresa 021', 'Calle E Nº176', 'Granada', '657966148', 'Pedro Sánchez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP022', 'Empresa 022', 'Calle Z Nº112', 'Madrid', '765140068', 'Sergio Martínez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP023', 'Empresa 023', 'Calle L Nº11', 'Valencia', '696644870', 'Lucía Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP024', 'Empresa 024', 'Calle X Nº52', 'Murcia', '727308349', 'María López', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP025', 'Empresa 025', 'Calle T Nº109', 'Granada', '777382731', 'Laura Díaz', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP026', 'Empresa 026', 'Calle W Nº106', 'Valencia', '697140700', 'Luis Martínez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP027', 'Empresa 027', 'Calle B Nº184', 'Palma', '753556759', 'Sara Díaz', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP028', 'Empresa 028', 'Calle O Nº22', 'Granada', '707398228', 'Sara Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP029', 'Empresa 029', 'Calle I Nº134', 'Bilbao', '608132758', 'Pedro Díaz', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP030', 'Empresa 030', 'Calle A Nº185', 'Bilbao', '714949445', 'Luis Rodríguez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP031', 'Empresa 031', 'Calle P Nº49', 'Murcia', '702476661', 'Sergio Díaz', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP032', 'Empresa 032', 'Calle Z Nº126', 'Granada', '735994404', 'Laura García', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP033', 'Empresa 033', 'Calle M Nº174', 'Sevilla', '715734043', 'María Rodríguez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP034', 'Empresa 034', 'Calle T Nº40', 'Bilbao', '668890651', 'Carlos Gómez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP035', 'Empresa 035', 'Calle Y Nº18', 'Murcia', '741161502', 'Lucía Pérez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP036', 'Empresa 036', 'Calle A Nº189', 'Granada', '791988470', 'Ana Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP037', 'Empresa 037', 'Calle L Nº137', 'Palma', '616540525', 'Sara Gómez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP038', 'Empresa 038', 'Calle D Nº16', 'Zaragoza', '714922141', 'Sergio Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP039', 'Empresa 039', 'Calle N Nº77', 'Barcelona', '661392292', 'Luis López', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP040', 'Empresa 040', 'Calle W Nº134', 'Bilbao', '658849181', 'Lucía Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP041', 'Empresa 041', 'Calle O Nº116', 'Granada', '664434416', 'Pedro Martínez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP042', 'Empresa 042', 'Calle M Nº84', 'Murcia', '775831915', 'Sergio Fernández', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP043', 'Empresa 043', 'Calle Z Nº74', 'Madrid', '689845512', 'María Rodríguez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP044', 'Empresa 044', 'Calle Z Nº69', 'Murcia', '648670273', 'Pedro García', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP045', 'Empresa 045', 'Calle Z Nº162', 'Murcia', '713441486', 'Laura Sánchez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP046', 'Empresa 046', 'Calle R Nº74', 'Madrid', '652537647', 'Sara López', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP047', 'Empresa 047', 'Calle H Nº81', 'Sevilla', '768935296', 'Jorge López', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP048', 'Empresa 048', 'Calle L Nº166', 'Granada', '734528473', 'Jorge Rodríguez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP049', 'Empresa 049', 'Calle Y Nº175', 'Sevilla', '692885680', 'Pedro Pérez', 'Cliente VIP desde 2024');
INSERT INTO `clientesVip` (`codigoCliente`,`empresa`,`direccion`,`poblacion`,`telefono`,`responsable`,`historial`) VALUES ('VIP050', 'Empresa 050', 'Calle P Nº190', 'Murcia', '725490761', 'Ana López', 'Cliente VIP desde 2024');


DROP TABLE IF EXISTS `pedidos`;
CREATE TABLE `pedidos` (
  `id_pedido` int(11) NOT NULL,
  `codigoCliente` varchar(10) NOT NULL,
  `codigo_articulo` varchar(10) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT 1,
  `fecha_pedido` date NOT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `fk_pedidos_clientes` (`codigoCliente`),
  KEY `fk_pedidos_articulos` (`codigo_articulo`),
  CONSTRAINT `fk_pedidos_clientes` FOREIGN KEY (`codigoCliente`) REFERENCES `clientes` (`codigoCliente`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_pedidos_articulos` FOREIGN KEY (`codigo_articulo`) REFERENCES `articulos` (`codigo_articulo`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('1', 'CL050', 'PR014', '7', '2024-12-14');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('2', 'CL038', 'PR012', '2', '2024-12-09');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('3', 'CL008', 'PR025', '10', '2025-06-12');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('4', 'CL040', 'PR001', '9', '2024-08-27');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('5', 'CL024', 'PR026', '6', '2025-01-03');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('6', 'CL010', 'PR020', '8', '2025-09-09');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('7', 'CL034', 'PR028', '5', '2025-08-18');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('8', 'CL045', 'PR003', '6', '2025-05-11');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('9', 'CL031', 'PR050', '2', '2024-04-30');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('10', 'CL024', 'PR048', '6', '2024-03-14');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('11', 'CL018', 'PR008', '2', '2025-06-10');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('12', 'CL042', 'PR033', '5', '2024-07-07');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('13', 'CL033', 'PR033', '9', '2025-09-04');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('14', 'CL036', 'PR042', '1', '2025-11-03');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('15', 'CL038', 'PR031', '1', '2024-10-01');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('16', 'CL015', 'PR037', '9', '2025-08-28');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('17', 'CL009', 'PR007', '6', '2024-09-27');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('18', 'CL025', 'PR018', '10', '2024-11-30');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('19', 'CL026', 'PR010', '6', '2025-11-30');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('20', 'CL006', 'PR042', '6', '2024-11-19');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('21', 'CL024', 'PR005', '8', '2024-08-03');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('22', 'CL018', 'PR017', '8', '2025-03-21');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('23', 'CL015', 'PR002', '6', '2024-05-17');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('24', 'CL036', 'PR030', '2', '2024-02-05');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('25', 'CL029', 'PR002', '1', '2025-03-16');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('26', 'CL011', 'PR003', '9', '2024-08-22');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('27', 'CL015', 'PR008', '1', '2024-08-21');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('28', 'CL008', 'PR002', '9', '2024-02-19');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('29', 'CL001', 'PR002', '2', '2024-02-12');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('30', 'CL036', 'PR044', '5', '2025-10-26');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('31', 'CL016', 'PR015', '6', '2025-09-10');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('32', 'CL025', 'PR043', '8', '2025-11-26');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('33', 'CL015', 'PR047', '2', '2024-02-06');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('34', 'CL022', 'PR008', '8', '2025-06-21');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('35', 'CL013', 'PR010', '2', '2025-06-16');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('36', 'CL010', 'PR036', '9', '2025-05-15');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('37', 'CL028', 'PR004', '8', '2024-12-15');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('38', 'CL049', 'PR004', '9', '2025-12-29');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('39', 'CL047', 'PR038', '1', '2024-11-09');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('40', 'CL030', 'PR022', '1', '2025-10-15');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('41', 'CL018', 'PR049', '1', '2024-05-23');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('42', 'CL029', 'PR032', '8', '2025-05-05');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('43', 'CL023', 'PR012', '4', '2025-05-14');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('44', 'CL050', 'PR018', '1', '2024-11-24');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('45', 'CL014', 'PR014', '2', '2025-06-08');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('46', 'CL033', 'PR014', '3', '2025-05-17');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('47', 'CL017', 'PR022', '5', '2024-10-28');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('48', 'CL014', 'PR015', '4', '2025-10-31');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('49', 'CL047', 'PR037', '4', '2025-05-03');
INSERT INTO `pedidos` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('50', 'CL016', 'PR041', '2', '2024-10-10');


DROP TABLE IF EXISTS `pedidosVip`;
CREATE TABLE `pedidosVip` (
  `id_pedido` int(11) NOT NULL,
  `codigoCliente` varchar(10) NOT NULL,
  `codigo_articulo` varchar(10) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT 1,
  `fecha_pedido` date NOT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `fk_pedidosVip_clientesVip` (`codigoCliente`),
  KEY `fk_pedidosVip_articulos` (`codigo_articulo`),
  CONSTRAINT `fk_pedidosVip_clientesVip` FOREIGN KEY (`codigoCliente`) REFERENCES `clientesVip` (`codigoCliente`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_pedidosVip_articulos` FOREIGN KEY (`codigo_articulo`) REFERENCES `articulos` (`codigo_articulo`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('1', 'VIP020', 'PR008', '5', '2025-05-12');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('2', 'VIP046', 'PR015', '8', '2024-01-17');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('3', 'VIP016', 'PR005', '8', '2024-01-04');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('4', 'VIP030', 'PR038', '10', '2025-09-11');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('5', 'VIP014', 'PR023', '8', '2025-04-06');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('6', 'VIP033', 'PR015', '8', '2024-04-04');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('7', 'VIP006', 'PR031', '4', '2025-11-09');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('8', 'VIP023', 'PR041', '10', '2025-06-25');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('9', 'VIP030', 'PR036', '5', '2024-05-10');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('10', 'VIP012', 'PR005', '1', '2025-05-18');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('11', 'VIP031', 'PR001', '10', '2024-06-08');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('12', 'VIP032', 'PR030', '6', '2024-06-19');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('13', 'VIP041', 'PR008', '9', '2024-02-01');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('14', 'VIP022', 'PR003', '6', '2025-03-20');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('15', 'VIP034', 'PR022', '2', '2025-04-16');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('16', 'VIP030', 'PR042', '6', '2024-03-23');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('17', 'VIP024', 'PR047', '6', '2025-06-30');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('18', 'VIP016', 'PR038', '4', '2025-09-17');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('19', 'VIP009', 'PR005', '3', '2024-03-13');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('20', 'VIP028', 'PR011', '7', '2025-12-19');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('21', 'VIP011', 'PR037', '7', '2025-05-04');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('22', 'VIP010', 'PR013', '3', '2025-04-29');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('23', 'VIP045', 'PR008', '9', '2025-03-03');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('24', 'VIP040', 'PR006', '10', '2025-10-06');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('25', 'VIP029', 'PR049', '10', '2025-09-08');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('26', 'VIP024', 'PR040', '5', '2025-07-31');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('27', 'VIP007', 'PR050', '3', '2024-09-02');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('28', 'VIP026', 'PR008', '7', '2025-07-06');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('29', 'VIP038', 'PR034', '10', '2024-03-16');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('30', 'VIP047', 'PR029', '9', '2024-09-24');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('31', 'VIP046', 'PR023', '1', '2024-04-27');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('32', 'VIP009', 'PR017', '10', '2025-09-06');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('33', 'VIP032', 'PR036', '2', '2025-05-28');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('34', 'VIP018', 'PR040', '5', '2025-06-23');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('35', 'VIP014', 'PR046', '6', '2024-07-15');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('36', 'VIP015', 'PR034', '4', '2025-09-29');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('37', 'VIP046', 'PR047', '10', '2025-07-08');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('38', 'VIP035', 'PR004', '7', '2025-11-30');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('39', 'VIP042', 'PR025', '3', '2024-12-15');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('40', 'VIP028', 'PR043', '6', '2024-04-01');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('41', 'VIP028', 'PR043', '4', '2025-02-13');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('42', 'VIP023', 'PR031', '2', '2024-08-29');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('43', 'VIP014', 'PR018', '8', '2024-12-21');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('44', 'VIP024', 'PR027', '9', '2025-08-09');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('45', 'VIP042', 'PR049', '10', '2025-04-21');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('46', 'VIP013', 'PR003', '4', '2025-02-24');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('47', 'VIP017', 'PR033', '7', '2024-01-27');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('48', 'VIP013', 'PR036', '7', '2024-10-12');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('49', 'VIP039', 'PR005', '7', '2024-11-18');
INSERT INTO `pedidosVip` (`id_pedido`,`codigoCliente`,`codigo_articulo`,`cantidad`,`fecha_pedido`) VALUES ('50', 'VIP022', 'PR046', '7', '2025-11-20');