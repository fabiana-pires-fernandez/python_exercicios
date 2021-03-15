preco = float(input('Digite o preco normal do produto: R$ '))

dinheiro = preco - (preco * 0.10)
cartao = preco - (preco * 0.05)
cartao3 = preco + (preco * 0.20)

opcao = int(input('print('''' Escolha uma opcao de pagamento: 
    [ 1 ] Dinheiro
    [ 2 ] Cartao a vista
    [ 3 ] Cartao em ate 3x 
    [ 4 ] Cartao 3x ou mais 
    Sua escolha: '''''))

if 1 <= opcao <= 4:
    print('Sua escolha foi {}, o valor a ser pago sera: R$'.format(opcao), end=' ')
    if opcao == 1:
        print(dinheiro)
    elif opcao == 2:
        print(cartao)
    elif opcao == 3:
        print(preco)
    else:
        print(cartao3)
else:
    print('Digite uma opcao valida!')