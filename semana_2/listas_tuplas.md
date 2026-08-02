# Listas, Tuplas

## Listas
- Como criar listas em python:

`alunos = ["Ana", "Bruno", "Carla"]`

- Adicionar itens:

`alunos.append("Diego")` adiciona ao final da lista
`alunos.remove("Bruno")` remove item
`alunos.sort()` ordena a lista

- Percorrer uma lista

```
for alunos in alunos:
    print(aluno)
```

## Tuplas
O que muda?
Listas podem ser alteradas.
Tuplas são imutáveis.

- Tupla
`tupla = (1, 2, 3)

## Dicionários

```
aluno = {
    "nome": "Ana",
    "idade": 18,
    "curso": "Dev de Sistemas"
}
```
Acesse com `aluno["aluno"]` pela chave, não pela posição.

- Acessando e atualizando

```
print(aluno["nome"]) --> Ana
aluno["idade"] = 19 #atualiza
aluno["email"] = "user@mail.com" #adiciona
```
-- Lista de dicionários

```
alunos = [
    {"nome": "Ana", "Idade": 18},
    {"nome": "Karla", "Idade": 15}
]
```

- Lista de listas

```
notas = [
    ["Ana", 8.5, 9.0],
    ["Bruno", 7.0, 6.5]
]
```