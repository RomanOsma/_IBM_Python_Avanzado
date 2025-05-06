(() => {

    // **********************************************
    //     POO - Herencia - Sobrecarga de métodos
    // **********************************************


    // Implementa una clase PerfilUsuario que tenga un método crear sobrecargado para 
    // crear un perfil de usuario:

    // Utilizando un nombre.
    // Utilizando un nombre y una edad.

    class PerfilUsuario {
        crear(nombre: string): void;
        crear(nombre: string, edad: number): void;

        crear(nombre: string, edad?: number): void {
            console.log(`Perfil creado para ${nombre}${edad ? `, edad ${edad}` : ''}.`);
        }
    }

    const perfil = new PerfilUsuario();
    perfil.crear("Juan"); // Perfil creado para Juan.
    perfil.crear("Juan", 30); // Perfil creado para Juan, edad 30.

})()