# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
# comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use
# cores.

# Situação:


def titulo(tit: str, color: str):
    w = len(tit) + 4
    print(color, end='')
    print("~"*w)
    print(tit.center(w))
    print("~"*w)
    print("\033[m", end='')


def ajuda(cmd):
    print("\033[0:32:40m", end='')
    help(cmd)
    print("\033[m", end='')
    ler_cmd()


def ler_cmd():
    titulo("Sistema de Ajuda PyHELP", "\033[1:30:42m")

    cmd = input("Função ou biblioteca: ")
    if cmd.upper() == "FIM":
        titulo("Tchau!", "\033[1:30:41m")
        exit()
    else:
        ajuda(cmd)


ler_cmd()
