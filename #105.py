# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def nota(*notas, sit=False):
    """
    -> Esta função retorna dados, como situação e estatísticas, de um aluno de acordo com suas notas
    :param notas: Uma ou mais notas, tipo inteiro ou flutuante.
    :param sit: Parâmetro opcional, indica se você deseja receber a situação do aluno.
    :return: Uma série de valores em um dicionário: quantidade de notas, a maior nota, a menor, média e a situação.
    """

    notas = tuple(map(float, notas))

    d = dict()
    d['Total'] = len(notas)
    d['Maior'] = max(notas)
    d['Menor'] = min(notas)
    d['Média'] = sum(notas)/d['Total']

    if sit:
        if d['Média'] == 10:
            d['Situação'] = 'INCRÍVEL'
        elif d['Média'] > 6:
            d['Situação'] = 'BOA'
        elif d['Média'] > 4:
            d['Situação'] = 'RAZOÁVEL'
        elif d['Média'] == 0:
            d['Situação'] = 'PÉSSIMA'
        else:
            d['Situação'] = 'RUIM'
    return d


dadosDosAlunos = {
    'Pedro': nota(3.4, 9, 4, 2, sit=True),
    'Davi': nota(3.12, sit=False),
    'Nilton': nota(10, 9, 2.9, 7.1),
    'Rafaela': nota(5, 6, 7, 8, 9, 10, sit=True)}

divisoria = "=" * 82

print(divisoria)
for nome, aluno in dadosDosAlunos.items():
    print(f"Nome: {nome}", end='')
    for k, v in aluno.items():
        print(f" | {k}: {v}", end='')
    print("\n" + divisoria)


help(nota)