# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga
# mostrar os números como um valor monetário formatado.

# Situação: Completo

from ex108.moeda import *

preco = decimal(input("Digite o preço: R$ "))
print(f"O dobro é {real(dobro(preco))}")
print(f"A metade é {real(metade(preco))}")
print(f"Com um aumento de 12% o preço se torna {real(aumentar(preco, 12))}")
print(f"E com 33,3% de desconto, {real(descontar(preco, 33.3))}")
