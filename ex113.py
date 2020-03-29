# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# Situação: Com erros

from ex097 import titulo


def leia_int(num_txt: str):
    try:
        num_int = int(0 if num_txt == '' else num_txt)
    except ValueError:
        print(f"\033[1;31;48mERRO!\033[0;31;48m O \"inteiro\" \033[0;32;48m{num_txt}\033[0;31;48m está invalido.\033[m")
    else:
        return num_int


def leia_float(num_txt: str):
    try:
        num_float = float(0 if num_txt == '' else num_txt.replace(",", "."))
    except ValueError:
        print(f"\033[1;31;48mERRO!\033[0;31;48m O \"inteiro\" \033[0;32;48m{num_txt}\033[0;31;48m está invalido.\033[m")
        raise ValueError
    else:
        return num_float


def ler(msg: str, func):
    try:
        saida = func(input(msg))
    except ValueError:
        ler(msg, func)
    else:
        return saida


def test(opção=''):
    if opção == '':
        tamanho = 25
        titulo("Leitor", tam=tamanho, cor="\033[1:30:48m")
        print("1 - Ler número inteiro")
        print("2 - Ler número racional")
        print("~"*tamanho)
        opção = ler("Digite sua opção: ", leia_int)

    if opção == 1:
        funcao = leia_int
    elif opção == 2:
        funcao = leia_float
    else:
        print("\033[1;31;48mOpção Inválida.", end='')
        opção = ler(" \033[1:30:48mTente novamente: ", leia_int)
        test(opção)
        funcao = None

    num_txt = input(f"Insira um número {'inteiro' if funcao == leia_int else 'racional'}: ")
    num = funcao(num_txt)
    return num


x = test()
print(f"\033[1;30;48mO número \033[1;34;48m{x}\033[1;30;48m foi lido com sucesso!")
