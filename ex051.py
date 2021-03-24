print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

num = int(input('Primeiro termo: '))
r = int(input('Razao: '))
d = num + (10 - 1) * r

for c in range(num, d + r, r):
    print('{} '.format(c), end='- ')
print('ACABOU')