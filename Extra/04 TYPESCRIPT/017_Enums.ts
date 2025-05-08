(() => {

    // ***************************
    //     ENUMS
    // ***************************

    // Imagina que estás desarrollando una aplicación para gestionar pedidos. 
    // Usa ENUM para representar los distintos estados por los que puede pasar un pedido:
    //     Pendiente,
    //     EnPreparacion,
    //     Enviado,
    //     Entregado,
    //     Cancelado.

    enum EstadoPedido {
        Pendiente,
        EnPreparacion,
        Enviado,
        Entregado,
        Cancelado,
    }

    let pedido: EstadoPedido = EstadoPedido.Pendiente;

    // El pedido progresa
    pedido = EstadoPedido.EnPreparacion;

    // Luego es enviado
    pedido = EstadoPedido.Enviado;

    console.log(pedido); // Muestra 2, correspondiente al valor de 'Enviado' en el enum.


})()