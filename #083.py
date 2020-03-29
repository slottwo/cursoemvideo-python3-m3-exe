# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Situação: Com erros

"""
def parentese_valido(eq, i):

    for j in eq:  # Removendo espaços*
        if j.isspace():
            eq = eq.replace(j, '')

    if eq[i] == '(':
        if eq[i+1] == ')':  # Se o próximo é ')' quer dizer que temos algo como (()(a*i+3))
            print("Você digitou um/uns parentese(s) desnecessário(s).")
            return False
        elif parentese_valido(eq, i+1):
            return True
        else:
            return False
    if eq[i] == ')':  # *Por isso eu precisava remove-los, ou se não ele consideraria ...( )... correto
        if i == 0:
            return False

    else:
        return parentese_valido(eq, i + 1)
"""


# Resposta do Guanabara

def parentese_valido(ex):

    pilha: list = []

    for s in ex:
        if s == '(':
            pilha.append(s)
        elif s == ')':
            if len(pilha) > 0:
                pilha.pop()  # Se já houver um parentese aberto antes eles se cancelam.
                # E por que funciona: Se tiver um "(" e tiver outro "(" não terá problema porque esse pedaço de código
                # só é executado quando aparece ")".
            else:
                pilha.append(')')  # Se não... porra véi, já tá errado.
                break  # Paramos o laco com o len > 0 para indicar o erro.

    if len(pilha) == 0:  # Todos os parenteses se "cancelaram" hierarquicamente
        return True
    else:
        return False


# Função para testar o programa

def teste():
    while True:
        ex = input("Insira uma expressão a ser analisada: ")
        parentese_valido(ex)
        if parentese_valido(ex):
            print("A expressão é válida")
        else:
            print("A expressão não é válida")
        if input("Sair? [S/n] ") in "Ss":
            break


teste()