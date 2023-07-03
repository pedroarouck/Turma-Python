# soma, subtração, multiplicação, divisão

def soma(num1,num2):
    soma = num1 + num2
    return soma

def subtracao(num1,num2):
    subtracao = num1 - num2
    return subtracao

def multiplicacao(num1,num2):
    multi = num1 * num2
    return multi

def divisao(num1,num2):
    if num2 != 0:
        div = num1 / num2
        return div
    else:
        return False

def calculadora():
    num1 = float(input("Digite o primeiro número\n"))
    num2 = float(input("Digite o segundo número\n"))
    operador = input("Digite a operação desejada\n1 para Soma, 2 para Subtração, 3 para Multiplicação ou 4 para Divisão\n")
    if operador == "1":
        print("A soma de {} com {} é {}".format(num1,num2,soma(num1,num2)))
    elif operador == "2":
        print("A diferença entre {} e {} é {}".format(num1,num2,subtracao(num1,num2)))
    elif operador == "3":
        print("O produto entre {} e {} é {}".format(num1,num2,multiplicacao(num1,num2)))
    elif operador == "4":
        if divisao(num1,num2) != False:
            print("O quociente entre {} e {} é {}".format(num1,num2,divisao(num1,num2)))
        else:
            print("Não é possível dividir por zero")
    else:
        print("Operação inválida")
    repetir()

def repetir():
    repetir = input("Deseja realizar outra operação?\nDigite 1 para sim e 2 para encerrar\n")
    if repetir == "1":
        calculadora()
    else:
        print("Calculadora encerrada.")

calculadora()
