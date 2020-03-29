# Imports
from menu import *
from utilidades.arquivo import *

# Docstring

# Var
arquivo = 'dados.txt'
opcoes = [["Ver pessoas cadastradas", mostrar_pessoas], ["Cadastrar pessoas", cadastrar]]

# Init
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

menu(opcoes, arquivo)
