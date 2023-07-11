
class SeguroIphone:

    def __init__(self, valor, titular, numero):
        self._valor = valor
        self._titular = titular
        self._numero = numero

    def get_valor_imposto(self):
        return 50 + self._valor * 0.1