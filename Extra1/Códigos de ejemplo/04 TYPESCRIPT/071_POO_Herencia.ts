(() => {

    // **********************************************
    //     POO - Herencia
    // **********************************************

    // Define una clase base Vehiculo con propiedades comunes como marca, modelo, y año. 
    // Incluye un método mostrarInformacion() que imprima la información del vehículo. 
    // A continuación, crea dos clases derivadas: Automovil y Motocicleta, que hereden 
    // de Vehiculo y añadan propiedades específicas, como numeroDePuertas para Automovil 
    // y tieneSidecar para Motocicleta. 
    // Sobrescribe el método mostrarInformacion() en las clases derivadas para incluir 
    // la información adicional.

    class Vehiculo {
        marca: string;
        modelo: string;
        año: number;

        constructor(marca: string, modelo: string, año: number) {
            this.marca = marca;
            this.modelo = modelo;
            this.año = año;
        }

        mostrarInformacion(): void {
            console.log(`Marca: ${this.marca}, Modelo: ${this.modelo}, Año: ${this.año}`);
        }
    }

    class Automovil extends Vehiculo {
        numeroDePuertas: number;

        constructor(marca: string, modelo: string, año: number, numeroDePuertas: number) {
            super(marca, modelo, año);
            this.numeroDePuertas = numeroDePuertas;
        }

        mostrarInformacion(): void {
            super.mostrarInformacion();
            console.log(`Número de puertas: ${this.numeroDePuertas}`);
        }
    }

    class Motocicleta extends Vehiculo {
        tieneSidecar: boolean;

        constructor(marca: string, modelo: string, año: number, tieneSidecar: boolean) {
            super(marca, modelo, año);
            this.tieneSidecar = tieneSidecar;
        }

        mostrarInformacion(): void {
            super.mostrarInformacion();
            console.log(`Tiene sidecar: ${this.tieneSidecar}`);
        }
    }

    // Instancias de prueba
    const miAuto = new Automovil("Toyota", "Corolla", 2020, 4);
    miAuto.mostrarInformacion();

    const miMoto = new Motocicleta("Harley Davidson", "Street 750", 2019, false);
    miMoto.mostrarInformacion();


})()