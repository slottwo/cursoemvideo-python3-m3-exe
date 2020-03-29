# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No
# final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Situação: Completo.

t = int(input("Digite o 1º número: ")), int(input("Digite o 2º número: ")), int(input("Digite o 3º número: ")), int(
    input("Digite o 4º número: "))

# temp var
txt = str(t).replace('[', '').replace(']', '')
txt = txt[:txt.rfind(',')] + ' e' + txt[txt.rfind(',')+1:]

print(f"\nValores digitados {txt}")

del txt

# A)

noves_p_extenso = ('nenhuma vez', 'uma vez', 'duas vezes', 'três vezes', 'quatro vezes')[t.count(9)]
# Sei que não precisava...
print(f"\nO número 9 apareceu {noves_p_extenso}.\n")

# B)
if 3 in t:
    print(f"A primeira vez que o valor 3 apareceu foi na {t.index(3) + 1}ª posição")
else:
    print("O valor 3 não apareceu.")

# C)

print("")  # Isso foi só para o "C)" não juntar com o codigo antigo.

# Meus erros...
# # Não pode!
# pares = []
# for i in t:
#    if int(i) % 2 == 0:
#        pares += [int(i)]
#
# if pares: print("\nDos números que você digitou, os seguintes são pares: " + str(pares).replace('[', '').replace(
# ']', '') + ".")
# else: print("\nVocê não inseriu números pares.")

# t_pares = t[0] if t[0] % 2 == 0 else None, t[1] if t[1] % 2 == 0 else None, t[2] if t[2] % 2 == 0 else None, \
#          t[3] if t[3] % 2 == 0 else None

# t_pares = t[0] if t[0] % 2 == 0 else '', t[1] if t[1] % 2 == 0 else '', t[2] if t[2] % 2 == 0 else '', \
#          t[3] if t[3] % 2 == 0 else ''
#
# if t_pares != (None, None, None, None):
#     print("Dos números que você digitou, os seguintes são pares: ",
#           str(t_pares).replace('(', '').replace(')', '').replace(', None', '', 4).replace('None', ''))
# else:
#     print("Você não inseriu números pares.")

# Na verdade esquece tudo isso, descobri que não era necessário criar uma tupla, algo que já havia feito antes mas...
# sla, era só fazer um for simples como em outros projetos e imprimir quando fosse par. Grrrrrrrrr!

print("Dos números que você digitou ", end='')

# temp vars
txt = ''
c = 0

for i in t:
    if i % 2 == 0:
        if c == 0:
            txt += f"Os seguintes são pares: {i}"
        else:
            txt += f", {i}"
        c += 1

if c == 0:
    txt += "nenhum é par."

txt = txt[:txt.rfind(',')] + ' e' + txt[txt.rfind(',')+1:]

print(txt)

del txt
del c

print("\nFim! :D")
