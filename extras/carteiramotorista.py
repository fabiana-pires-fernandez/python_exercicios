nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
ler = str(input('Voce sabe ler e escrever? (Digite sim ou nao) ')).strip().lower()

if idade >= 18 and ler == 'sim':
    print('{} pode tirar sua habilitacao!'.format(nome))
else:
    print('Sinto muito {}, mas e necessario ser maior que 18 anos, saber ler e escrever para tirar habitacao.'.format(nome))