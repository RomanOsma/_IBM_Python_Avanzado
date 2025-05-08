(() => {


    // Crear un array de números
    let numeros: any[] = [1, 2, 3, 4, 5];

    // Filtrar números mayores que 2
    let filtrados = numeros.filter(numero => numero > 2);

    console.log(filtrados); // Salida: [3, 4, 5]

    // Multiplicar cada número por 2 usando map
    let dobles = numeros.map(numero => numero * 2);

    console.log(dobles); // Salida: [2, 4, 6, 8, 10]



})()