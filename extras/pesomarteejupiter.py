name = str(input('Digite seu nome: '))
p = float(input('Digite seu peso: '))

gt = 9.8
gm = 3.7
gj = 24.8
pm = (p / gt) * gm
pj = (p / gt) * gj

print('{}, seu peso em Marte e {:.2f}Kg, e em Jupiter e {:.2f}Kg.'.format(name, pm, pj))
