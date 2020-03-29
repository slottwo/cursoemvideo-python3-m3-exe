# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

# Situação: Completo

import urllib.request

endereço = input("Digite a url de um site: ")

try:
    print("Carregando...")
    site = urllib.request.urlopen(endereço)
except urllib.error.URLError:
    print("Desculpe. Esse site está fora do ar.")
else:
    print("Site carregado com sucesso")
