(() => {

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
    class Persona {
        constructor(public nombre: string, public edad: number) { }
    }

    // Interface para empleados
    interface Empleado {
        salario: number;
        asignarSalario(salario: number): void;
    }

    // Interface para estudiantes
    interface Estudiante {
        curso: string;
        inscribirCurso(curso: string): void;
    }

    // Clase para profesores que implementa la interface Empleado
    class Profesor extends Persona implements Empleado {
        salario: number;

        constructor(nombre: string, edad: number, salario: number) {
            super(nombre, edad);
            this.salario = salario;
        }

        asignarSalario(salario: number): void {
            this.salario = salario;
        }
    }

    // Clase para alumnos que implementa la interface Estudiante
    class Alumno extends Persona implements Estudiante {
        curso: string;

        constructor(nombre: string, edad: number, curso: string) {
            super(nombre, edad);
            this.curso = curso;
        }

        inscribirCurso(curso: string): void {
            this.curso = curso;
        }
    }

    // Demostración de uso
    let profesor = new Profesor("Ana", 40, 3000);
    console.log(`El salario de ${profesor.nombre} es ${profesor.salario}`);

    profesor.asignarSalario(3500);
    console.log(`Nuevo salario de ${profesor.nombre}: ${profesor.salario}`);

    let alumno = new Alumno("Luis", 20, "Matemáticas");
    console.log(`${alumno.nombre} está inscrito en el curso de ${alumno.curso}`);

    alumno.inscribirCurso("Física");
    console.log(`Nuevo curso de ${alumno.nombre}: ${alumno.curso}`);


})()