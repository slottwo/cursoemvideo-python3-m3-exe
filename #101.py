# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.

# Situação:

from datetime import datetime

ano = datetime.now().year


def voto(nasc):
    idade = ano - nasc
    if idade >= 16:
        if idade < 18 or idade > 70:
            return "Opcional"
        else:
            return "Obrigatório"
    else:
        return "Negado"


print("Seu voto é " + voto(int(input("Ano de Nascimento: "))))
