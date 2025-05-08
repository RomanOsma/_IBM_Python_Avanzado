(() => {

    // ***************************
    //     GENERICS
    // ***************************

    // Escribe una función genérica identidad que tome un argumento de cualquier tipo y lo devuelva. 
    // Demuestra su uso con varios tipos de datos.


    function identidad<T>(arg: T): T {
        return arg;
    }

    console.log(identidad<string>("Hola mundo"));
    console.log(identidad<number>(42));
    console.log(identidad<boolean>(true));


})()