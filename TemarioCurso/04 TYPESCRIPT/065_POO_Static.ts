(() => {

    // **********************************************
    //     POO - Static
    // **********************************************

    // Crea una clase llamada ContadorInstancias que pueda rastrear cuántas instancias 
    // de esa clase han sido creadas. 
    // Cada vez que se crea una nueva instancia, el contador debe incrementarse. 
    // Proporciona un método estático cuantasInstancias() que devuelva el número total 
    // de instancias creadas de esa clase



    class ContadorInstancias {
        static contador: number = 0;

        constructor() {
            ContadorInstancias.contador++;
        }

        static cuantasInstancias(): number {
            return ContadorInstancias.contador;
        }
    }

    // Crear algunas instancias
    const instancia1 = new ContadorInstancias();
    const instancia2 = new ContadorInstancias();
    console.log(ContadorInstancias.cuantasInstancias()); // Debería mostrar 2

    const instancia3 = new ContadorInstancias();
    console.log(ContadorInstancias.cuantasInstancias()); // Debería mostrar 3


})()