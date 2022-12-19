reais = float(input('Digite quantos reais você tem na sua carteira: R$'))
print(type(reais))

dolars = reais / 5.23
print(type(dolars))
print(f'convertendo seu dinheiro da carteira em dólares, fica: U${dolars:.2f} \n(considerando que atualmente um dólar vale R$5,23)')
