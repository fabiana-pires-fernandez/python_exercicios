d = float(input('Digite a distancia da viagem(em Km): '))
p1 = d * 0.50
p2 = d * 0.45

print('Voce esta prestes a começar uma viagem de {}Km.'.format(d))
if d <= 200:
    print('E o preço da sua passagem sera de R${:.2f}.'.format(p1))
else:
    print('E o preço da sua passagem sera de R${:.2f}.'.format(p2))
