vel = float(input('Digite sua velocidade: '))
multa = (vel - 80) * 7

if vel > 80:
    print('MULTADO! Voce excedeu o limite permitido que e de 80Km/h!')
    print('Voce deve pagar uma multa de R${:.2f} reais!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
print('*' * 40)
print('<--- FIM! --->')
