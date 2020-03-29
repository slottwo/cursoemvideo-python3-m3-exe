# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
# crescente.

numeros = [[], []]

for c in list(range(7)):
    while True:
        try:
            n = int(input(f"Digite o {c+1}º número inteiro: "))
            if n in numeros[0] or n in numeros[1]:
                raise ZeroDivisionError
            if n % 2 == 1:
                numeros[0].append(n)
            else:
                numeros[1].append(n)
            break
        except ValueError:
            print("Você não digitou um número inteiro. Tente novamente.")
        except ZeroDivisionError:
            print("Você já digitou este número. Por favor insira outro número.")


numeros[0].sort()
numeros[1].sort()

print("Os números ímpares digitados foram: ", end='')
for n in numeros[0]:
    print(n, end=''), print(", " if n != numeros[0][-1] else ".\n", end='')

print("Os números pares digitados foram: ", end='')
for n in numeros[1]:
    print(n, end=''), print(", " if n != numeros[1][-1] else ".\n", end='')
