from random import randint
from time import sleep

comp = randint(0, 5)
print('*' * 60)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('*' * 60)

num = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if comp == num:
    print('PARABEEENS! Voce conseguiu me vencer!')
else:
    print('GANHEEEI! Eu pensei no numero {} e nao no {}!'.format(comp, num))
print('FIM!')