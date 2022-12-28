# Calcula o preço de um produto à vista e parcelado.
produto = float(input('Digite o preço do produto: R$'))

print(f'Com o preço de R${produto}, caso seja pago à vista, com um desconto de 15%, ficará R${produto - produto * 15 / 100:.2f}')
print(f'Já caso seja pago parcelado, com 15% de juros, ficará R$ {produto + produto * 15 / 100:.2f}')
