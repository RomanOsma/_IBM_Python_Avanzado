(() => {

    // ***************************
    //     GENERICS
    // ***************************

    // muestra cómo puedes escribir una función que acepte y devuelva un valor 
    // de cualquier tipo.
    
    function identidad<T>(arg: T): T {
        return arg;
    }
    
    let cadena = identidad("miCadena"); // 'cadena' es de tipo 'string'
    let numero = identidad(10); // 'numero' es de tipo 'number'
    console.log(cadena); // Muestra: miCadena
    console.log(numero); // Muestra: 10
    

})()