# Calcula o fatorial de um número dado.
from time import sleep

num = int(input('Digite um número inteiro maior que zero e será mostrado seu fatorial: '))
while num <= 0:
    num = int(input('Valor inválido. Digite um número inteiro e maior que zero: '))
print('Calculando...')
sleep(2)

resultado = num
print(f'{num}! = ', end='')
while num > 1:
    print(f'{num}x', end='')
    num -= 1
    resultado *= num
print(f'1 = {resultado}')
