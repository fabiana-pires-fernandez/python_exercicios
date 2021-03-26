num = int(input('Digite um numero: '))
div = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        div += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vez(es).'.format(num, div))

if div > 2:
    print('Esse numero nao e primo!'.format(num))
else:
    print('Esse numero e primo!'.format(num))
