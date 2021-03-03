nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())
print('Seu nome tem ao todos {} letras.'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
lnome = nome.split()
print('Seu primeiro nome e {} e ele tem {} letras.'.format(lnome[0], len(lnome[0])))
