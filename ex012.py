v = float(input('Digite o preço do produto: R$'))
d = v * 0.05
vn = v - d

print('O produto vale R${} reais, mas na liquidaçao o novo valor do produto R${:.2f} reais. \n Aproveite! ;)'.format(v, vn))
