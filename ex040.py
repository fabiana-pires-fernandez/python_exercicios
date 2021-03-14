nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print('A media do alunx foi {:.1f}.'.format(media))

if media >= 7:
    print('APROVADO!!!')
elif 5 <= media <= 6.9:
    print('RECUPERACAO!!!')
else:
    print('REPROVADO!!!')
