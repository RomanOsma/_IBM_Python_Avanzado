(() => {

    // ***************************
    //     GENERICS
    // ***************************


    // Desarrolla una función genérica que tome dos arreglos de elementos del mismo tipo 
    // y los concatene en un nuevo arreglo. 
    // La función debe poder trabajar con cualquier tipo de elementos.


    function concatenarArreglos<T>(arreglo1: T[], arreglo2: T[]): T[] {
        return arreglo1.concat(arreglo2);
    }

    console.log(concatenarArreglos([1, 2, 3], [4, 5, 6])); // [1, 2, 3, 4, 5, 6]
    console.log(concatenarArreglos(["a", "b"], ["c", "d", "e"])); // ["a", "b", "c", "d", "e"]

})()