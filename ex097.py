def titulo(tit: str, sub_tit: str = '', tam=0, cor="\033[1:30:48m"):
    if tam == 0:
        if len(tit) > len(sub_tit):
            if len(sub_tit) == 0:
                tam = 3 * len(tit) // 2
            else:
                tam = 2 * len(tit) - len(sub_tit)
        else:
            tam = 3 * len(sub_tit) // 2
    print(cor, end='')
    print('~' * tam)
    print(tit.center(tam))
    print('~' * tam)
    if sub_tit != '':
        if cor[4] == '1':
            print(cor.replace('1', '0'))
        print(' ' * (tam - len(sub_tit) - 1) + sub_tit + ' ')
        print('~' * tam)
    print(cor, end='')


# titulo('Lá e de volta outra vez')
# print('\n\n')
# titulo('Lá e de volta outra vez', '~ Um conto de Bilbo Bolseiro')
# print('\n\n')
# titulo('Lá e de volta outra vez', '~ Bilbo Bolseiro')
