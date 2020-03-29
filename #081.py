# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# Situação: Completo

lista: list = []


def quer_sair(r):
    while True:
        if r in 'Ss':
            return True
        elif r in 'Nn':
            return False
        else:
            print('Não entendi. Tente novamente.')
            r = input('Pronto? [s/n] ')


while True:
    n = int(input('Digite um número inteiro: '))

    lista.append(n)

    sair = input('Pronto? [s/n] ')

    if quer_sair(sair):
        break

# A)
print(f'\nForam digitados {len(lista)} números.')

# B)
lista.sort(reverse=True)
print(f'\nA lista de números criada é: {str(lista).replace("[", "").replace("]", "")}')

# C)
if 5 in lista:
    print(f'\nO valor 5 foi digitado {lista.count(5)}')
else:
    print('\nO valor 5 não foi digitado.')
