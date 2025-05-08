# Curso Completo de Python con MySQL

## Descripción General

Este repositorio contiene un curso completo para aprender a interactuar con bases de datos MySQL utilizando Python. El curso abarca desde los conceptos básicos de SQL y la configuración de MySQL hasta temas avanzados como el uso de pools de conexiones, el patrón DAO (Data Access Object), transacciones y procedimientos almacenados. Además, se incluye una aplicación completa de gestión de clientes para un gimnasio (Zona Fit).

## Contenidos del Curso

1.  **Fundamentos de MySQL**:

    *   Instalación y configuración de MySQL.
    *   Creación de bases de datos y tablas.
    *   Operaciones CRUD básicas en MySQL.
2.  **Conexión Python-MySQL**:

    *   Instalación del conector MySQL para Python (`mysql-connector-python`).
    *   Establecimiento de conexiones a la base de datos.
    *   Ejecución de consultas SQL desde Python.
    *   Manejo de errores y excepciones.
    *   Uso de parámetros en consultas SQL para prevenir inyección SQL.
3.  **Operaciones CRUD en Python**:

    *   Implementación de operaciones CRUD (Create, Read, Update, Delete) utilizando Python y MySQL.
    *   Uso de parámetros para ejecutar consultas de manera segura.
    *   Manejo de transacciones para garantizar la integridad de los datos.
4.  **Patrones de Diseño para Acceso a Datos**:

    *   Pool de Conexiones: concepto, implementación y beneficios para el rendimiento.
    *   Patrón DAO (Data Access Object): separación de responsabilidades y abstracción del acceso a datos.
    *   Implementación de un pool de conexiones para mejorar la eficiencia.
    *   Mapeo Objeto-Relacional básico.
5.  **Temas Avanzados**:

    *   Transacciones en MySQL: cómo asegurar la integridad de los datos.
    *   Procedimientos almacenados: creación y uso desde Python.
    *   Manejo de cursores y resultados de consultas.
6.  **Desarrollo de una Aplicación Completa**:

    *   Desarrollo de una aplicación de gestión para un gimnasio (Zona Fit).
    *   Implementación de un menú interactivo por consola.
    *   Operaciones CRUD completas con manejo de errores.
    *   Ejemplos de procedimientos almacenados y transacciones.

## Estructura del Código

El archivo principal `BaseDatos.py` está organizado en las siguientes secciones:

1.  **Preliminares y Configuración**:

    *   Importación de las bibliotecas necesarias (`mysql.connector`, `pooling`, `Error`).
    *   Definición de tipos (`List`, `Dict`, `Any`, `Tuple`, `Optional`) para mejorar la legibilidad del código.
2.  **Fundamentos de MySQL**:

    *   Explicación de las operaciones CRUD básicas en SQL (CREATE, READ, UPDATE, DELETE).
    *   Script SQL para crear las bases de datos (`personas_db` y `zona_fit_db`) y las tablas necesarias.
3.  **Conexión Python-MySQL**:

    *   Ejemplo básico de conexión a MySQL y consulta SELECT (`ejemplo_conexion_basica`).
    *   Función genérica para crear conexiones reutilizables (`crear_conexion`).
    *   Función para cerrar conexiones (`cerrar_conexion`).
4.  **Operaciones CRUD en Python**:

    *   Ejemplos de inserción (`ejemplo_insertar`), actualización (`ejemplo_actualizar`) y eliminación (`ejemplo_eliminar`) de datos en la base de datos `personas_db`.
    *   Función para seleccionar todas las personas de la base de datos (`select_personas`).
    *   Implementación de operaciones CRUD básicas y avanzadas con manejo de errores y parámetros.
5.  **Pool de Conexiones**:

    *   Implementación de la clase `Conexion` para gestionar un pool de conexiones a la base de datos `zona_fit_db`.
    *   Métodos para obtener (`obtener_pool`, `obtener_conexion`) y liberar (`liberar_conexion`) conexiones del pool.
6.  **Patrón DAO (Data Access Object)**:

    *   Definición de la clase `Cliente` para representar la entidad cliente.
    *   Implementación de la clase `ClienteDAO` para gestionar los registros de clientes en la base de datos.
    *   Métodos para seleccionar (`seleccionar`), insertar (`insertar`), actualizar (`actualizar`) y eliminar (`eliminar`) clientes.
