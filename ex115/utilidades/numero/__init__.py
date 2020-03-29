def leia_int(msg: str):
    num_txt = input(msg)
    try:
        num_int = int(num_txt)
    except ValueError:
        print(f"\033[0;31;48mERRO: O \"número\" \033[0;33;48m{num_txt}\033[0;31;48m é inválido.", end='')
        return leia_int("Por favor, tente novamente: \033[m")
    else:
        return num_int


