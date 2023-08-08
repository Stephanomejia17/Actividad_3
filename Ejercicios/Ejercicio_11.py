class CuentaBancaria:
    monto = 0

    def __init__(self, num_cuenta: str, propietarios: str, balance: str):
        self.num_cuenta: str = num_cuenta
        self.propietarios: str = propietarios
        self.balance: str = balance

    def depositar(self, dinero: float):
        print("Deposito Exitoso")
        self.monto += dinero

    def retirar(self, dinero: float):
        if(self.monto >= dinero):
            self.monto -= dinero
            print("Retiro Satisfactorio")
        else:
            print("Fondos insuficientes")
    def aplicar_cuota_de_manejo(self):
        self.balance = "2%"
    def mostrar_detalles(self):
        print("Numero de cuenta: ", self.num_cuenta)
        print("Propietarios: ", self.propietarios)
        print("Balance: ", self.balance)
        print("Dinero Disponible: ", self.monto)

mi_cuenta_de_ahorro = CuentaBancaria("123456", "Stephano Mejia", "0%")
mi_cuenta_de_ahorro.depositar(10000)
mi_cuenta_de_ahorro.retirar(500)
mi_cuenta_de_ahorro.aplicar_cuota_de_manejo()
mi_cuenta_de_ahorro.mostrar_detalles()
