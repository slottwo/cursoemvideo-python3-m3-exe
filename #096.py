# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

# Situação: Completo


def inputting(nome: str, un: str = 'm'):
    return float(input(f"{nome}({un}): ").replace(',', '.'))


def area(x=inputting('Largura'), y=inputting('Comprimento')):
    print(f"Seu terreno tem {x}m por {y}m")
    print(f"A área do terreno é: {x * y:.6}m²\nE o perímetro é: {2 * (x + y)}m")


area()
