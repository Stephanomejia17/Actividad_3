class CuentaBancaria:
    monto = 0

    def __init__(self, num_cuenta: str, propietarios: str, balance: str):
        self.num_cuenta: str = num_cuenta
        self.propietarios: str = propietarios
        self.balance: str = balance

    def depositar(self, dinero: float):
        print("Deposito Exitoso")
        self.monto += dinero

mi_cuenta_de_ahorro = CuentaBancaria("123456", "Stephano Mejia", "0%")
mi_cuenta_de_ahorro.depositar(10000)
