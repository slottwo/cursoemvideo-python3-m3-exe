# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# Situação: Feito!

from random import randint

numeros = randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000)

# maior = 0
# for i in range(len(numeros)-1):
# 	if numeros[maior] >= numeros[i+1]:
# 		continue
# 	else:
# 		maior = i+1
#
# menor = 0
# for i in range(len(numeros)-1):
# 	if numeros[menor] <= numeros[i+1]:
# 		continue
# 	else:
# 		menor = i+1
#
# maior_valor = numeros[maior]
# menor_valor = numeros[menor]

maior_valor = max(numeros)
menor_valor = min(numeros)

print(f'A lista de 5 números entre 0 e 1000 gerados aleatoriamente é {str(numeros).replace("(", "").replace(")", "")}.')
print(f'O maior número da lista é {maior_valor} e o menor {menor_valor}.')
