test = list()
galera = list()

test.append('Pedro')
test.append('17')

galera.append(test[:])  # Cópia de test
galera.append(test)  # "Link" de test

print(galera)

test[0] = 'Rafaela'

print(galera)

galera.remove(test)

galera.append(test[:])

test[0] = 'João'
test[1] = '16'

galera.append(test[:])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
