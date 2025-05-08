(() => {

    // ***************************
    //     ENUMS
    // ***************************


    // Crea un enum para representar los estados de una conexión (Conectando, Conectado, Desconectado). 
    // Escribe una función que tome el estado de la conexión y devuelva un mensaje apropiado 
    // para el usuario.


    enum EstadoConexion {
        Conectando,
        Conectado,
        Desconectado,
    }

    function mensajeEstado(estado: EstadoConexion): string {
        switch (estado) {
            case EstadoConexion.Conectando:
                return "Conectando...";
            case EstadoConexion.Conectado:
                return "Conectado";
            case EstadoConexion.Desconectado:
                return "Desconectado";
        }
    }

    console.log(mensajeEstado(EstadoConexion.Conectado)); // "Conectado"


})()