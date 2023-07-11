from gerente import Gerente
from funcionario import Funcionario
from controle_bonificacao import ControleBonificacao
from diretor import Diretor
from cliente import Cliente
from sistema_interno import SistemaInterno

gerente = Gerente('José', '000000000-00', 5000.0, '1234', 0)

diretor = Diretor('Maria', '222222222-22', 10000.0)

cliente = Cliente("Pedro", "Salles", "000000000-00", '1234')

sistema = SistemaInterno()
sistema.login(gerente)
sistema.login(cliente)
sistema.login(diretor)

