# Fazendo o Ex060-CálculoDeFatorial, porém usando o laço de repetiçã "for" ao invés do "while" para o cálculo.
from time import sleep

num = int(input('Digite um número inteiro e maior que zero e será mostrado seu fatorial: '))
while num <= 0:
    num = int(input('Valor inválido. Digite um número inteiro e maior que zero.'))
print('Calculando...')
sleep(2)

resultado = num
print(f'{num}! = ', end='')
for c in range(0, num):
    print(f'{num}x', end='')
    num -= 1
    resultado *= num
print(f'1 = {resultado}')