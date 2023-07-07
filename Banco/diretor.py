from funcionario import Funcionario

class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def get_bonificacao(self):
        return super().get_bonificacao() * 2
