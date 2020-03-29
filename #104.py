# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

# Situação: Completo


def leia_int(msg: str):
    num_txt = input('\033[0:30:48m'+msg)
    if num_txt.isnumeric():
        return int(num_txt)
    else:
        print('\033[1:31:48mERRO! Desculpe, você não digitou um número inteiro. Tente Novamente\033[0:30:48m')
        return leia_int(msg)


n = leia_int("Digite um numero inteiro: ")
print(n)
