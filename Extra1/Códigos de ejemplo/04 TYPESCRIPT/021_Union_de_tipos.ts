(() => {

    // ***************************
    //     UNIÓN DE TIPOS
    // ***************************

    // Escribe una función imprimirId que acepte un parámetro id que puede ser un number 
    // o un string. La función debe imprimir el id. 
    // Si el id es un number, añade el prefijo "Número: " antes de imprimirlo. 
    // Si es un string, añade "String: ".

    function imprimirId(id: number | string) {
        if (typeof id === "number") {
            console.log("Número: " + id);
        } else {
            console.log("String: " + id);
        }
    }
    
    imprimirId(101); // Debería imprimir "Número: 101"
    imprimirId("202"); // Debería imprimir "String: 202"
    

})()