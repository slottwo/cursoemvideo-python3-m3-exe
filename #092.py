# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com
# idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Situação: Completo

ano = 2019
pessoa = dict()


def ano_decimal(lista: list):
    l = list(map(int, lista))
    return l[2] + l[1]/12 + l[0]/365


def inscricao(p: dict):
    p['Nome'] = input('Nome: ').capitalize()
    p['Sexo'] = input('Sexo: [F/m] ').upper()
    p['Nascimento'] = input('Data de nascimento: [DD/MM/AAAA] ').split('/')
    p['Idade'] = int(round(ano - ano_decimal(p['Nascimento']), 0))
    if input('Tens carteira de trabalho? [S/n] ') in 'Ss':
        r = int(input("CTPS: "))
    else:
        r = 0
    p['CTPS'] = r
    if p['CTPS'] != 0:
        p['Contratacao'] = int(input('Ano de contratação: [AAAA] '))
        p['Aposentadoria'] = p['Idade'] + (p['Contratacao'] + 30 - ano) + 5 if p['Sexo'] == 'M' else 0
    else:
        p['Aposentadoria'] = 65 if p['Sexo'] == 'M' else 60


inscricao(pessoa)
print()
for k, v in pessoa.items():
    if k == 'Nascimento':
        print(f"{k}: ", end='')
        for i in v:
            print(f"{'0' if len(i) == 1 else ''}{i}", end="/" if len(i) != 4 else "\n")
    else:
        print(f"{k}: {v}")
