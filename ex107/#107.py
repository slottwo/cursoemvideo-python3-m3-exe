# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Situação: Completo

from ex107.moeda import *

preco = float(input("Digite o preço: R$ ").replace(',', '.'))
print(f"O dobro é R$ {round(dobro(preco), 2)}")
print(f"A metade é R$ {round(metade(preco), 2)}")
print(f"Com um aumento de 12% o preço se torna R$ {round(aumentar(preco, 12), 2)}")
print(f"E com 33,3% de desconto, R$ {round(descontar(preco, 33.3), 2)}")
