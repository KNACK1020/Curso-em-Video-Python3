# Calcula um preço com desconto.
preco = float(input('Digite um preço de um produto: R$'))
desconto = float(input('Digite o desconto desse protudo em porcentagem: '))

print(f'{preco:.2f}R$ com {desconto}% de desconto fica R${preco - (preco * desconto / 100)}')
