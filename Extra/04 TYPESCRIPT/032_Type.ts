(() => {

    // ***************************
    //     TYPE
    // ***************************

    // Crea un tipo personalizado OperacionMatematica para una función que tome 
    // dos números (a y b) y retorne un número. 
    // Implementa una función sumar que se ajuste a este tipo.


    type OperacionMatematica = (a: number, b: number) => number;

    const sumar: OperacionMatematica = (a, b) => {
        return a + b;
    };

    console.log(sumar(5, 3)); // Debería mostrar 8

})()