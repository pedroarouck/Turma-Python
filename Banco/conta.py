from cliente import Cliente
class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        print('Inicializando a conta')
        self.numero = numero
        self.titular = cliente.nome
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print("numero: {} \ntitular: {} \nsaldo: {}".format(self.numero, self.titular, self.saldo))

    def transferir(self, destino, valor):
        retirada = self.sacar(valor)
        if (retirada == False):
            return False
        else:
            destino.depositar(valor)
            return True