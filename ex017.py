import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
nco = math.pow(co, 2)
nca = math.pow(ca, 2)
h = nco + nca
nh = math.sqrt(h)
print('O valor da hipotenusa sera {:.2f}.'.format(nh))
