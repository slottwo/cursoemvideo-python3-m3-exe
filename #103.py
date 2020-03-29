# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

# Situação: Completo


def ficha(nome="<desconhecido>", qnt_gols=0):
    print("Nome do jogador: ", nome)
    print("Gols: ", qnt_gols)


jogador = input("Digite o nome do jogador: ")
gols = input("E quantos gols ele fez: ")

if jogador != '':
    if gols != '':
        ficha(jogador, int(gols))
    else:
        ficha(jogador)
else:
    if gols != '':
        ficha(qnt_gols=int(gols))
    else:
        ficha()
