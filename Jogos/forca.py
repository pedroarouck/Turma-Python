import random
import menu

def jogar():
    mensagem_de_abertura()
    palavra_secreta = pega_palavras_secretas()
    letras_acertadas = configura_letras_acertadas(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    while (not acertou and not enforcou):
        chute = pedir_chute()
        if (chute in palavra_secreta):
            chute_certo(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
        print(letras_acertadas)

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

    if (acertou):
        mensagem_vitoria()
        menu.chama_menu()
    else:
        mensagem_derrota()
        menu.chama_menu()


def mensagem_de_abertura():
    print("Bem vindo ao jogo da forca")


def pega_palavras_secretas():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def configura_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def pedir_chute():
    chute = input('Qual letra?\n').upper()
    return chute


def chute_certo(chute, palavra_secreta, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def mensagem_vitoria():
    print('Voce ganhou')

def mensagem_derrota():
    print('Voce foi enforcado')