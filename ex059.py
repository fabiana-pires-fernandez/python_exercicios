valor = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

print('''
---- MENU ----
[ 1 ] somar
[ 2 ] multiplicar 
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do programa ''')

menu = int(input('Qual sua opcao? '))
num = 0

while menu != 5:

    if menu == 1:
        num = valor + valor2
        print('A soma do valor {} com o valor {} equivale a {}.'.format(valor, valor2, num))
        menu = int(input('Qual sua opcao? '))

    if menu == 2:
        num = valor * valor2
        print('A multiplicaçao do valor {} com o valor {} equivale a {}.'.format(valor, valor2, num))
        menu = int(input('Qual sua opcao? '))

    if menu == 3:
        if valor > valor2:
            print('O valor {} e maior que o valor {}.'.format(valor, valor2))
        if valor < valor2:
            print('O valor {} e maior que o valor {}.'.format(valor2, valor))
        else:
            print('O valor {} e igual ao valor {}.'.format(valor, valor2))
        menu = int(input('Qual sua opcao? '))

    if menu == 4:
        valor = int(input('Digite o novo primeiro valor: '))
        valor2 = int(input('Digite o novo segundo valor: '))
        menu = int(input('Qual sua opcao? '))

print('Fim!')
