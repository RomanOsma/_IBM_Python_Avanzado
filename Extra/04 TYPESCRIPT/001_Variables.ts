(() => {

    //NUMBERS
    const CERO: number = 0;
    let miNumber1: number = 3;
    let miNumber2: number = 0b1001; // binario
    let miNumber3: number = 0o246; // octal
    let miNumber4: number = 0xf0d; // hexadecimal

    //STRINGS
    var cadenaGlobal: string = "Hola mundo!";
    let cadenaLocal: string = 'Hola mundo!';
    let nombre: string = `Juan`;
    let saludo: string = `Hola, mi nombre es ${nombre}`//en TS



    //BOOLEANS
    let activo: boolean = false;

    //ANY
    let arrayMezclado: any[] = ['a'];


    //NEVER
    function error(mensajeError: string,): never {
        throw new Error(mensajeError);
    }

    error("Socorro!!!");

    //Otra opción de NEVER

    function error2(mensajeError: string): never | number {
        if (false) {
            throw new Error(mensajeError);
        } return 1;
    }

    error2("Socorro!!!");

    //NULL
    let miNull1: null = null;
    let miNull2: number = null; //Error forzado, No se puede asignar un null como number

    //UNDEFINED
    let miUndef: undefined = undefined;

    //VOID
    let miVoid1: void = undefined;
    let miVoid2: void = 1; // Error forzado, No se puede asignar un number como void

    //ARRAYS
    let arrayString: string[] = ['a', '2', 'b'];
    let arrayNumero: Array<number> = [1, 2, 3];

    //TUPLAS
    let miTupla: [number, string] = [5, 'Hola Mundo'];

    //TUPLA en dos pasos
    let miTupla2: [number, string];
    miTupla = [5, 'Hola Mundo']; //ok
    miTupla = [5, 6]; ////Error forzado, el segundo valor debería ser un string
    let miTupla2: [number, string | number, any, boolean, null, undefined];

    //ENUMS
    enum enumGranja { vaca, caballo, cerdo, gallina, pato }
    //En este caso: vaca=0, caballo=1, cerdo=2 y pato=3.

    //Emunerado con valores presonalizados
    enum volumen {
        minimo = 0,
        medio = 5,
        maximo = 10
    }


    // Aserciones de Tipo
    const poder: any = '100';
    const largoDelPoder: number = (poder as string).length;
    console.log(largoDelPoder);

    //Tipos personalizados
    //creamos un nuevo tipo de dato: color
    type color = "blue" | "green" | "red" | "yellow";
    function colorea(c: color) {
        let elegido: string = 'El color es ' + c;
        console.log(elegido);
    }
    colorea("red");

