# Exercicio Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas.

# Situação: Completo

lista, impares, pares = [], [], []

while True:
    x = int(input("Digite um número inteiro: "))
    if x not in lista:
        lista.append(x)
        if x % 2 == 0:
            pares.append(x)
        else:
            impares.append(x)
        sair = input("Pronto? [s/n] ")
    else:
        print("Você já digitou esse número")
        sair = input("Já terminou? [s/n]")

    if sair in "Ss":
        break

print(f"A sua lista tem os seguintes números: {str(lista).replace('[', '').replace(']', '')}")
print(f"Dos quais {str(impares).replace('[', '').replace(']', '')} são ímpares")
print(f"E {str(pares).replace('[', '').replace(']', '')} são pares")