7.  **Temas Avanzados**:

    *   Ejemplo de uso de transacciones (`ejemplo_transacciones`) para asegurar la integridad de los datos.
    *   Ejemplo de uso de procedimientos almacenados (`ejemplo_procedimiento_almacenado`) para ejecutar lógica en el servidor de la base de datos.
8.  **Aplicación Zona Fit (Gestión de Clientes)**:

    *   Implementación de un menú interactivo para gestionar clientes desde la consola (`main`).
    *   Opciones para listar, agregar, modificar y eliminar clientes.
9.  **Funciones de Soporte**:

    *   Funciones adicionales para imprimir resultados de consultas (`imprimir_resultados`).
    *   Funciones para generar datos de prueba (`generar_datos_prueba`).
10. **Bloque Principal**:

    *   Ejemplos de cómo ejecutar las diferentes funciones y métodos del curso.
    *   Llamada a la función `main()` para iniciar la aplicación de gestión de clientes.

## Requisitos

Antes de ejecutar los ejemplos, asegúrate de tener lo siguiente:

*   Python 3.6 o superior.
*   MySQL Server instalado y en ejecución.
*   La biblioteca `mysql-connector-python` instalada. Puedes instalarla con el siguiente comando:
pip install mysql-connector-python


## Configuración

1.  **Creación de las bases de datos**:

Crea las bases de datos `personas_db` y `zona_fit_db` en tu servidor MySQL. Puedes utilizar el siguiente script SQL:

-- Base de datos para ejemplos básicos
CREATE DATABASE IF NOT EXISTS personas_db;
USE personas_db;

CREATE TABLE IF NOT EXISTS personas (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(50) NOT NULL,
edad INT
);

-- Base de datos para la aplicación Zona Fit
CREATE DATABASE IF NOT EXISTS zona_fit_db;
USE zona_fit_db;

CREATE TABLE IF NOT EXISTS cliente (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(50) NOT NULL,
membresia VARCHAR(20) NOT NULL
);


2.  **Configuración de las credenciales**:

Asegúrate de configurar las credenciales de la base de datos en el archivo `BaseDatos.py`. Las credenciales se utilizan para establecer la conexión a la base de datos. Debes modificar los valores de `host`, `user`, `password` y `database` para que coincidan con tu configuración local.

Credenciales de la base de datos
DATABASE = 'zona_fit_db' o 'personas_db'
USERNAME = 'root'
PASSWORD = 'Aroman1984' # O 'admin', dependiendo de la base de datos
DB_PORT = '3306'
HOST = 'localhost'


**Nota importante**: Verifica que las contraseñas para las bases de datos `personas_db` y `zona_fit_db` sean correctas. En algunos ejemplos, se usa `'admin'` y en otros `'Aroman1984'`.

## Cómo Utilizar el Código

1.  **Descargar el repositorio**:

Descarga el archivo `BaseDatos.py` desde este repositorio.

2.  **Configurar las credenciales**:

Modifica las credenciales de la base de datos en el archivo `BaseDatos.py` para que coincidan con tu configuración local.

3.  **Ejecutar el código**:

Ejecuta el archivo `BaseDatos.py` desde la terminal utilizando el siguiente comando:


4.  **Interactuar con el menú**:

Sigue las instrucciones del menú para interactuar con la aplicación de gestión de clientes. Puedes listar, agregar, modificar y eliminar clientes desde la consola.

## Ejemplos de Uso

A continuación, se muestran algunos ejemplos de cómo utilizar las diferentes funciones y métodos del curso:

*   **Ejecutar el ejemplo de conexión básica**:

from BaseDatos import Cliente, ClienteDAO # Importa las clases

cliente = Cliente(nombre='Nuevo', apellido='Cliente', membresia='Básica')
clientes_insertados = ClienteDAO.insertar(cliente)
print(f'Clientes insertados: {clientes_insertados}')


*   **Ejecutar el ejemplo de transacciones**:


## Contribución

Siéntete libre de contribuir a este repositorio. Puedes agregar nuevos ejemplos, corregir errores o mejorar la documentación. Para contribuir, sigue los siguientes pasos:

1.  Haz un fork del repositorio.
2.  Crea una rama con tus cambios.
3.  Envía un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más información.

