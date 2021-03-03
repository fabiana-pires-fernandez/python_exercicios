nome = str(input('Digite seu nome completo: ')).strip()
lnome = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e {}.'.format(lnome[0]))
print('Seu ultimo nome e {}.'.format(lnome[-1]))

