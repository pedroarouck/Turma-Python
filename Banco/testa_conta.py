from conta import Conta

conta = Conta('123-4', 'Pedro Salles', 1000.0, 10000.0)
conta1 = Conta('321-4', 'Henrique Souza', 500.0, 10000.0)

conta1.depositar(250.0)
conta1.extrato()
conta1.sacar(500.0)
conta1.extrato()