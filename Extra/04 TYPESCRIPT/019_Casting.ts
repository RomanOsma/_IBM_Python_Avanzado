(() => {

    // ***************************
    //     CASTING
    // ***************************


    // Tienes un objeto de tipo any que representa a un usuario con propiedades nombre y edad. 
    // Usa una aserción de tipo para acceder a la propiedad nombre del objeto y mostrarla en la consola.


    let usuario: any = { nombre: "Juan", edad: 30 };
    // Realiza la aserción de tipo aquí
    console.log(usuario.nombre.lenght); // Debería mostrar "Juan"


})()