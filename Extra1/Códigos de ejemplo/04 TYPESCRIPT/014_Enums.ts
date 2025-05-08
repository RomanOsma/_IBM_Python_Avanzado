(() => {

    // ***************************
    //     ENUMS
    // ***************************

    // Define un enum para los días de la semana, donde el domingo sea 0 y el sábado sea 6. 
    // Luego, escribe una función que acepte un valor del enum y devuelva si es fin de semana o no.
 
    enum Dia {
        Domingo,
        Lunes,
        Martes,
        Miercoles,
        Jueves,
        Viernes,
        Sabado,
    }
    
    function esFinDeSemana(dia: Dia): string {
        if (dia === Dia.Sabado || dia === Dia.Domingo) {
            return "Es fin de semana";
        } else {
            return "No es fin de semana";
        }
    }
    
    console.log(esFinDeSemana(Dia.Domingo)); // "Es fin de semana"
    console.log(esFinDeSemana(Dia.Miercoles)); // "No es fin de semana"
    

})()