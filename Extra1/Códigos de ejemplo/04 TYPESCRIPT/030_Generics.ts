(() => {

    // ***************************
    //     GENERICS
    // ***************************

    // Considera una función genérica de búsqueda que puede buscar un elemento 
    // dentro de un array de cualquier tipo y devolver un valor booleano indicando 
    // si el elemento está presente.


    function contieneElemento<T>(elemento: T, lista: T[]): boolean {
        return lista.indexOf(elemento) > -1;
    }

    const tieneCinco = contieneElemento(5, [1, 2, 3, 4, 5]); // true
    console.log(tieneCinco);

    const tieneTexto = contieneElemento("Hola", ["Adiós", "Hola", "Bienvenido"]); // true
    console.log(tieneTexto);

})()