(() => {

    // ***************************
    //     FUNCIONES
    // ***************************

    // Crea una función que reciba un nombre (string) como parámetro y retorne un saludo 
    // personalizado. Si no se proporciona un nombre, debe retornar "Hola, mundo".


    function saludar(nombre: string = "mundo"): string {
        return `Hola, ${nombre}`;
    }

    console.log(saludar("Alice")); // Hola, Alice
    console.log(saludar()); // Hola, mundo

})()