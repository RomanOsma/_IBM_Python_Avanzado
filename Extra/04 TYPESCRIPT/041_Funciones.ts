(() => {

    // ***************************
    //     FUNCIONES ANÓNIMAS
    // ***************************


    // Utiliza una función anónima con el método map para crear un nuevo arreglo que 
    // contenga los cuadrados de los números del arreglo original.

    const originales = [1, 2, 3, 4];
    const cuadrados = originales.map(function (numero) {
        return numero * numero;
    });
    console.log(cuadrados);

})()