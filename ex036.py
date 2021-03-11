valor = float(input('Digite o valor do imovel: R$'))
salario = float(input('Digite o salario: R$'))
periodo = float(input('Quantos anos para pagar? '))

parcelas = (valor / periodo) / 12
porcentagem = (salario * 0.30)

print('Para pagar uma casa de R${:.2f} em {} anos, o valor das parcelas sera R${:.2f}.'.format(valor, periodo, parcelas))
if porcentagem >= parcelas:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')

