(() => {

    // ************************************
    //     POO - DECLARACIÓN DE UNA CLASE
    // ************************************


    class Persona {
        nombre: string;
        edad: number;

        constructor(nombre: string, edad: number) {
            this.nombre = nombre;
            this.edad = edad;
        }

        presentarse() {
            return `Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años.`;
        }
    }

    let persona1 = new Persona("Juan", 30);
    console.log(persona1.presentarse());


})()