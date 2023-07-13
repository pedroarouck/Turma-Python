from conta import Conta
from cliente import Cliente
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente
from atualizador_conta import AtualizadorConta
from seguro_iphone import SeguroIphone
from manipulador import Manipulador

cliente = Cliente("Pedro", "Salles", "000000000-00", "1234")
cc = ContaCorrente('123-4', cliente, 1000.0)
cc.depositar(500)
cc.sacar(50000)
print(cc)