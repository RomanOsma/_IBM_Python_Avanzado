(() => {

    // ****************************************************************************
    //     POO - CLase con atributos, métodos, constructor e instancias de clase
    // ****************************************************************************


    class Estudiante {
        nombre: string;
        grado: string;
        notas: number[];

        constructor(nombre: string, grado: string) {
            this.nombre = nombre;
            this.grado = grado;
            this.notas = [];
        }

        agregarNota(nota: number): void {
            this.notas.push(nota);
        }

        calcularPromedio(): number {
            const suma = this.notas.reduce((acum, actual) => acum + actual, 0);
            return suma / this.notas.length;
        }
    }

    // Instancias de la clase Estudiante
    const estudiante1 = new Estudiante("Marta", "10mo");
    const estudiante2 = new Estudiante("Jorge", "11vo");

    estudiante1.agregarNota(8);
    estudiante1.agregarNota(9);
    console.log(estudiante1.calcularPromedio()); // Muestra el promedio de notas de Marta

    estudiante2.agregarNota(7);
    estudiante2.agregarNota(6);
    estudiante2.agregarNota(8);
    console.log(estudiante2.calcularPromedio()); // Muestra el promedio de notas de Jorge


})()