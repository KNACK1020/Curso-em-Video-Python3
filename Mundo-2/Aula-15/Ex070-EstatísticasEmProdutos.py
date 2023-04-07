# Lê o nome e preço de vários produtos até o usuário não desejar mais.
# Serão retiradas e mostradas as seguintes informações:
# > O total de dinheiro gasto na compra;
# > A quantia de produtos com preço maior que R$1000,00.
# > O nome do produto mais barato entre todos.
from time import sleep

c = preco_total = produto_mais_1000 = 0
while True:
    c += 1
    print('=-='*20)
    print(F'{c}º PRODUTO')
    print('=-='*20)
    produto = input(f'Nome do produto: ')
    preco = float(input(f'Preço em reais do produto: R$'))

    preco_total += preco
    if preco > 1000:
        produto_mais_1000 += 1
    if c == 1 or preco < menor:
        produto_mais_barato = produto
        menor = preco

    continuar = ' '
    while 'N' != continuar != 'S':
        continuar = input('Deseja continuar? (S/N): ').upper().strip()
    if continuar == 'N':
        break
print('Calculando...')
sleep(2)

print(f'O total da compra é de R${preco_total:.2f}')
print(f'Há um total de {produto_mais_1000} produtos que custam mais que R$1000.00')
print(f'O produto mais barato, custando R${menor:.2f}, foi identificado pelo nome de "{produto_mais_barato}".')