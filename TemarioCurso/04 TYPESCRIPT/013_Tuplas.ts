(() => {

    // ***************************
    //     ELEMENTOS OPCIONALES
    // ***************************

    // Ejemplo válido: ambos elementos presentes
    let tuplaCompleta: [string, number?] = ["ejemplo", 42];

    // Ejemplo válido: solo el elemento obligatorio presente
    let tuplaSoloString: [string, number?] = ["solo texto"];

    // Ejemplo inválido: falta el elemento obligatorio
    // let tuplaIncorrecta: [string, number?] = [42]; // Error de compilación

    // Ejemplo inválido: orden incorrecto de elementos
    // let tuplaOrdenIncorrecto: [string, number?] = [42, "texto"]; // Error de compilación

    // Ejemplo válido: asignación posterior del segundo elemento
    let tuplaAsignacionPosterior: [string, number?] = ["inicial"];
    tuplaAsignacionPosterior[1] = 100;

    console.log(tuplaCompleta); // Muestra: ["ejemplo", 42]
    console.log(tuplaSoloString); // Muestra: ["solo texto"]
    console.log(tuplaAsignacionPosterior); // Muestra: ["inicial", 100]



})()