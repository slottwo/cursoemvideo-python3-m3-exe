# Imports
from utilidades.arquivo import *
from utilidades.interface import *
from utilidades.numero import *


# Docstring

# Functions
def menu(opcoes: list, arquivo: str):
    tamanho = 35

    titulo("MENU PRINCIPAL", tamanho)
    for opcao in opcoes:
        print(f"\033[0;33;48m{opcoes.index(opcao)+1} - \033[0;34;48m{opcao[0]}")
    print(f"\033[0;33;48m{len(opcoes)+1} -\033[0;34;48m Sair do sistema\033[m")
    linha(tamanho)
    escolha = leia_int("\033[0;33;48mSua Opção: \033[m")-1
    while True:        
        if escolha in range(len(opcoes)+1):
            if escolha == len(opcoes):
                titulo("Saindo do sistema... Ate mais!", tamanho)
                exit()
            titulo(opcoes[escolha][0], tamanho)
            opcoes[escolha][1](arquivo)
            break
        else:
            escolha = leia_int("Opção inválida. Por favor, tente novamente: ")-1
    menu(opcoes, arquivo)

