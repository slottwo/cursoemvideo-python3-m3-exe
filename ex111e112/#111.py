# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# Situação: COMPLETOOOOOOO!

from ex111e112.utilidades.dados import leia_dinheiro
from ex111e112.utilidades.moeda import resumo, decimal

preço = leia_dinheiro("Digite o preço: R$ ")
aumento = decimal(input("Insira o aumento em porcentagem: ").replace("%", ""))
desconto = decimal(input("Insira o desconto em porcentagem: ").replace("%", ""))
print()
resumo(preço, aumento, desconto)
