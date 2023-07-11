class SistemaInterno:

    def login(self, obj):
        if hasattr(obj, 'autentica'):
            obj.autentica(obj.senha)
            print('Autenticável')
            return True
        else:
            print('Não autenticável')
            return False