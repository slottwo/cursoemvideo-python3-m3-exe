# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior

# Situação: Concluído

from random import randint
from time import sleep


def sorteia():
    lista = []
    for i in range(5):
        lista.append(randint(0, 100))
    return lista


def soma_par(lista: list):
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    return s


print("A lista sorteada é: ", end='')
nums = sorteia()
for n in nums[:-1]:
    sleep(0.5)
    print(n, end=', ', flush=True)
sleep(0.5)
print(f" {nums[-1]}!")
print("E a soma dos números pares", end=' ')
numsPar = list(filter(lambda x: x % 2 == 0, nums))
for n in numsPar[:-1]:
    sleep(0.5)
    print(n, end=', ', flush=True)
print(numsPar[-1], end=' ')
print("é:", soma_par(nums))
