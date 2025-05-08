(() => {

    // ***************************
    //     TYPE
    // ***************************

    // Crea un alias de tipo Input que acepte string, number, o boolean. 
    // Usa este tipo para declarar una variable que pueda contener cualquiera de estos tipos de datos.


    type Input = string | number | boolean;

    let entrada: Input;
    entrada = "Hola, mundo";
    console.log(entrada);
    entrada = 42;
    console.log(entrada);
    entrada = true;
    console.log(entrada);

})()