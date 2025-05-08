(() => {

    // ************************************
    //     POO - DECLARACIÓN DE UNA CLASE
    // ************************************

    class Coche {
        marca: string;
        modelo: string;

        constructor(marca: string, modelo: string) {
            this.marca = marca;
            this.modelo = modelo;
        }

        describirCoche() {
            return `Este coche es un ${this.marca} ${this.modelo}.`;
        }
    }

    let coche1 = new Coche("Toyota", "Corolla");
    console.log(coche1.describirCoche());



})()