(() => {

    // **********************************************
    //     POO
    // **********************************************

    // Crea una clase CuentaBancaria que encapsule el saldo de la cuenta, de manera que 
    // solo pueda ser modificado mediante los métodos depositar() y retirar(). 
    // El método depositar() solo debe aceptar valores positivos. 
    // El método retirar() debe permitir retirar dinero solo si hay saldo suficiente en la cuenta. 
    // Añade un método consultarSaldo() que permita ver el saldo actual sin modificarlo.

    class CuentaBancaria {
        private saldo: number;

        constructor(saldoInicial: number) {
            this.saldo = saldoInicial;
        }

        public depositar(monto: number): void {
            if (monto > 0) {
                this.saldo += monto;
            } else {
                console.error('El monto a depositar debe ser positivo.');
            }
        }

        public retirar(monto: number): void {
            if (monto <= this.saldo) {
                this.saldo -= monto;
            } else {
                console.error('Saldo insuficiente.');
            }
        }

        public consultarSaldo(): number {
            return this.saldo;
        }
    }

    // Test de la clase
    const cuenta = new CuentaBancaria(1000);
    cuenta.depositar(500);
    cuenta.retirar(200);
    console.log(cuenta.consultarSaldo()); // Debería mostrar 1300


})()