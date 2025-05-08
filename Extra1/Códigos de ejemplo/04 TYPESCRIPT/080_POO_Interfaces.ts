(() => {

    // **********************************************
    //     POO - Interfaces
    // **********************************************


    // Define una interfaz Vehiculo que especifique un contrato para objetos 
    // vehículo con las siguientes propiedades y métodos: 
    // marca (string), modelo (string), año (number) y un método mostrarDetalle() 
    // que no tome argumentos y no retorne nada. Implementa la interfaz en una 
    // clase Coche y sobrescribe el método mostrarDetalle() para que muestre las 
    // propiedades del coche.

    interface Vehiculo {
        marca: string;
        modelo: string;
        año: number;
        mostrarDetalle(): void;
    }

    class Coche implements Vehiculo {
        marca: string;
        modelo: string;
        año: number;

        constructor(marca: string, modelo: string, año: number) {
            this.marca = marca;
            this.modelo = modelo;
            this.año = año;
        }

        mostrarDetalle(): void {
            console.log(`Marca: ${this.marca}, Modelo: ${this.modelo}, Año: ${this.año}`);
        }
    }

    const miCoche = new Coche("Toyota", "Corolla", 2020);
    miCoche.mostrarDetalle();

})()