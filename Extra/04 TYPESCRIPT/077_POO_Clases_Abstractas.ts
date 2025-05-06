(() => {

    // **********************************************
    //     POO - Clases Abstractas
    // **********************************************


    // Crea una clase abstracta Notificador con un método abstracto 
    // enviarMensaje(mensaje: string): void. 
    // Después, implementa dos clases concretas: NotificadorEmail y NotificadorSMS, 
    // que extiendan de Notificador y proporcionen implementaciones específicas 
    // para el método enviarMensaje.

    abstract class Notificador {
        abstract enviarMensaje(mensaje: string): void;
    }

    class NotificadorEmail extends Notificador {
        emailDestino: string;

        constructor(emailDestino: string) {
            super();
            this.emailDestino = emailDestino;
        }

        enviarMensaje(mensaje: string): void {
            console.log(`Enviando email a ${this.emailDestino}: ${mensaje}`);
        }
    }

    class NotificadorSMS extends Notificador {
        numeroTelefono: string;

        constructor(numeroTelefono: string) {
            super();
            this.numeroTelefono = numeroTelefono;
        }

        enviarMensaje(mensaje: string): void {
            console.log(`Enviando SMS al número ${this.numeroTelefono}: ${mensaje}`);
        }
    }

    // Instancias de prueba
    const notificadorEmail = new NotificadorEmail("usuario@example.com");
    notificadorEmail.enviarMensaje("Hola, este es un mensaje de prueba.");

    const notificadorSMS = new NotificadorSMS("123456789");
    notificadorSMS.enviarMensaje("Hola, este es un mensaje de prueba.");

})()