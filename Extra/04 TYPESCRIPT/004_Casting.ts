(() => {

    // Tenemos una variable que es de tipo string, pero queremos tratarla como un número.
    let numeroComoTexto: string = "123";

    // Usamos el casting para convertir el string a number.
    let numeroReal: number = Number(numeroComoTexto);

    console.log(numeroReal); // Ahora `numeroReal` es de tipo number, y podemos hacer operaciones numéricas con él.




})()