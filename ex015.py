km = float(input('Digite a quantidade de km percorrido: '))
d = int(input('Digite a quantidade de dias alugados: '))
v = (km * 0.15) + (d * 60)

print('O valor total do aluguel do automovel fica em R${} reais.'.format(v))
