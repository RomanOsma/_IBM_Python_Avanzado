(() => {

    // **********************************************
    //     FUNCIONES CON DIFERENTES TIPOS DE RETORNO
    // **********************************************

    // Implementa una función procesar sobrecargada que:

    // Devuelva la longitud de una cadena cuando se le pasa un string.
    // Devuelva el cuadrado de un número cuando se le pasa un number.
    // Devuelva true si se le pasa un boolean que es true, de lo contrario, devuelva false.

    function procesar(entrada: string): number;
function procesar(entrada: number): number;
function procesar(entrada: boolean): boolean;

function procesar(entrada: string | number | boolean): number | boolean {
    if (typeof entrada === "string") {
        return entrada.length;
    } else if (typeof entrada === "number") {
        return entrada * entrada;
    } else {
        return entrada;
    }
}

// Pruebas de la función
console.log(procesar("Hello World")); // Debería devolver 11
console.log(procesar(5)); // Debería devolver 25
console.log(procesar(true)); // Debería devolver true
console.log(procesar(false)); // Debería devolver false


})()