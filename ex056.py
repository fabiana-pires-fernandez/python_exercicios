somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
sf = 0

for c in range(1, 5):
    print('---- {} PESSOA ----'.format(c))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    somaidade += idade

    if c == 1 and sexo == 'M':
        maioridadeh = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        sf += 1

    mediaidade = somaidade / 4

print('A media de idade do grupo e de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadeh, nomevelho))
print('Ao todo ha {} mulher(es) com menos de 20 anos..'.format(sf))
