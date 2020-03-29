# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
# cada aluno individualmente.

alunos = list()
dados = list()

c = 1

while True:

    print("Aluno", ("0" if c < 10 else "") + str(c), 31*"=")
    c += 1

    # Nome do aluno

    nome = input("Nome: ").split()
    for i, p in enumerate(nome):
        nome[i] = p.capitalize()
    dados.append(" ".join(nome))

    # Notas

    for i in range(2):
        while True:
            try:
                nota = float(input(f"Nota {i+1}: ").replace(",", "."))
                if nota <= 10:
                    dados.append(nota)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Digite um valor de 0 a 10. Tente novamente.")

    alunos.append(dados[:])  # Copiando nome, n1, n2...
    dados.clear()  # Como estou usando append(), no final do próximo loop, teria 4 notas e não 2.

    if input("Continuar? ") in "Nn":
        break

del dados, c

# Tabela das médias

print("="*40)
print("Nº ALUNO", " "*(40-8-5-2), "MÉDIA")  # Ah véi, vai contando aí...
for n, dados in enumerate(alunos):
    indice = ("0" if n+1 < 10 else "") + str(n+1)
    print(indice, end=' ')
    print(dados[0], " "*(40 - len(dados[0]) - 1 - 3 - 5), end='')  # 1: Concatenação por vírgula -> " "; 3: Nº; 5: MÉDIA
    media = (dados[1] + dados[2]) / 2
    print(round(media, 3))
print("="*40)

# Notas individuais

while True:
    try:
        opcao = int(input(f"Digite o nº do aluno para ver sua nota individual: [Sair: >={len(alunos) + 1}] ")) - 1
        if opcao+1 > len(alunos):
            print("Obrigado por usar o sistema e até logo!")
            break
        elif opcao < 0:
            raise ValueError
        else:
            print(f"A notas de {alunos[opcao][0]} foram {alunos[opcao][1]} e {alunos[opcao][2]}.")
    except ValueError:
        print("Por favor, digite um número natural maior que 0.")
