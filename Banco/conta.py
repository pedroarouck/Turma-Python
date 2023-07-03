from cliente import Cliente
from historico import Historico
class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        print('Inicializando a conta')
        self.numero = numero
        self.titular = cliente.nome
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {} reais".format(valor))

    def sacar(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {} reais".format(valor))
            return True

    def extrato(self):
        print("numero: {} \ntitular: {} \nsaldo: {}".format(self.numero, self.titular, self.saldo))
        self.historico.transacoes.append("tirou o extrato - saldo {} reais".format(self.saldo))

    def transferir(self, destino, valor):
        retirada = self.sacar(valor)
        if (retirada == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("envio de {} reais sacados para a conta {}".format(valor, destino.numero))
            return True