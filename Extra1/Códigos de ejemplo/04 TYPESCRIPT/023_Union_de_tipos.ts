(() => {

    // ***************************
    //     UNIÓN DE TIPOS
    // ***************************

    // Crea una función concatenar que pueda unir dos string o dos number. 
    // Si los argumentos son number, conviértelos a string antes de concatenarlos. 
    // La función debe retornar el resultado de la concatenación.

    function concatenar(a: string | number, b: string | number): string {
        return a.toString() + b.toString();
    }

    console.log(concatenar("Hola, ", "mundo"));
    console.log(concatenar(100, 200));


})()