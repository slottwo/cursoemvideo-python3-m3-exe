from ex111e112.utilidades.moeda import decimal


def is_num(num: str):
    try:
        float(num)
    except ValueError:
        return False
    return True


def leia_dinheiro(msg: str):
    dinheiro = input(msg).rstrip(" ").rstrip(" ").replace(",", ".")
    if not is_num(dinheiro):
        print(f"\033[1;31;48mErro! {dinheiro} é um preço inválido. Tente novamente.\033[m")
        return leia_dinheiro(msg)
    else:
        return decimal(dinheiro)
