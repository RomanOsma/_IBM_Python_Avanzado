(() => {

    // ***************************
    //     CASTING
    // ***************************


    // Tienes una función procesarDato que acepta un parámetro de tipo any. 
    // Dentro de la función, estás seguro de que el parámetro es un number. 
    // Realiza una aserción de tipo dentro de la función para trabajar con el 
    // parámetro como un number y calcula su cuadrado.


    function procesarDato(dato: any): number {
        // Realiza la aserción de tipo aquí
        let numero = dato as number;
        return numero * numero;
    }

    console.log(procesarDato(5)); // Debería mostrar 25

})()