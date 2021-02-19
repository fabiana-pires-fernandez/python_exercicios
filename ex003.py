n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
sub = n2 - n1
m = n1 * n2
d = n2 / n1

print('A soma entre {} e {} = {}.'.format(n1, n2, s))
print('A subtracao entre {} e {} = {}.'.format(n2, n1, sub))
print('A multiplicacao entre {} e {} = {}.'.format(n1, n2, m))
print('A divisao entre {} e {} = {}.'.format(n2, n1, d))

print(type(s))
print(type(sub))
print(type(m))
print(type(d))
