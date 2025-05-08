(() => {

    // ***************************
    //     TYPE
    // ***************************


    // Crea un tipo EstadoCarga que represente los posibles estados de una petición de carga. 
    // Este tipo debe incluir los valores 'cargando', 'exitoso', 'error'.

    type EstadoCarga = 'cargando' | 'exitoso' | 'error';

    function mostrarEstado(estado: EstadoCarga) {
        console.log(`El estado de la carga es: ${estado}`);
    }

    mostrarEstado('cargando'); // Debería imprimir: El estado de la carga es: cargando
    mostrarEstado('exitoso'); // Debería imprimir: El estado de la carga es: exitoso
    mostrarEstado('error');    // Debería imprimir: El estado de la carga es: error

})()