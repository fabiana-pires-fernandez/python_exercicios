from datetime import date

atual = date.today().year
menor = 0
maior = 0

for c in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if atual - ano < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas menores de idade.'.format(menor))
print('E tambem tivemos {} pessoas maiores de idade.'.format(maior))