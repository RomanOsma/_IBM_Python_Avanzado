(() => {

    let valorAlguno: any = "Un texto interesante";
    // Aserción de tipo para tratar 'valorAlguno' como string
    let longitudTexto: number = (<string>valorAlguno).length;

    console.log(longitudTexto); // Muestra la longitud del texto
    
})()