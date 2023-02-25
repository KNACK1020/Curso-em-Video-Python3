# Cálculo de tinta necessária para pintar uma parede.
altura = float(input('Digite a altura em metros da sua parede: \033[34;1m'))
largura = float(input('\033[mDigite a largura em metros da sua parede: \033[31;1m'))

area = altura * largura
print(f'\033[mA área de sua parede é de \033[35;1m{area:.2f}m²\033[m.')

tinta = area / 2
print(f'Para pintar essa parede será necessário 1L de tinta para cada 2m², totalizando \033[32;1m{tinta:.2f}L\033[m.')
