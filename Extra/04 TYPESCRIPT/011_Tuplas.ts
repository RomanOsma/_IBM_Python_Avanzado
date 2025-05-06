(() => {


    let estudiante: [string, number] = ["Roberto", 20];

    // Modificar el nombre del estudiante
    estudiante[0] = "Carla";

    // Incrementar la edad del estudiante
    estudiante[1] = estudiante[1] + 1;

    console.log(estudiante); // Muestra: ["Carla", 21]




})()