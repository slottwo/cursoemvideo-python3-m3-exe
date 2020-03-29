# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Resolvido!

lista: list = []  # Declarando a lista principal vazia a princípio

for c in range(5):  # Inserção de dados pelo usuário
    lista += [int(input(f"Digite o {c + 1}º de 5 números: "))]

maior = max(lista)
menor = min(lista)


def buscador_de_valor(valor, tipo):
    ls_pos_var: list = []  # Posições em que o maior valor aparece

    proximo = lista.index(valor)  # Próximo valor a ser guardado em ls_pos_var
    ls_pos_var += [proximo + 1]  # Não seria conveniente colocar a inserção das posições na primeira linha do laço já
    # que no último valor de proximo não seria adicionado.

    for i in range(lista.count(valor) - 1):  # Número de vezes em que aparece
        proximo = lista.index(valor, proximo + 1)  # Para que comece a procura a partir do último valor encontrado
        ls_pos_var += [proximo + 1]

    # Aqui é mostrado o valor e a primeira posição sem quebrar a linha no final permitindo impressão de próximos
    # valores se houverem.

    print(f"\nO {tipo} valor, {valor}, apareceu como o ", end='')

    for i in ls_pos_var:
        print(f"{i}º", end='')
        if ls_pos_var.index(i) + 1 == len(ls_pos_var) - 1:  # Verificando se o valor i é o penúltimo pois se só houvesse
            # 1 item [-2] sairia do range.
            print(" e ", end='')
        elif i != ls_pos_var[-1]:
            print(", ", end='')
        else:
            print(".", end='')


buscador_de_valor(maior, 'maior')
buscador_de_valor(menor, 'menor')
