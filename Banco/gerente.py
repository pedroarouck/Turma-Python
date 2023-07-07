from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_liderados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_liderados = qtd_liderados

    def autentica(self, senha):
        if self._senha == senha:
            return True
        else:
            return False

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000