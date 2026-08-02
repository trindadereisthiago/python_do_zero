lista_alunos = []

sair = False

while sair is not True:
    nome = input("Digite o nome: \n")
    idade = int(input("Digite a idade: \n"))
    lista_alunos.append({"nome": nome, "idade": idade})

    opcao = input("Deseja sair? (S/N)")
    if opcao.lower() == "s":
        sair = True
for a in lista_alunos:print(a)