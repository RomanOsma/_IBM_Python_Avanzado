(() => {

    // ***************************
    //     GENERICS
    // ***************************


    // Define una función genérica crearTupla que acepte dos parámetros de tipos posiblemente 
    // diferentes y retorne una tupla que contenga esos dos elementos.

    function crearTupla<T, U>(primero: T, segundo: U): [T, U] {
        return [primero, segundo];
    }

    // Uso de la función
    const tupla1 = crearTupla("hola", 42); // ['hola', 42]
    const tupla2 = crearTupla(true, { nombre: "Alice" }); // [true, { nombre: 'Alice' }]

    console.log(tupla1);
    console.log(tupla2);

})()