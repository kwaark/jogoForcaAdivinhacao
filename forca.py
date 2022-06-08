import random

def jogar():
    imprimir_menssagem_abertura()
    palavra_secreta = carrega_palavra_secreta_txt()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #Enquanto(True)
    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        mensagem_ganhador(palavra_secreta)
    else:
        mensagem_perdedor(palavra_secreta)

    print("Fim do jogo!")


def imprimir_menssagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************\n")

def carrega_palavra_secreta_txt():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_ganhador(palavra_secreta):
    print("\nVocê ganhou! :D\n")
    print("A palavra secreta é:", palavra_secreta, "\n")

def mensagem_perdedor(palavra_secreta):
    print("\nVocê perdeu! :(\n")
    print("A palavra secreta é:", palavra_secreta, "\n")

if (__name__ == "__main__"):
    jogar()