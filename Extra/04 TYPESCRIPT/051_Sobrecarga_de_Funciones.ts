(() => {

    // **********************************************
    //     SOBRECARGA DE FUNCIONES
    // **********************************************

    // Crea una función calcular que pueda sumar dos números o multiplicar dos números, 
    // basada en un argumento de tipo string que indica la operación.


    function calcular(operacion: 'suma', a: number, b: number): number;
    function calcular(operacion: 'multiplicacion', a: number, b: number): number;
    function calcular(operacion: string, a: number, b: number): number {
        if (operacion === 'suma') return a + b;
        if (operacion === 'multiplicacion') return a * b;
        throw new Error('Operación no soportada');
    }

    console.log(calcular('suma', 5, 7)); // 12
    console.log(calcular('multiplicacion', 3, 4)); // 12

})()