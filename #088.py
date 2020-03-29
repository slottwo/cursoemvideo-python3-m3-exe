# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista compos-
# ta.

# Situation: Completo com 14 linhas de código.

# Imports:

from random import randint

# Variables & GUI:

jogos_gerados = []
numero_jogos = int(input("Quantos jogos devem ser gerados?"))

# Algorithm:

for i in range(numero_jogos):
    jogos_gerados.append([])
    for j in range(6):
        while True:
            n = randint(1, 60)
            if n not in jogos_gerados[i]:
                jogos_gerados[i].append(n)
                break
for k in jogos_gerados:
    k.sort()
    print(str(k).replace("[", "").replace("]", ""))
