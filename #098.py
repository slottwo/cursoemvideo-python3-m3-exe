# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# Situação: Completo (Eu acho, talvez precise de mais testes...)

"""
def oposto(lista: list):
    neg_l = list()
    for i in lista:
        neg_l.append(-i)
    return neg_l
"""


def contador(step=1, init=1, end=10):

    if step == 0:
        return []
    elif step < 0:
        init, end, step = -end, -init, -step
        rev = True
        if step == 2:
            end = 0
    else:
        if init > end:
            init, end = -init, -end
            rev = True
        else:
            rev = False

    print(step, init, end)

    n = init
    contagem = []
    while n <= end:
        contagem.append(n)
        n += step

    print(contagem)

    if rev:
        # contagem = oposto(contagem)
        contagem = list(map(lambda x: -x, contagem))

    print(contagem)

    return contagem


'''
# A)

print(contador())

# B)

print(contador(-2))
'''
# C)

tit = "Contagem Personalizada"
print("~"*(len(tit)+2) + f"\n {tit} \n" + "~"*(len(tit)+2))
for i in list(contador(int(input("Passo: ")), int(input("Início: ")), int(input("Fim: ")))):
    print(f"{i}...")
