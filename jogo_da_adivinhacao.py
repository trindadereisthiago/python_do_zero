import random

def mensagem():
    print("Bem-vindo ao jogo da adivinhação.\n")
    print("Adivinhe o número secreto entre 1 a 20.\n")
    print("Você tem 1.000.000 de aura.\n")
    print("Quer jogar?\n")

def chute():
    numero = int(input("Qual seu chute? "))
    return numero

def main():

    numero = random.randint(1, 10)
    aura = 1000000
    tentativas = 5

    mensagem()

    while tentativas != 0:    
        palpite = chute()
        if palpite != numero:
            aura -= 200000
            print("Errou. Perdeu aura. - 20.000 de aura.\n")
            print(f"Aura: {aura}")
            tentativas -= 1

        if aura == 0:
            print(f"O número era: {numero}")
            print(f"Sua aura: {aura}")

        if palpite == numero:
            print("Parabéns, você acertou!!!")
            print(f"O número era {numero}.")
            break

main()