# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.

# Situação: Completo


def fatorial(n, show, pri=True):
    if pri:
        print("Calculando...\n")
    if n == 0 or n == 1:
        if show:
            print(f"{n} = ", end='')
        return 1
    else:
        if show:
            print(f"{n} x ", end='', flush=False)
        f = n * fatorial(n-1, show, False)
        if pri and show:
            print(f)
        return f


num = int(input("Digite um número inteiro: "))
mostrar = True if input("Deseja ver o cálculo?[Sn] ") in "Ss" else False
print(f"\nO fatorial de {num} é {fatorial(num, mostrar)}")
