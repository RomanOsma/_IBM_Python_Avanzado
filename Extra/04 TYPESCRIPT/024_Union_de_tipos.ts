(() => {

    // ***************************
    //     UNIÓN DE TIPOS
    // ***************************

    // Define un tipo NumerosOStrings que acepte un arreglo de números o de strings, 
    // pero no una mezcla de ambos. Luego, crea un arreglo de este tipo.


    type NumerosOStrings = number[] | string[];

    const miArreglo: NumerosOStrings = ["Hola", "Mundo"];
    // const miArreglo: NumerosOStrings = [1, 2, 3]; // También válido
    // const miArreglo: NumerosOStrings = [1, "dos", 3]; // Esto causaría un error

    console.log(miArreglo);

})()