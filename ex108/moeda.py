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
