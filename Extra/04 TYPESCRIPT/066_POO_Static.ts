(() => {

    // **********************************************
    //     POO - Static
    // **********************************************

    // Desarrolla una clase ConversorUnidades que contenga métodos estáticos para convertir 
    // diferentes unidades de medida. Implementa al menos dos conversiones: una de kilómetros 
    // a millas y otra de kilogramos a libras. 
    // Los métodos deben recibir un valor y devolver el resultado de la conversión.


    class ConversorUnidades {
        private static kilometrosAMillas = 0.621371;
        private static kilogramosALibras = 2.20462;

        public static deKilometrosAMillas(kilometros: number): number {
            return kilometros * ConversorUnidades.kilometrosAMillas;
        }

        public static deKilogramosALibras(kilogramos: number): number {
            return kilogramos * ConversorUnidades.kilogramosALibras;
        }
    }

    // Uso de los métodos estáticos
    console.log(ConversorUnidades.deKilometrosAMillas(10)); // Convierte 10 kilómetros a millas
    console.log(ConversorUnidades.deKilogramosALibras(5)); // Convierte 5 kilogramos a libras

})()