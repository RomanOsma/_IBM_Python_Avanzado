(() => {

    // **********************************************
    //     POO - Interfaces
    // **********************************************


    // Crea una interfaz OperacionesMatematicas que defina métodos para las 
    // operaciones básicas de matemáticas: suma, resta, multiplicación y división. 
    // Cada método debe tomar dos argumentos numéricos y retornar un número. 
    // Desarrolla una clase Calculadora que implemente esta interfaz y realice 
    // las operaciones definidas.

    interface OperacionesMatematicas {
        suma(a: number, b: number): number;
        resta(a: number, b: number): number;
        multiplicacion(a: number, b: number): number;
        division(a: number, b: number): number;
    }

    class Calculadora implements OperacionesMatematicas {
        suma(a: number, b: number): number {
            return a + b;
        }

        resta(a: number, b: number): number {
            return a - b;
        }

        multiplicacion(a: number, b: number): number {
            return a * b;
        }

        division(a: number, b: number): number {
            if (b === 0) {
                throw new Error("No se puede dividir por cero.");
            }
            return a / b;
        }
    }

    const miCalculadora = new Calculadora();
    console.log(miCalculadora.suma(10, 5));
    console.log(miCalculadora.resta(10, 5));
    console.log(miCalculadora.multiplicacion(10, 5));
    console.log(miCalculadora.division(10, 5));

})()