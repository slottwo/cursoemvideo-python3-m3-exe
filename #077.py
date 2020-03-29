# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

# Situação: Feito!

vogais = 'aáàâã', 'eéê', 'ií', 'oóôõ', 'uú', 'y'
palavras = 'Arara', 'Leopardo', 'Panteão', 'Transformações', 'Matemática', 'Paleontologia', 'Saci', 'Capricórnio', \
           'Humano', 'Rabisco', 'Íris', 'Tiranossauro', 'Poderes', 'Mágica', 'Jargão', 'Xaxado', 'Cogumelo', \
           'Abeirou', 'Bagunceiro', 'Balões', 'Tíbia', 'Hiato'

for i in palavras:  # Escolhendo a palavra
    vog_enc = ''  # Está dentro do primeiro laço para resetar o número vogais encontradas para a próxima palavra
    print(f'A palavra {i} contém a(s) seguinte(s) vogal(is): ', end='')
    for j in i.lower():  # Pegando j como uma letra dessa palavra
        for k in vogais:  # k sendo uma string de com vogais.
            if j in k:
                if k[0] in vog_enc:  # verifica se a vogal em questão já foi encontrada antes
                    break
                else:
                    print(k[0] + ' ', end='')
                    vog_enc += k[0]
                    break
    print('')
