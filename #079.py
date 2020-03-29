# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista: list = []
sair = False

while not sair:
    temp = int(input('Digite um número: '))
    if temp in lista:
        print(f'{temp} já está na lista, logo não será adicionado.')
    else:
        lista.append(temp)
    while True:  # Desnecessário, veja Anexo 1
        quer_sair = input('Deseja sair? [s/n] ').lower()

        if quer_sair == 's':
            sair = True
            break
        elif quer_sair == 'n':
            sair = False
            break
        else:
            print('Desculpe-me não entendi. Tente novamente.')

lista.sort()

print('\nA sua lista é: ', str(lista).replace('[', '').replace(']', ''))

# Anexos

# :1:





