# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.

# Situação: Quase Completo (Falta sistema de busca)


def sair():
    r = input("Continuar? [Sn] ")
    if r not in "SsNn" or r == "":
        print("Resposta Inválida. Tente novamente.")
        return sair()
    elif r in "Ss":
        return False
    else:
        return True


jogadores = list()

while True:
    jogador = {'nome': input('Insira o nome do jogador(a): '),
               'partidas': int(input('Quantas partidas ele(a) jogou? '))}
    jogador['gols'] = [int(input(f'Quantos gols ele(a) fez na {i + 1}ª partida? ')) for i in range(jogador['partidas'])]

    jogadores.append(jogador.copy())

    jogador.clear()

    if sair():
        break

del jogador

for j in jogadores:
    print('\n\nNOME DO JOGADOR(A):', j['nome'])

    print('\nPARTIDAS:', end='')
    for i in range(j['partidas']):
        print(str(i).center(5), end='')

    print('\nGOLS:    ', end='')
    for gols in j['gols']:
        print(str(gols).center(5), end='')

    print('\n\nTOTAL DE GOLS NO CAMPEONATO:', sum(j['gols']))
