(() => {

    // **********************************************
    //     POO - Herencia - Sobrecarga de métodos
    // **********************************************

      // Crea una clase CalculadoraBasica que tenga un método operar sobrecargado para 
    // realizar operaciones básicas:

    // Sumar dos números.
    // Restar dos números.


    class CalculadoraBasica {
        operar(a: number, b: number, operacion: 'suma'): number;
        operar(a: number, b: number, operacion: 'resta'): number;

        operar(a: number, b: number, operacion: 'suma' | 'resta'): number {
            return operacion === 'suma' ? a + b : a - b;
        }
    }

    const calculadora = new CalculadoraBasica();
    console.log(calculadora.operar(5, 3, 'suma')); // 8
    console.log(calculadora.operar(5, 3, 'resta')); // 2  
    
})()