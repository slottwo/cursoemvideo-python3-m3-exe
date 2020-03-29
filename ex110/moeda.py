from ex097 import titulo
from ex108.moeda import *


def porcentagem(num: float):
    return str(num).replace('.', ',') + "%"


def resumo(price, up: float, down: float):
    aum = f"Com {porcentagem(up)} de aumento: {real(aumentar(price, 23.3))}"
    desc = f"Com {porcentagem(down)} de desconto: {real(descontar(price, 12.98))}"
    tamanho = len(aum) if len(aum) > len(desc) else len(desc)
    titulo("RESUMO", tam=tamanho)
    print(f"O preço analisado é: {real(price)}")
    print(f"O dobro é: {real(dobro(price))}")
    print(f"A metade é: {real(metade(price))}")
    print(aum)
    print(desc)
    print("~"*tamanho)
