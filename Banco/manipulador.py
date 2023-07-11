class Manipulador:

    def calcula_imposto(self, lista_tributavel):
        total = 0
        for t in lista_tributavel:
            total += t.get_valor_imposto()

        return total