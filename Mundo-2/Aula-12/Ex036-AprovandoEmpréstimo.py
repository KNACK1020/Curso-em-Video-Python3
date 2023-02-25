# Um empréstimo de banco para a compra de uma casa, porém o valor mensal da compra não poderá exceder 30% do salário do comprador.
valor_casa = float(input('Digite o valor da casa que deseja comprar: R$'))
salario = float(input('Digite seu salário mensal: R$'))
print(f'Para pagar a casa, o valor mensal não pode ultrapassar 30% de seu salário, ou seja, R${salario*30/100:.2f}')
mensalidade = float(input('Digite em quantos anos deseja pagar essa casa: ')) * 12

if mensalidade <= salario * 30 / 100:
    print(f'Empréstimo aprovado! O valor a ser pago mensalmente pela casa será de R${valor_casa/mensalidade:.2f}.')
else:
    print(f'''Infelizmente a mensalidade da compra supera 30% do seu salário mensal,
logo o empréstimo não poderá ser realizado.''')
