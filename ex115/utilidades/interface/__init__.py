def titulo(tit: str, tam: int, color: str = "\033[1;38;48m"):
    linha(tam)
    print(color + tit.center(tam) + "\033[m")
    linha(tam)


def linha(tam):
    print('-'*tam)

