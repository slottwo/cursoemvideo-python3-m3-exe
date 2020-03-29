# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo
# teclado. No final, mostre a matriz na tela, com a formatação correta.

# Situação: Solucionado (E pomposo)

matriz = [[], [], []]
max_matriz = int()
max_digits = int()

for linha in range(3):
    for coluna in range(3):
        while True:
            try:
                cel = int(input(f"Insira a célula ({linha+1}, {coluna+1}): "))
                break
            except ValueError:
                print("Tente novamente.")
        matriz[linha].append(cel)
    max_linha = max(matriz[linha])
    max_matriz = max_linha if max_linha > max_matriz else max_matriz

max_digits = len(str(max_matriz))

for linha in matriz:
    for cel in linha:
        print("[" + str(cel).center(max_digits+2) + "]", end='')
    print()
