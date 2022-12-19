preco = float(input('Digite um preço de um produto: R$'))
desconto = float(input('Digite o desconto desse protudo em porcentagem: '))

print(f'{preco:.2f}R$ com 5% de desconto fica R${preco - preco * desconto / 100}')
