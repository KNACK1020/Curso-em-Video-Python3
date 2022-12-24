altura = float(input('Digite a altura em metros da sua parede: '))
largura = float(input('Digite a largura em metros da sua parede: '))

area = altura * largura

print(f'A área de sua parede é de {area:.2f}m².')

tinta = area / 2
print(f'Para pintar essa parede, serão necessários {tinta:.2f}L de tinta.')
