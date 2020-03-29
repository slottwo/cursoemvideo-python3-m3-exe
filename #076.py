# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
# sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Situação: Completo, eu acho...

print()  # Lista de produtos abaixo....

# Potion 300
# Super Potion 700
# Hyper Potion 1200
# Max Potion 2500
# Full Restore 3000
# Repel 350
# Super Repel 500
# Max Repel 700
# Soda POP 300
# Poke Doll 1000
# Magikarp 500
# Revival Herb
# Revive 1500
# Antidote 100
# Awakening 250
# Burn Heal 250
# Ice Heal 250
# Paralyz Heal 200
# Full Heal 600
# Bike 1000000
# Escape Rope 550
# Fire  Stone 2100
# Thunder Stone 2100
# Water Stone 2100
# Pokeball 200
# Great Ball 600
# Ultra Ball 1200

# Variáveis

t = 'Potion$300',\
	'Super Potion$700',\
	'Hyper Potion$1200',\
	'Max Potion$2500',\
	'Full Restore$3000',\
	'Repel$350',\
	'Super Repel$500',\
	'Max Repel$700',\
	'Soda POP$300',\
	'Poke Doll$1000',\
	'Magikarp$500',\
	'Revive$1500',\
	'Antidote$100',\
	'Awakening$250',\
	'Burn Heal$250',\
	'Ice Heal$250',\
	'Paralyz Heal$200',\
	'Full Heal$600',\
	'Bike$1000000',\
	'Escape Rope$550',\
	'Fire  Stone$2100',\
	'Thunder Stone$2100',\
	'Water Stone$2100',\
	'Pokeball$200',\
	'Great Ball$600',\
	'Ultra Ball$1200'

# GUI

print('='*40)
print('='+'PokeCenter Online'.center(38, ' ')+'=')
print('='*40)

print("Produto " + '.'*(38 - (13 - 1)) + ' ' + "Preço")
for i in t:
	print(i.replace('$', ' ' + '.'*(38 - (len(i) - 1)) + ' '))  # Tocando $ por " ...(...).. " O número de pontos é:
# 40 - 2(espaços) - o tamanho da string sem o $

print('='*40)
