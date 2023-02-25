# Calcula o preço de um produto à vista e parcelado. Esse é um exercício extra dado na resolução do exercício 13.
produto = float(input('Digite o preço do produto: \033[1;32mR$'))

print(f'\033[mCaso seja pago à vista, com um desconto de 15%, ficará \033[1;36mR${produto - produto * 15 / 100:.2f}\033[m.')
print(f'Já caso seja pago parcelado, com 15% de juros, ficará R$ \033[1;31m{produto + produto * 15 / 100:.2f}\033[m.')
