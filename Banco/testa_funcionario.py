from gerente import Gerente
from funcionario import Funcionario
from controle_bonificacao import ControleBonificacao
from diretor import Diretor

gerente = Gerente('José', '000000000-00', 5000.0, '1234', 0)
print('bonificacao gerente: {}'.format(gerente.get_bonificacao()))

#funcionario = Funcionario('Joao', '111111111-11', 2000.0)
#print('bonificacao funcionario: {}'.format(funcionario.get_bonificacao()))

diretor = Diretor('Maria', '222222222-22', 10000.0)

controle = ControleBonificacao()
#controle.registro(funcionario)
controle.registro(gerente)
print("total: {}".format(controle.total_bonificacao))
