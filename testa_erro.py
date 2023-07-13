class MeuErro(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return repr(self.valor)

lista = [1, 2,[1,2,3], 'a', 2.1]
print(lista)