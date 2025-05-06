(() => {

    // **********************************************
    //     POO - Herencia
    // **********************************************

    // Crea una clase base Empleado con propiedades nombre y sueldo. 
    // Añade un método mostrarInformacion() que imprima el nombre y sueldo del empleado. 
    // Luego, crea clases derivadas Gerente y Desarrollador, que hereden de Empleado. 
    // La clase Gerente debe tener una propiedad adicional departamento, y la clase 
    // Desarrollador una propiedad lenguajeDeProgramacion. 
    // Sobrescribe el método mostrarInformacion() para incluir las nuevas propiedades.


    class Empleado {
        nombre: string;
        sueldo: number;

        constructor(nombre: string, sueldo: number) {
            this.nombre = nombre;
            this.sueldo = sueldo;
        }

        mostrarInformacion(): void {
            console.log(`Nombre: ${this.nombre}, Sueldo: ${this.sueldo}`);
        }
    }

    class Gerente extends Empleado {
        departamento: string;

        constructor(nombre: string, sueldo: number, departamento: string) {
            super(nombre, sueldo);
            this.departamento = departamento;
        }

        mostrarInformacion(): void {
            super.mostrarInformacion();
            console.log(`Departamento: ${this.departamento}`);
        }
    }

    class Desarrollador extends Empleado {
        lenguajeDeProgramacion: string;

        constructor(nombre: string, sueldo: number, lenguajeDeProgramacion: string) {
            super(nombre, sueldo);
            this.lenguajeDeProgramacion = lenguajeDeProgramacion;
        }

        mostrarInformacion(): void {
            super.mostrarInformacion();
            console.log(`Lenguaje de Programación: ${this.lenguajeDeProgramacion}`);
        }
    }

    // Instancias de prueba
    const gerente = new Gerente("Ana", 5000, "Sistemas");
    gerente.mostrarInformacion();

    const desarrollador = new Desarrollador("Luis", 4000, "JavaScript");
    desarrollador.mostrarInformacion();

})()