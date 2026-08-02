soma = 0
sair = False

while sair is not True:
    numero = int(input("Digite um número limite para uma contagem: "))
    for soma in range(numero+1):
        print(soma)

    encerrar = input("Quer sair? (S/N)\n")
    if encerrar.lower() == "s":
        sair = True