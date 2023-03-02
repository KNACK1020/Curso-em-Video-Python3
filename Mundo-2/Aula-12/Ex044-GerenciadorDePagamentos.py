# Lê o preço de uma compra e o muda de acordo com sua condição:
# À vista em dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Até 2x no cartão: preço base; 
# 3x ou mais no cartão: 20% de juros.
preço = float(input('Digite o preço total da compra: '))
condiçao = int(input('''Como você deseja pagar o produto?
[1] À vista em dinheiro/cheque: ganha 10% de desconto.
[2] À vista no cartão: ganha 5% de desconto.
[3] Em até 2x no cartão: preço base.
[4] Em 3x ou mais no cartão: com 20% de juros.
Digite o número da alternativa escolhida: '''))

if condiçao == 1:
    print(f'Com 10% de desconto, o preço diminui para R${preço-preço*10/100:.2f}.')
elif condiçao == 2:
    print(f'Com 5% de desconto, o preço diminui para R${preço-preço*5/100:.2f}.')
elif condiçao == 3:
    print(f'Parcelado em 2x no cartão, o preço continua o mesmo, sendo R${preço/2:.2f} por mês.')
elif condiçao == 4:
    parcela = int(input('Deseja parcelar em quantas vezes? '))
    print(f'Parcelado em {parcela}x no cartão o preço aumenta em 20%, ficando R${preço+preço*20/100:.2f}, ou seja, R${(preço+preço*20/100)/parcela:.2f} por mês.')
else:
    print('\033[1;31mOpção inválida. Só existem 4 formas de pagamento. Digite o número da alternativa que deseja.\033[m')