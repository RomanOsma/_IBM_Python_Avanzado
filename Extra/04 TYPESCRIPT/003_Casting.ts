(() => {

    let valor: any = "Este es un mensaje";
    // Asumimos que sabemos que 'valor' es realmente una cadena de texto.

    // Usamos 'casting' para tratarlo como tal y acceder a métodos específicos de string.
    let longitudDelMensaje: number = (valor as string).length;
    console.log(longitudDelMensaje); // Muestra la longitud del mensaje


})()