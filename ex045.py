from random import randint
from time import sleep

print('''Sua opçoes:
 [ 0 ] PEDRA
 [ 1 ] PAPEL 
 [ 2 ] TESOURA ''')
jogador = int(input('Qual e a sua jogada? '))

lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 11)
print('Computador jogou {}.'.format(lista[computador]))
print('Jogador jogou {}.'.format(lista[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATADO!!!')
    elif jogador == 1:
        print('Jogador ganhou!!!')
    elif jogador == 2:
        print('Computador ganhou!!!')
    else:
        print('Jogada invalida!')
elif computador == 1:
    if jogador == 0:
        print('Computador ganhou!!!')
    elif jogador == 1:
        print('EMPATADO!!!')
    elif jogador == 2:
        print('Jogador ganhou!!!')
    else:
        print('Jogada invalida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou!!!')
    elif jogador == 1:
        print('Computador ganhou!!!')
    elif jogador == 2:
        print('EMPATADO!!!')
    else:
        print('Jogada invalida!')
else:
    print('Invalido!')
