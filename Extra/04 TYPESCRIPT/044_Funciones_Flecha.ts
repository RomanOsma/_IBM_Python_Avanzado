(() => {

    // ***************************
    //     FUNCIONES FLECHA
    // ***************************

    // Crea una función flecha que acepte dos parámetros: a y b, donde b tenga un valor 
    // predeterminado de 2. La función debe retornar la multiplicación de a y b.


    const multiplicar = (a: number, b: number = 2): number => a * b;

    console.log(multiplicar(5)); // 10
    console.log(multiplicar(5, 3)); // 15

})()