class ControleBonificacao:

    def __init__(self, total_bonificacao = 0):
        self._total_bonificacao = total_bonificacao

    def registro(self, funcionario):
        self._total_bonificacao += funcionario.get_bonificacao()

    @property
    def total_bonificacao(self):
        return self._total_bonificacao