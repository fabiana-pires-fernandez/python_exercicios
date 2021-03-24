num = int(input('Digite um numero para ver sua tabuada: '))

print( '*' * 15)
print('Tabuada do {}:'.format(num))
for c in range(0, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print( '*' * 15)