# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.

# Situação:

from random import randint

jogadores = dict()
podio = dict()

# "Rolagem dos dados"
for i in range(1, 5):
    jogadores['j'+str(i)] = randint(1, 20)

# print(jogadores)

# Valores rodados
rolls = sorted([v for v in jogadores.values()], reverse=True)
# print(rolls)

# Guardando temporariamente jogadores organizados por valor
for k, v in jogadores.items():
    podio[v] = k
# print(podio)

# Apagando o conteúdo de 'jogadores' para preenchê-lo com os valores já organizados em rolls
jogadores.clear()
# print(jogadores)

for i in rolls:
    jogadores[podio[i]] = i
# print(jogadores)

n = 0
for k, v in jogadores.items():
    print(f"{n}º lugar: {k} com {v}")
