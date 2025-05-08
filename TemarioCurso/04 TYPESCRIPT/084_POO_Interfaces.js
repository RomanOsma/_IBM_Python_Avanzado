var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
(function () {
    // **********************************************
    //     POO - Interfaces
    // **********************************************
    // Se desea modelar un sistema para una escuela que pueda manejar tanto a empleados 
    // como a estudiantes. 
    // Para ello, se requiere lo siguiente:
    // Una clase base Persona que contenga propiedades comunes como nombre y edad.
    // Dos interfaces, Empleado y Estudiante, que definan comportamientos específicos:
    // Empleado debe tener una propiedad salario y un método asignarSalario para establecer 
    // el salario del empleado.
    // Estudiante debe tener una propiedad curso y un método inscribirCurso para inscribir 
    // al estudiante en un nuevo curso.
    // Dos clases derivadas de Persona que implementen las interfaces respectivas:
    // Profesor, que implementa la interfaz Empleado, debe poder manejar su salario.
    // Alumno, que implementa la interfaz Estudiante, debe poder inscribirse en cursos.
    // Objetivo: Implementar la clase base, las interfaces, y las clases derivadas según 
    // los requerimientos, y demostrar su uso mediante la creación de instancias y la llamada 
    // a sus métodos.
    // Clase base
    var Persona = /** @class */ (function () {
        function Persona(nombre, edad) {
            this.nombre = nombre;
            this.edad = edad;
        }
        return Persona;
    }());
    // Clase para profesores que implementa la interface Empleado
    var Profesor = /** @class */ (function (_super) {
        __extends(Profesor, _super);
        function Profesor(nombre, edad, salario) {
            var _this = _super.call(this, nombre, edad) || this;
            _this.salario = salario;
            return _this;
        }
        Profesor.prototype.asignarSalario = function (salario) {
            this.salario = salario;
        };
        return Profesor;
    }(Persona));
    // Clase para alumnos que implementa la interface Estudiante
    var Alumno = /** @class */ (function (_super) {
        __extends(Alumno, _super);
        function Alumno(nombre, edad, curso) {
            var _this = _super.call(this, nombre, edad) || this;
            _this.curso = curso;
            return _this;
        }
        Alumno.prototype.inscribirCurso = function (curso) {
            this.curso = curso;
        };
        return Alumno;
    }(Persona));
    // Demostración de uso
    var profesor = new Profesor("Ana", 40, 3000);
    console.log("El salario de ".concat(profesor.nombre, " es ").concat(profesor.salario));
    profesor.asignarSalario(3500);
    console.log("Nuevo salario de ".concat(profesor.nombre, ": ").concat(profesor.salario));
    var alumno = new Alumno("Luis", 20, "Matemáticas");
    console.log("".concat(alumno.nombre, " est\u00E1 inscrito en el curso de ").concat(alumno.curso));
    alumno.inscribirCurso("Física");
    console.log("Nuevo curso de ".concat(alumno.nombre, ": ").concat(alumno.curso));
})();
