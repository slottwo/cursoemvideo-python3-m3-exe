# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura na tela.

# Situação: Concluído

ls_alunos = []
tmp_aluno = {"Nome": "", "Média": float(), "Situação": bool()}


def sair():
    a = input("Continuar? [Sn] ")
    if a not in "SsNn" or a == "":
        print("Resposta Inválida. Tente novamente.")
        return sair()
    elif a in "Ss":
        return False
    else:
        return True


while True:
    tmp_aluno["Nome"] = input("Nome: ").capitalize()

    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    tmp_aluno["Média"] = str((n1+n2)/2)

    tmp_aluno["Situação"] = "Aprovado" if float(tmp_aluno["Média"]) >= 7 else "Reprovado"

    ls_alunos.append(tmp_aluno.copy())

    if sair():
        break


print("-" + "="*30)
print("Nome" + " " * 5 + "|" + "Média".center(8) + "| Situação")
for aluno in ls_alunos:
    print(aluno['Nome'] + ' ' * (10 - len(aluno['Nome'])),
          aluno['Média'] + ' ' * (8 - len(aluno['Média'])),
          aluno['Situação'])
