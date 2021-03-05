a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c
print('O menor valor foi {}.'.format(menor))

if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor foi {}.'.format(maior))
