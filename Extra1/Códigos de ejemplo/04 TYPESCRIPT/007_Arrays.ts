(() => {


    // Crear un array vacío de cadenas
    let frutas: string[] = [];

    // Añadir elementos al array
    frutas.push("Manzana"); // Añade al final
    frutas.push("Banana");
 

    // Añadir un elemento al inicio
    frutas.unshift("Naranja");

    console.log(frutas); // Salida: ["Naranja", "Manzana", "Banana"]

    // Eliminar el último elemento del array
    let ultimaFruta = frutas.pop(); // Elimina "Banana"

    console.log(ultimaFruta); // Salida: "Banana"
    console.log(frutas); // Salida: ["Naranja", "Manzana"]


})()