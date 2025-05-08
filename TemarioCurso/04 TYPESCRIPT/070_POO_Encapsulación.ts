(() => {

    // **********************************************
    //     POO
    // **********************************************

    // Crea una clase Producto que tenga propiedades privadas para el nombre 
    // y precio de un producto. 
    // Implementa getters y setters para ambas propiedades, incluyendo validaciones 
    // en los setters para prevenir asignaciones de nombres vacíos y precios negativos o cero.


    class Producto {
        private _nombre: string;
        private _precio: number;

        constructor(nombre: string, precio: number) {
            this._nombre = nombre;
            this._precio = precio;
        }

        get nombre(): string {
            return this._nombre;
        }

        set nombre(nuevoNombre: string) {
            if (nuevoNombre === '') {
                console.error('El nombre del producto no puede estar vacío.');
            } else {
                this._nombre = nuevoNombre;
            }
        }

        get precio(): number {
            return this._precio;
        }

        set precio(nuevoPrecio: number) {
            if (nuevoPrecio <= 0) {
                console.error('El precio debe ser mayor que cero.');
            } else {
                this._precio = nuevoPrecio;
            }
        }
    }

    // Test de la clase
    const producto = new Producto("Laptop", 1000);
    console.log(producto.nombre); // Muestra: Laptop
    producto.nombre = ""; // Error: El nombre del producto no puede estar vacío
    producto.precio = -100; // Error: El precio debe ser mayor que cero
    console.log(producto.precio); // Muestra: 1000

})()