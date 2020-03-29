# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Situação:

jogador: dict = {'nome': input('Insira o nome do jogador(a): '),
                 'partidas': int(input('Quantas partidas ele(a) jogou? '))}

jogador['gols'] = [int(input(f'Quantos gols ele(a) fez na {i+1}ª partida? ')) for i in range(jogador['partidas'])]

print('\n\nNOME DO JOGADOR(A):', jogador['nome'])

print('\nPARTIDAS:', end='')
for i in range(jogador['partidas']):
    print(str(i).center(5), end='')

print('\nGOLS:    ', end='')
for gols in jogador['gols']:
    print(str(gols).center(5), end='')

print('\n\nTOTAL DE GOLS NO CAMPEONATO:', sum(jogador['gols']))
