# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Situação: Completo com 20 linhas de código.

# Variáveis e Constantes
matriz = [[], [], []]
soma_pares = soma_col_3 = max_line_2 = 0

# Aproveitando o exercício anterior:

for linha in range(3):
    for coluna in range(3):
        while True:
            try:
                matriz[linha].append(int(input(f"Insira a célula ({linha + 1}, {coluna + 1}): ")))
                break
            except ValueError:
                print("Tente novamente.")

print("\n")
for linha in matriz:
    for cel in linha:
        print(f"[{cel:^5}]", end='')
        if cel % 2 == 0:  # A)
            soma_pares += cel
    print()
    soma_col_3 += linha[2]  # B)
print("\n")

# A)
"""
for linha in matriz:
    for cel in linha:
        if cel % 2 == 0:
            soma_pares += cel
"""
print(f"A soma dos valores pares da matriz é {soma_pares}.")

# B)
"""
for linha in matriz:
    soma_col_3 += linha[2]
"""
print(f"A soma dos valores da 3ª coluna é {soma_col_3}.")

# C)

print(f"O maior valor da 2ª linha é {max(matriz[1])}")
