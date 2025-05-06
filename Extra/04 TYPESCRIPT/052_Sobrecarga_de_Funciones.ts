(() => {

    // **********************************************
    //     SOBRECARGA DE FUNCIONES
    // **********************************************


    // Diseña una función combinar que pueda unir dos o tres números en una cadena, 
    // separados por un guion. La función debe poder ser llamada con dos o tres argumentos numéricos.

    function combinar(a: number, b: number): string;
    function combinar(a: number, b: number, c: number): string;
    function combinar(a: number, b: number, c?: number): string {
        if (c !== undefined) return `${a}-${b}-${c}`;
        return `${a}-${b}`;
    }

    console.log(combinar(1, 2)); // "1-2"
    console.log(combinar(1, 2, 3)); // "1-2-3"

})()