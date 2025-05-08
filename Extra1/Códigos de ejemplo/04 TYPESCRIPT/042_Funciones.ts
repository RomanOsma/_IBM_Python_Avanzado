(() => {

    // ***************************
    //     FUNCIONES ANÓNIMAS
    // ***************************


    // Escribe una función anónima que se use con Array.filter para obtener todos los 
    // elementos de un arreglo de strings que tengan una longitud mayor a 3.

    const palabras = ["sol", "piedra", "cielo", "mar", "aire"];
    const filtradas = palabras.filter(function (palabra) {
        return palabra.length > 3;
    });
    console.log(filtradas);

})()