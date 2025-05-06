(() => {

    // ***************************
    //     GENERICS
    // ***************************


    // crear y retornar un array que contenga elementos del mismo tipo que los 
    // argumentos proporcionados a la función

    function crearPares<T>(x: T, y: T): T[] {
        return [x, y];
    }

    let parNumerico = crearPares(1, 2); // Inferido como 'number[]'
    let parDeCadenas = crearPares("hola", "mundo"); // Inferido como 'string[]'

    console.log(parNumerico); // Muestra: [1, 2]
    console.log(parDeCadenas); // Muestra: ["hola", "mundo"]

})()