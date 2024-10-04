class TarjetaCredito:
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self  # Devolver self para encadenamiento

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self  # Devolver self para encadenamiento

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self  # Devolver self para encadenamiento


class Usuario:
    def __init__(self, nombre, tarjetas=[]):
        self.nombre = nombre
        self.tarjetas = tarjetas

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)
        return self  # Devolver self para encadenamiento

    def hacer_compra(self, monto, numero_tarjeta=0):
        if numero_tarjeta < len(self.tarjetas):
            self.tarjetas[numero_tarjeta].compra(monto)
        else:
            print("Número de tarjeta inválido.")
        return self

    def pagar_tarjeta(self, monto, numero_tarjeta=0):
        if numero_tarjeta < len(self.tarjetas):
            self.tarjetas[numero_tarjeta].pago(monto)
        else:
            print("Número de tarjeta inválido.")
        return self

    def mostrar_saldo_usuario(self):
        for i, tarjeta in enumerate(self.tarjetas):
            print(f"Tarjeta {i+1}:")
            tarjeta.mostrar_info_tarjeta()


# Crear instancias de usuario y tarjetas
usuario1 = Usuario("Juan")
tarjeta1 = TarjetaCredito(limite_credito=5000, intereses=0.02)
usuario1.agregar_tarjeta(tarjeta1)

usuario2 = Usuario("María")
tarjeta2 = TarjetaCredito(limite_credito=10000, intereses=0.03, saldo_pagar=1000)
tarjeta3 = TarjetaCredito(limite_credito=2000, intereses=0.05)
usuario2.agregar_tarjeta(tarjeta2).agregar_tarjeta(tarjeta3)  # Encadenamiento

# Realizar operaciones
usuario1.hacer_compra(1000).mostrar_saldo_usuario()
usuario2.hacer_compra(500, 0).pagar_tarjeta(200, 1).mostrar_saldo_usuario()