(() => {

    // **********************************************
    //     FUNCIONES CON DIFERENTES TIPOS DE RETORNO
    // **********************************************


    // Implementa una función que devuelva la longitud de una cadena o la suma de dos números, 
    // dependiendo de los tipos de sus argumentos.


    function longitudOSuma(x: number | string, y?: number): number {
        if (typeof x === 'string') {
            return x.length;
        } else if (typeof y === 'number') {
            return x + y;
        } else {
            return x;
        }
    }

    console.log(longitudOSuma('Test')); // 4
    console.log(longitudOSuma(7, 3)); // 10


})()