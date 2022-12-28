# Analiza qual é o maior e o menor número entre 2 números dados.
num1 = float(input('Digite um número qualquer: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite mais um número: '))

if num1 > num2 and num1 > num3:
    print(f'Maior número: {num1}')
if num2 > num1 and num2 > num3:
    print(f'Maior número: {num2}')
if num3 > num1 and num3 > num2:
    print(f'Maior número: {num3}')


if num1 < num2 and num1 < num3:
    print(f'Menor número: {num1}')
if num2 < num1 and num2 < num3:
    print(f'Menor número: {num2}')
if num3 < num1 and num3 < num2:
    print(f'Menor número: {num3}')
