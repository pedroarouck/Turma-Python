'''
Faça com que a função DashInsert(str) insira traços ('-')
entre cada dois números ímpares em str. Por exemplo: se str
for 454793, a saída deve ser 4547-9-3. Não conte o zero como
um número ímpar.
'''

def DashInsert(string):
    nova_string = ''
    ultimo_digito = string[len(string)-1]
    for indice in range(0, len(string)-1):
        digito = int(string[indice])
        proximo_digito = int(string[indice+1])

        if digito % 2 != 0 and proximo_digito % 2 != 0:
            nova_string = nova_string + str(digito) + '-'
        else:
            nova_string = nova_string + str(digito)
    return nova_string + ultimo_digito

print(DashInsert("113035547854"))




