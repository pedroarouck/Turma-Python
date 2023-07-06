'''
Faça com que a função StockPicker(arr) pegue a matriz de números armazenados
 em arr que conterá inteiros que representam o valor em dólares que vale
 uma única ação e retorne o lucro máximo que poderia ter sido obtido
 comprando ações no dia x e vendendo estoque no dia y onde y > x.
Por exemplo: se arr é [44, 30, 24, 32, 35, 30, 40, 38, 15] então seu
programa deve retornar 16 porque no índice 2 a ação valia $ 24 e no
índice 6 a ação valia $ 40 , portanto, se você comprou a ação a 24 e
vendeu a 40, teria obtido um lucro de $ 16, que é o lucro máximo que
poderia ter sido obtido com essa lista de preços de ações.
Se não houver lucro que poderia ter sido feito com os preços das
ações, seu programa deve retornar -1. Por exemplo: arr é [10, 9, 8, 2]
 então seu programa deve retornar -1.
'''

def StockPicker(arr):
    lucro_maximo = 0
    valor_minimo = arr[0]

    for i in range(0, len(arr)):
        valor_minimo = min(valor_minimo, arr[i])
        lucro = arr[i] - valor_minimo
        lucro_maximo = max(lucro_maximo, lucro)
    if lucro_maximo > 0:
        return lucro_maximo
    else:
        return -1

print(StockPicker([10, 9, 8, 2]))