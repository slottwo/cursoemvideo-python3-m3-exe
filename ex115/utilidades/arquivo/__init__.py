#Imports
from utilidades.numero import leia_int

# Docstring



#Functions
def arquivo_existe(nome_arq: str):
    try:
        tmp_arq = open(nome_arq, 'rt')  # r=read, t=text
        tmp_arq.close
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome_arq: str):
    try:
        tmp_arq = open(nome_arq, 'wt+')  # w=write, t=text, +=creat if not found
        print(f'Arquivo {nome_arq} criado com sucesso.')
    except:
        print(f'Não foi possível criar o arquivo {nome_arq}.')

def ler_arquivo(nome_arq: str):
    try:
        arq = open(nome_arq, 'rt')
    except:
        return 'Erro ao ler arquivo.'
        if not arquivo_existe(nome_arq):
            criar_arquivo(nome_arq)
    else:
        return arq.readlines()


def escrever_no_arquivo(nome_arq: str, nome_pessoa: str, idade: int):
    try:
        arq = open(nome_arq, 'at')
    except:
        print(f"Houve um erro na abertura do arquivo {nome_arq}")
        if not arquivo_existe(nome_arq):
            criar_arquivo(nome_arq)
            escrever_no_arquivo(nome_arq. nome_pessoa, idade)
    else:
        try:
            arq.write(f"{nome_pessoa}:{idade}\n")
        except:
            print(f"Houve m erro ao escrever no arquivo {nome_arq}")
            return False
        else:
            return True


def cadastrar(nome_arq):
    # print("Nada ainda ._.")
    nome_pessoa = input("Nome: ").capitalize()
    while nome_pessoa == '':
        nome_pessoa = input("Nome inválido, tente novamente: ").capitalize()
    idade = leia_int("Idade: ")
    if escrever_no_arquivo(nome_arq, nome_pessoa, idade):
        print(f"{nome_pessoa} cadastrado com sucesso!")


def mostrar_pessoas(nome_arq):
    if arquivo_existe(nome_arq):
        pessoas = ler_arquivo(nome_arq)
        if not pessoas == []:
            print("\033[1;34;48mNome" + " "*(35-len("NomeIdade")) + "Idade\033[m")
            for pessoa in pessoas:
                dados = pessoa.split(":")
                print(dados[0] + " "*(35 - (len(pessoa)-2)) + dados[1], end='')
        else:
            print("Está meio vazio aqui ._.")
    else:
        criar_arquivo(nome_arq)
        mostrar_pessoas(nome_arq)

