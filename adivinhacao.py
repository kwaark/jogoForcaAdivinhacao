from random import randint

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")
    numero_secreto = (randint(1, 100))
    total_de_tentativas = 0
    pontos = 2000

    print("Qual o nivel de dificuldade?")
    print("(1)Facil (2)Medio (3)Dificil")

    nivel = int(input("Define nivel: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("\n>>> Tentativa {} de {}".format(rodada, total_de_tentativas))
        print(">>> Você digitou" , chute_str)
        chute = int(chute_str)
        trapaca = (chute == 112233)

        if (trapaca):
            print("\n>>>TRAPAÇA<<<\nO numero secreto é ", numero_secreto, " :D", "\n")
            continue

        if(chute < 1 or chute > 100):
            print("OBS: Você deve digitar um numero entre 1 e 100\n")
            continue

        acertou = (chute == numero_secreto)
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos, parabéns !".format(pontos))
            break
        else:
            if(maior):
                print("AVISO: O seu chute foi maior que o numero secreto")
            elif(menor):
                print("AVISO: O seu chuto foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("Pontuaçao atual: ", pontos,"\n")
    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()