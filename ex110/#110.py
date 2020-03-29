# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

# Situação: Completo

from ex110.moeda import *

preço = decimal(input("Digite o preço: R$ "))
aumento = decimal(input("Insira o aumento em porcentagem: ").replace("%", ""))
desconto = decimal(input("Insira o desconto em porcentagem: ").replace("%", ""))
print()
resumo(preço, aumento, desconto)
