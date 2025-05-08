(() => {

    // ***************************
    //     ENUMS
    // ***************************

    // Utiliza un enum para representar las direcciones (Norte, Sur, Este, Oeste) y escribe 
    // una función que acepte una dirección y devuelva su opuesto.


    enum Direccion {
        Norte = "NORTE",
        Sur = "SUR",
        Este = "ESTE",
        Oeste = "OESTE",
    }

    function direccionOpuesta(direccion: Direccion): Direccion {
        switch (direccion) {
            case Direccion.Norte:
                return Direccion.Sur;
            case Direccion.Sur:
                return Direccion.Norte;
            case Direccion.Este:
                return Direccion.Oeste;
            case Direccion.Oeste:
                return Direccion.Este;
        }
    }

    console.log(direccionOpuesta(Direccion.Oeste)); // "SUR"

})()