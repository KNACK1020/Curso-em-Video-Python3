# Analiza qual é o maior e o menor número entre 3 números dados.
num1 = float(input('Digite um número qualquer: \033[1m'))
num2 = float(input('\033[mDigite outro número: \033[1m'))
num3 = float(input('\033[mDigite mais um número: \033[1m'))
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

maior = num1
if num1 < num2 > num3:
    maior = num2
if num1 < num3 > num2:
    maior = num3

menor = num1
if num1 > num2 < num3:
    menor = num2
if num1 > num3 < num2:
    menor = num3

print(f'O \033[1;34mmaior\033[m número é \033[1;34m{maior}\033[m e o \033[1;31mmenor\033[m é \033[1;31m{menor}\033[m.')