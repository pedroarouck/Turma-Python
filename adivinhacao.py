print("Bem-vindo ao jogo da adivinhação")

numero_magico = 42

total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Tente adivinhar o numero magico, faça um chute\n"))

    if(chute == numero_magico):
        print("Acertou")
        break
    elif(chute > numero_magico):
        print("Errou, chutou alto")
    else:
        print("Errou, chutou baixo")

    rodada = rodada + 1
