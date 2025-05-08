(() => {

    // ***************************
    //     FUNCIONES ANÓNIMAS
    // ***************************


    // Usa una función anónima para ordenar un arreglo de números de mayor a menor.

    const numeros = [3, 1, 4, 1, 5, 9, 2, 6];
    numeros.sort(function (a, b) {
        return b - a;
    });
    console.log(numeros);

})()