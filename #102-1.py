# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.

# Situação: Completo


def fat(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f"{c} x ", end='')
            else:
                print(f"{c} = ", end='')
        f *= c
    print(f)
    return f


num = int(input("Digite um número inteiro: "))
mostrar = True if input("Deseja ver o cálculo?[Sn] ") in "Ss" else False
print(f"\nO fatorial de {num} é {fat(num, mostrar)}")


