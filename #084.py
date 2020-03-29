# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No
# final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Situação: Completo ... eu acho.

ls_pessoas = list()
pessoa = list()

while True:
    pessoa.append(input("Nome: ").lower().capitalize())
    pessoa.append(float(input("Peso: ")))
    ls_pessoas.append(pessoa[:])
    pessoa.clear()
    if input("Continue? ") in "Nn":
        del pessoa
        break

print("="*40)

# A)

print(f"Você cadastrou {len(ls_pessoas)} pessoas")

# B) & C)

pesos = []

for pessoa in ls_pessoas:
    pesos += [pessoa[1]]

maior_peso = max(pesos)

menor_peso = min(pesos)

pessoas_pesadas = []

pessoas_leves = []

for pessoa in ls_pessoas:
    if pessoa[1] == maior_peso:
        pessoas_pesadas.append(pessoa[0])

for pessoa in ls_pessoas:
    if pessoa[1] == menor_peso:
        pessoas_leves.append(pessoa[0])

# B)

print(f"O maior peso foi ", end='')
print(maior_peso, "kg de ", end='')

for pessoa in pessoas_pesadas:
    print(pessoa, end='')
    print(".\n" if pessoa == pessoas_pesadas[-1] else ", " if pessoa != pessoas_pesadas[-2] else " e ", end='')

# C)

print(f"O menor peso foi ", end='')
print(menor_peso, "kg de ", end='')

for pessoa in pessoas_leves:
    print(pessoa, end='')
    print(".\n" if pessoa == pessoas_leves[-1] else ", " if pessoa != pessoas_leves[-2] else " e ", end='')
