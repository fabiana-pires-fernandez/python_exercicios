from random import randint
from time import sleep

comput = randint(0, 10)
print('*' * 60)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('*' * 60)

num = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(3)

while num != comput:
    print('Errr..nao foi dessa vez, tente novamente...')
    num = int(input('Diga outro valor:  '))
    if num == comput:
        print('Parabeeenss! Acertouuu ;)')
