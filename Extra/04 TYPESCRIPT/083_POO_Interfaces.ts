(() => {

    // **********************************************
    //     POO - Interfaces
    // **********************************************

    // Diseñar e implementar una clase Vehiculo que cumpla con las especificaciones de dos interfaces:

    // La interfaz Motor debe especificar una propiedad tipoMotor y un método encenderMotor 
    // que muestre un mensaje indicando que el motor se ha encendido.
    // La interfaz Ruedas debe especificar una propiedad cantidadRuedas y un método mostrarRuedas 
    // que muestre la cantidad de ruedas del vehículo.
    // La clase Vehiculo debe implementar ambas interfaces, permitiendo especificar el tipo de 
    // motor y la cantidad de ruedas al crear una instancia de un vehículo, y proporcionar la 
    // funcionalidad para encender el motor y mostrar el número de ruedas.


    // Definición de interfaces
    interface Motor {
        tipoMotor: string;
        encenderMotor(): void;
    }

    interface Ruedas {
        cantidadRuedas: number;
        mostrarRuedas(): void;
    }

    // Implementación de la clase Vehiculo
    class Vehiculo implements Motor, Ruedas {
        tipoMotor: string;
        cantidadRuedas: number;

        constructor( tipoMotor: string, cantidadRuedas: number) { 
            this.tipoMotor=tipoMotor;
            this.cantidadRuedas=cantidadRuedas;
        }

        encenderMotor(): void {
            console.log(`El motor ${this.tipoMotor} ha sido encendido.`);
        }

        mostrarRuedas(): void {
            console.log(`El vehículo tiene ${this.cantidadRuedas} ruedas.`);
        }
    }

    // Demostración de uso
    let miVehiculo = new Vehiculo("gasolina", 4);
    miVehiculo.encenderMotor(); // Muestra: El motor gasolina ha sido encendido.
    miVehiculo.mostrarRuedas(); // Muestra: El vehículo tiene 4 ruedas.


})()