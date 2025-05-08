(() => {

    // **********************************************
    //     POO - Clases Abstractas
    // **********************************************


    // Define una clase abstracta FiguraGeometrica que incluya propiedades comunes 
    // de las figuras geométricas, como color. 
    // Añade métodos abstractos para calcularArea() y calcularPerimetro(). 
    // Luego, crea clases concretas Circulo y Rectangulo que implementen estos métodos. 
    // Usa PI como 3.14 para el cálculo del área y el perímetro del círculo.

    abstract class FiguraGeometrica {
        color: string;

        constructor(color: string) {
            this.color = color;
        }

        abstract calcularArea(): number;
        abstract calcularPerimetro(): number;
    }

    class Circulo extends FiguraGeometrica {
        radio: number;

        constructor(color: string, radio: number) {
            super(color);
            this.radio = radio;
        }

        calcularArea(): number {
            return 3.14 * this.radio * this.radio;
        }

        calcularPerimetro(): number {
            return 2 * 3.14 * this.radio;
        }
    }

    class Rectangulo extends FiguraGeometrica {
        ancho: number;
        alto: number;

        constructor(color: string, ancho: number, alto: number) {
            super(color);
            this.ancho = ancho;
            this.alto = alto;
        }

        calcularArea(): number {
            return this.ancho * this.alto;
        }

        calcularPerimetro(): number {
            return 2 * (this.ancho + this.alto);
        }
    }

    // Instancias de prueba
    const circulo = new Circulo("rojo", 5);
    console.log(circulo.calcularArea());
    console.log(circulo.calcularPerimetro());

    const rectangulo = new Rectangulo("azul", 10, 5);
    console.log(rectangulo.calcularArea());
    console.log(rectangulo.calcularPerimetro());


})()