'''
Faça com que a função PowersofTwo(num) pegue o parâmetro num
sendo passado, que será um número inteiro e retorne a string
true se for uma potência de dois. Se não for, retorne a string
false. Por exemplo, se a entrada for 16, seu programa deve retornar
a string true, mas se a entrada for 22, a saída deve ser a string false.
'''

def PowerofTwo(num):
    if num == 0:
        return 'false'
    while num != 1:
        if num % 2 != 0:
            return 'false'
        else:
            num = num // 2
    return 'true'

print(PowerofTwo(16))