(() => {

    // ***************************
    //     CASTING
    // ***************************


    // Tienes una variable de tipo any que sabes que contiene una cadena de texto. 
    // Realiza una aserción de tipo para tratar esta variable como un string.

    let valor: any = "Hola, TypeScript";
    // Realiza la aserción de tipo aquí
    let longitud: number = (valor as string).length;
    console.log(longitud); // Debería mostrar la longitud de la cadena


})()