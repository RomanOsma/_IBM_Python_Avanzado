(() => {

    // ***************************
    //     GENERICS
    // ***************************


    // Crea una función genérica que invierta los elementos de un arreglo y devuelva ese 
    // arreglo invertido. La función debe poder trabajar con arreglos de cualquier tipo.

    function invertirArreglo<T>(arreglo: T[]): T[] {
        return arreglo.reverse();
    }

    console.log(invertirArreglo([1, 2, 3, 4])); // [4, 3, 2, 1]
    console.log(invertirArreglo(["a", "b", "c"])); // ["c", "b", "a"]

})()