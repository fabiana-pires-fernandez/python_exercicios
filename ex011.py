l = float(input('Digite a largura da parede:'))
c = float(input('Digite a altura da parede: '))
a = l * c
t = a / 2

print('A area da parede e: {:.2f} metros ao quadrado.'.format(a))
print('Sera necessario {:.2f} litros de tintas para pintar a parede.'.format(t))
