sal = float(input('Digite o valor do salario: R$ '))

if sal >= 1250:
    nsal: float = (sal * 0.10) + sal
else:
    nsal: float = (sal * 0.15) + sal
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, nsal))