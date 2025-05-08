(() => {

    // **********************************************
    //     POO - Static
    // **********************************************

    // Crea una clase GeneradorID que genere un identificador único (ID) cada vez que se 
    // llame a su método estático generarID(). El ID generado debe ser un número entero 
    // que incremente en 1 el valor del último ID generado. El primer ID debe ser 1.


    class GeneradorID {
        private static ultimoID = 0;

        public static generarID(): number {
            return ++GeneradorID.ultimoID;
        }
    }

    // Generar algunos IDs
    console.log(GeneradorID.generarID()); // Debería mostrar 1
    console.log(GeneradorID.generarID()); // Debería mostrar 2
    console.log(GeneradorID.generarID()); // Debería mostrar 3

})()