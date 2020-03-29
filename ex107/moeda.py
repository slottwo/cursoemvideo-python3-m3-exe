def aumentar(price: float, tx: float):
    return price*(1+tx/100)


def descontar(price: float, tx: float):
    return price*(1-tx/100)


def dobro(price: float):
    return price*2


def metade(price: float):
    return price/2
