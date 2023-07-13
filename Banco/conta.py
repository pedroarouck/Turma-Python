from cliente import Cliente
from historico import Historico
from excecoes import SaldoInsuficienteError
import abc
class Conta(abc.ABC):
    _total_de_contas = 1
    def __init__(self, numero, cliente, saldo, limite = 10000.0):
        print('Inicializando a conta')
        self._numero = numero
        self._titular = cliente.nome+' '+cliente.sobrenome
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()

        Conta._total_de_contas += 1

    def __str__(self):
        return "Dados da Conta: \nNumero: {}\nTitular: {} \nSaldo: {}".format(self._numero, self._titular, self._saldo)

    @abc.abstractmethod
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

    @property
    def historico(self):
        return self._historico

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    @property
    def limite(self):
        return self._limite

    @staticmethod
    def get_total_de_contas():
        return Conta._total_de_contas


    def depositar(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo')
        else:
            self.saldo += valor
            self.historico.transacoes.append("depósito de {} reais".format(valor))

    def sacar(self, valor):
        if(valor < 0):
            raise ValueError('VocÊ tentou sacar um valor negativo')
        if(self.saldo < valor):
            raise SaldoInsuficienteError("Saldo Insuficiente")
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
