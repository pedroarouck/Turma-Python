# lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]
#Imprima o maior elemento;
#Imprima o menor elemento;
#imprima os números pares;
#imprima o número de ocorrências do primeiro elemento da lista;
#imprima a média dos elementos;
#imprima a soma dos elementos de valor negativo

lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

#inicializando as nossas variáveis
maiorValor = lista[0]
menorValor = lista[0]
listaPares = []
ocorrenciaItem1 = 0
mediaValores = 0
somaNegativos = 0

#inciando nosso loop
for index in range(0,len(lista)):
    #maior valor
    if maiorValor < lista[index]:
        maiorValor = lista[index]

    #menor valor
    if menorValor > lista[index]:
        menorValor = lista[index]

    #numeros pares
    if lista[index] % 2 == 0:
        listaPares.append(lista[index])

    #numero de ocorrencias do primeiro item
    if lista[index] == lista[0]:
        ocorrenciaItem1 += 1

    #soma negativos
    if lista[index] < 0:
        somaNegativos = somaNegativos + lista[index]

    #media dos valores
    mediaValores = mediaValores + lista[index]

mediaValores = mediaValores / len(lista)

print(maiorValor)
print(menorValor)
print(listaPares)
print(ocorrenciaItem1)
print(mediaValores)
print(somaNegativos)
