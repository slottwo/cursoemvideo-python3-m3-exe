# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média


def sair():
    r = input("Continuar? [Sn] ")
    if r not in "SsNn" or r == "":
        print("Resposta Inválida. Tente novamente.")
        return sair()
    elif r in "Ss":
        return False
    else:
        return True


pessoas = list()
while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo[MF]: ').capitalize()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)
    pessoa.clear()
    if sair():
        break

# A)

print('Quantidade de pessoas:', len(pessoas))

# B)

idade_mid = sum([p['idade'] for p in pessoas])/len(pessoas)
print('Idade Média:', idade_mid)

# C)

print('Mulheres:')
for p in pessoas:
    if p['sexo'] == 'F':
        print('>', p['nome'])

# D)

print('Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > idade_mid:
        print('>', p['nome'])
