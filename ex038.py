num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    print('O primeiro valor e maior.')
elif num2 > num1:
    print('O segundo valor e maior.')
else:
    print('Nao existe valor maior, os dois sao iguais.')