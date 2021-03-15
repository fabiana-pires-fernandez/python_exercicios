lado1 = float(input('Medida primeiro lado: '))
lado2 = float(input('Medida segundo lado: '))
lado3 = float(input('Medida terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar um triangulo ', end='')
    if lado1 == lado2 == lado3:
        print('Equilatero!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isosceles!')
    else:
        print('Escaleno!')
else:
    print('Os segmentos acima nao podem formar triangulo.')
