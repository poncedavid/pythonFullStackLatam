class TarjetaCredito:
    def __init__(self, limite_credito, intereses, saldo_pagar=0):  # Orden de parámetros actualizado
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")

    def pago(self, monto):
        self.saldo_pagar -= monto

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses

    @classmethod
    def imprimir_tarjetas(cls, tarjetas):
        for tarjeta in tarjetas:
            tarjeta.mostrar_info_tarjeta()


# Crear 3 tarjetas
tarjeta1 = TarjetaCredito(limite_credito=5000, intereses=0.02)
tarjeta2 = TarjetaCredito(limite_credito=10000, intereses=0.03, saldo_pagar=1000)
tarjeta3 = TarjetaCredito(limite_credito=2000, intereses=0.05)

# Operaciones con la tarjeta 1
tarjeta1.compra(1000).compra(2000).pago(500).cobrar_interes().mostrar_info_tarjeta()

# Operaciones con la tarjeta 2
tarjeta2.compra(500).compra(1500).compra(3000).pago(1000).pago(500).cobrar_interes().mostrar_info_tarjeta()

# Operaciones con la tarjeta 3 (excediendo el límite)
tarjeta3.compra(1000).compra(500).compra(700).compra(100).compra(50).mostrar_info_tarjeta()

# Imprimir información de todas las tarjetas (BONUS)
tarjetas = [tarjeta1, tarjeta2, tarjeta3]
TarjetaCredito.imprimir_tarjetas(tarjetas)