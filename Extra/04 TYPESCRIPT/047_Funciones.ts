(() => {

    // ***************************
    //     FUNCIONES FLECHA
    // ***************************


    // Implementa una función de calculadora que tome dos números y una operación 
    // opcional ("suma", "resta", "multiplicacion", "division"). 
    // Si no se especifica una operación, debe asumir "suma" por defecto.
    // Las opciones de sumar, restar , multiplicar y dividir se las pasaremos por unión de tipos
    // Usar un Switch...case

    function calcular(a: number, b: number, operacion?: "suma" | "resta" | "multiplicacion" | "division"): number {
        switch (operacion) {
            case "resta":
                return a - b;
            case "multiplicacion":
                return a * b;
            case "division":
                return a / b;
            default:
                return a + b;
        }
    }

    console.log(calcular(10, 5, "resta")); // 5
    console.log(calcular(4, 2)); // 6

})()