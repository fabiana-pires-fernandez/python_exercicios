n = str(input('Digite seu nome: '))
p = float(input('Digite o peso: '))
a = float(input('Digite a altura: '))
ca = a * a
imc = p / ca

print('{}, seu IMC e {:.2f}.'.format(n, imc))
