(() => {

    // ****************************************************************************
    //     POO - CLase con atributos, métodos, constructor e instancias de clase
    // ****************************************************************************

    class CuentaBancaria {
        titular: string;
        private saldo: number;

        constructor(titular: string, saldoInicial: number) {
            this.titular = titular;
            this.saldo = saldoInicial;
        }

        depositar(monto: number): void {
            this.saldo += monto;
            console.log(`Depósito de $${monto} realizado con éxito.`);
        }

        retirar(monto: number): boolean {
            if (monto <= this.saldo) {
                this.saldo -= monto;
                console.log(`Retiro de $${monto} realizado con éxito.`);
                return true;
            } else {
                console.log("Saldo insuficiente.");
                return false;
            }
        }

        consultarSaldo(): number {
            return this.saldo;
        }
    }

    // Instancias de la clase CuentaBancaria
    const cuenta1 = new CuentaBancaria("Ana", 500);
    const cuenta2 = new CuentaBancaria("Luis", 1000);

    cuenta1.depositar(200);
    console.log(cuenta1.consultarSaldo()); // Muestra 700
    cuenta2.retirar(1500); // Intenta retirar más del saldo disponible, muestra mensaje de error




})()