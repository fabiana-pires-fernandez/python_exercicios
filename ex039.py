from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    diferenca = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(diferenca))
    ano = atual + diferenca
    print('Seu alistamento sera em {}.'.format(ano))
else:
    diferenca = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos.'.format(diferenca))
