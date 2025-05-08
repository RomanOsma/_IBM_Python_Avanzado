(() => {

    // **********************************************
    //     POO
    // **********************************************


    // Desarrolla una clase Estudiante que almacene el nombre del estudiante y una lista 
    // de calificaciones. 
    // Las calificaciones deben ser accesibles solo dentro de la clase y modificables 
    // solo a través de un método agregarCalificacion(). 
    // Implementa métodos para calcular el promedio de calificaciones y determinar 
    // si el estudiante aprueba o no (promedio >= 6).

    class Estudiante {
        private nombre: string;
        private calificaciones: number[];

        constructor(nombre: string) {
            this.nombre = nombre;
            this.calificaciones = [];
        }

        public agregarCalificacion(calificacion: number): void {
            this.calificaciones.push(calificacion);
        }

        public calcularPromedio(): number {
            const suma = this.calificaciones.reduce((acumulado, actual) => acumulado + actual, 0);
            return suma / this.calificaciones.length;
        }

        public aprueba(): boolean {
            return this.calcularPromedio() >= 6;
        }
    }

    // Test de la clase
    const estudiante = new Estudiante("Juan");
    estudiante.agregarCalificacion(5);
    estudiante.agregarCalificacion(7);
    estudiante.agregarCalificacion(6);
    console.log(estudiante.calcularPromedio()); // Debería mostrar el promedio de Juan
    console.log(estudiante.aprueba()); // Debería mostrar true si Juan aprueba

})()