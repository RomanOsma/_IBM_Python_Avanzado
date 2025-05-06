(() => {

    // ****************************************************************************
    //     POO - CLase con atributos, métodos, constructor e instancias de clase
    // ****************************************************************************

    class Libro {
        titulo: string;
        autor: string;
        numPaginas: number;
    
        constructor(titulo: string, autor: string, numPaginas: number) {
            this.titulo = titulo;
            this.autor = autor;
            this.numPaginas = numPaginas;
        }
    
        mostrarInfo(): string {
            return `${this.titulo} escrito por ${this.autor}, ${this.numPaginas} páginas.`;
        }
    
        esExtensivo(): boolean {
            return this.numPaginas > 300;
        }
    }
    
    // Instancias de la clase Libro
    const libro1 = new Libro("Cien Años de Soledad", "Gabriel García Márquez", 471);
    const libro2 = new Libro("El Principito", "Antoine de Saint-Exupéry", 96);
    
    console.log(libro1.mostrarInfo()); // Muestra info de libro1
    console.log(libro2.esExtensivo()); // Muestra false, indicando que El Principito no es un libro extenso
    


})()