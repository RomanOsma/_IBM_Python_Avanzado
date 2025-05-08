(() => {

    // ***************************
    //     UNIÓN DE TIPOS
    // ***************************

    // Define una función obtenerDetalle que acepte un id (number) y retorne un string o un null. 
    // Si el id es menor que 10, devuelve "Detalle para id: [id]". De lo contrario, devuelve null.

    function obtenerDetalle(id: number): string | null {
        if (id < 10) {
            return `Detalle para id: ${id}`;
        } else {
            return null;
        }
    }

    console.log(obtenerDetalle(5)); // Debería imprimir "Detalle para id: 5"
    console.log(obtenerDetalle(15)); // Debería imprimir "null"


})()