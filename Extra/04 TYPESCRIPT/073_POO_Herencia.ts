(() => {

    // **********************************************
    //     POO - Herencia
    // **********************************************

    // Implementa una clase base Persona con propiedades nombre y edad. 
    // De esta clase base, deriva dos clases: Profesor y Estudiante. 
    // La clase Profesor debe añadir una propiedad materia que enseña, mientras que 
    // Estudiante debe añadir una propiedad carrera en la que está inscrito. 
    // Implementa un método mostrarInformacion() en todas las clases para imprimir sus propiedades.


    class Persona {
        nombre: string;
        edad: number;

        constructor(nombre: string, edad: number) {
            this.nombre = nombre;
            this.edad = edad;
        }

        mostrarInformacion(): void {
            console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
        }
    }

    class Profesor extends Persona {
        materia: string;

        constructor(nombre: string, edad: number, materia: string) {
            super(nombre, edad);
            this.materia = materia;
        }

        mostrarInformacion(): void {
            super.mostrarInformacion();
            console.log(`Materia: ${this.materia}`);
        }
    }

    class Estudiante extends Persona {
        carrera: string;

        constructor(nombre: string, edad: number, carrera: string) {
            super(nombre, edad);
            this.carrera = carrera;
        }

        mostrarInformacion(): void {
            super.mostrarInformacion();
            console.log(`Carrera: ${this.carrera}`);
        }
    }

    // Instancias de prueba
    const profesor = new Profesor("Carlos", 45, "Matemáticas");
    profesor.mostrarInformacion();

    const estudiante = new Estudiante("María", 20, "Ingeniería de Sistemas");
    estudiante.mostrarInformacion();

})()