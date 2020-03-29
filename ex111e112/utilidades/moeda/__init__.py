from ex097 import titulo


def aumentar(price: float, tx: float):
    return price*(1+tx/100)


def descontar(price: float, tx: float):
    return price*(1-tx/100)


def dobro(price: float):
    return price*2


def metade(price: float):
    return price/2


def real(num: float):
    return "R$ " + str(round(num, 2)).replace('.', ',')


def decimal(num: str):
    return round(float(num.replace(',', '.')), 2)


def porcentagem(num: float):
    return str(num).replace('.', ',') + "%"


def resumo(price, up: float, down: float):
    # Aumento e desconto: formatação
    aum = f"Com {porcentagem(up)} de aumento: {real(aumentar(price, 23.3))}"
    desc = f"Com {porcentagem(down)} de desconto: {real(descontar(price, 12.98))}"
    # Tamanho do maior print de resumo() para utilizar em titulo e cosméticos
    tamanho = len(aum) if len(aum) > len(desc) else len(desc)

    titulo("RESUMO", tam=tamanho)
    print(f"O preço analisado é: {real(price)}")
    print(f"O dobro é: {real(dobro(price))}")
    print(f"A metade é: {real(metade(price))}")
    print(aum)
    print(desc)
    print("~"*tamanho)
