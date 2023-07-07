from conta import Conta
class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2