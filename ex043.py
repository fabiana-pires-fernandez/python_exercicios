peso = float(input('Digite o peso: (kg) '))
altura = float(input('Digite a altura: (m) '))

imc = peso / (altura * altura)

print('O IMC dessa pessoa e {:.1f}.'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso!')
elif 25 >= imc > 18.5:
    print('Peso ideal!')
elif 30 >= imc > 25:
    print('Sobrepeso!')
elif 40 >= imc > 30:
    print('Obesidade!')
else:
    print('Obesidade Morbida!')
