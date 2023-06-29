class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('Inicializando a conta')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("numero: {} \ntitular: {} \nsaldo: {}".format(self.numero, self.titular, self.saldo))
