# Pede para o usuário digitar 2 números e escolher o que deseja fazer com esses números:
# [1] Somá-los
# [2] Multiplicá-los
# [3] Mostrar o maior entre eles
# [4] Digitar novos valores
# [5] Sair do programa
# O programa só termina quando o usuário escolher a opção 5.
from time import sleep

opcao = 1
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while opcao != 5:
    opcao = int(input('''
O que você deseja fazer com esses números?

[1] Somar eles
[2] Multiplicar eles
[3] Mostrar o maior entre eles
[4] Digitar novos números
[5] Terminar programa

Digite o número da sua opção: '''))
    
    if num1 > num2:
        maior = num1
    elif num2 > num1:
        maior = num2
    else:
        maior = 'Ambos os números são iguais'

    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
        sleep(2)
    elif opcao == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
        sleep(2)
    elif opcao == 3:
        print(f'O maior número é: {maior}')
        sleep(2)
    elif opcao == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        sleep(2)
    elif opcao == 5:
        print('\033[1;36mFim do programa.\033[m')
    else:
        print('\033[1;31mOpção inválida. Digite 1, 2, 3, 4 ou 5 de acordo com a opção que desejada.\033[m')
        sleep(3)