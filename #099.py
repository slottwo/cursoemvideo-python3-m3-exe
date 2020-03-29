# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Situação:


def maior(*num):
    if len(num) < 2:
        m = num[0]
    elif len(num) == 2:
        if num[0] > num[1]:
            m = num[0]
        else:
            m = num[1]
    else:
        m: int = maior(num[0], num[1])
        for n in num[2:]:
            m = maior(m, n)
    return m


print(maior(1, 13))
print(maior(0, 20, 3))
print(maior(-273, 0, -0.5))
print(maior(32, 2, 4, 20, 100))
print(maior(32, 2, 4, 20, 100, 12345, 1024, maior(-12, 9, 54321)))
