(() => {

    // **********************************************
    //     POO - Clases Abstractas
    // **********************************************


    // Implementa una clase abstracta Empleado que contenga un método 
    // abstracto calcularSalario(): number. 
    // Crea dos clases derivadas: EmpleadoPorHora y EmpleadoFijo, donde 
    // EmpleadoPorHora calcula su salario basado en las horas trabajadas y 
    // una tarifa por hora, mientras que EmpleadoFijo tiene un salario mensual fijo.

    abstract class Empleado {
        nombre: string;

        constructor(nombre: string) {
            this.nombre = nombre;
        }

        abstract calcularSalario(): number;
    }

    class EmpleadoPorHora extends Empleado {
        horasTrabajadas: number;
        tarifaPorHora: number;

        constructor(nombre: string, horasTrabajadas: number, tarifaPorHora: number) {
            super(nombre);
            this.horasTrabajadas = horasTrabajadas;
            this.tarifaPorHora = tarifaPorHora;
        }

        calcularSalario(): number {
            return this.horasTrabajadas * this.tarifaPorHora;
        }
    }

    class EmpleadoFijo extends Empleado {
        salarioMensual: number;

        constructor(nombre: string, salarioMensual: number) {
            super(nombre);
            this.salarioMensual = salarioMensual;
        }

        calcularSalario(): number {
            return this.salarioMensual;
        }
    }

    // Instancias de prueba
    const empleadoPorHora = new EmpleadoPorHora("Juan", 40, 15);
    console.log(empleadoPorHora.calcularSalario());

    const empleadoFijo = new EmpleadoFijo("Ana", 3000);
    console.log(empleadoFijo.calcularSalario());

})()