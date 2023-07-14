class InformacoesMixIn:

    def tamanho(self):
        return len(self.dados)

    def esta_vazia(self):
        return len(self.dados) == 0

class Fila(InformacoesMixIn):
    def __init__(self):
        self.dados = []

    def insere(self, elemento):
        self.dados.append(elemento)

    def retira(self):
        if not self.esta_vazia():
            return self.dados.pop(0)
        else:
            return False

    def __str__(self):
        return "Fila: {}".format(self.dados)

class Pilha(InformacoesMixIn):

    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.esta_vazia():
            return self.dados.pop(-1)
        else:
            return False

    def __str__(self):
        return "Pilha: {}".format(self.dados)











