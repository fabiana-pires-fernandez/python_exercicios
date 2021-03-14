from datetime import date

atual = date.today().year
ano = int(input('Ano de nascimento do atleta: '))
idade = atual - ano

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificaçao: MIRIM')
elif idade <= 14:
    print('Classificaçao: INFANTIL')
elif idade <= 19:
    print('Classificaçao: JUNIOR')
elif idade <= 25:
    print('Classificaçao: SENIOR')
else:
    print('Classificaçao: MASTER')
