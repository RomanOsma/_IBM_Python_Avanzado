(() => {

    // **********************************************
    //     SOBRECARGA DE FUNCIONES
    // **********************************************


    // Implementa una función concatenar que puede unir dos string o dos number. 
    // Si los argumentos son number, conviértelos a string antes de concatenar.

    function concatenar(a: number, b: number): string;
    function concatenar(a: string, b: string): string;
    function concatenar(a: any, b: any): string {
        return a.toString() + b.toString();
    }

    console.log(concatenar("Hola, ", "mundo")); // "Hola, mundo"
    console.log(concatenar(100, 200)); // "100200"

})()