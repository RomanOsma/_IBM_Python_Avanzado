(() => {

    // **********************************************
    //     FUNCIONES CON DIFERENTES TIPOS DE RETORNO
    // **********************************************


    // Diseña una función que, si recibe dos números, eleve el primero al segundo. 
    // Si recibe una cadena y un número, devuelva la cadena seguida de ese número convertido a cadena.

    function elevarOUnir(x: number | string, y: number): number | string {
        if (typeof x === 'number') {
            return Math.pow(x, y);
        } else {
            return x + y.toString();
        }
    }

    console.log(elevarOUnir(2, 3)); // 8
    console.log(elevarOUnir('Número: ', 7)); // Número: 7

})()