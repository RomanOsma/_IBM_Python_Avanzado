(() => {

    // **********************************************
    //     POO - Interfaces
    // **********************************************

    // Define una interfaz Usuario que contenga las propiedades nombreDeUsuario y contraseña. 
    // Luego, crea otra interfaz ServicioAutenticacion que defina un método iniciarSesion 
    // que tome un objeto Usuario y retorne un booleano indicando si la autenticación fue 
    // exitosa o no. 
    // Implementa ServicioAutenticacion en una clase AutenticacionSimple que valide un 
    // nombre de usuario y contraseña predeterminados.


    interface Usuario {
        nombreDeUsuario: string;
        contraseña: string;
    }

    interface ServicioAutenticacion {
        iniciarSesion(usuario: Usuario): boolean;
    }

    class AutenticacionSimple implements ServicioAutenticacion {
        usuarioValido: Usuario = { nombreDeUsuario: "admin", contraseña: "1234" };

        iniciarSesion(usuario: Usuario): boolean {
            return usuario.nombreDeUsuario === this.usuarioValido.nombreDeUsuario &&
                usuario.contraseña === this.usuarioValido.contraseña;
        }
    }

    const usuario = { nombreDeUsuario: "admin", contraseña: "1234" };
    const servicio = new AutenticacionSimple();
    console.log(servicio.iniciarSesion(usuario)); // true o false dependiendo de la validez

})()