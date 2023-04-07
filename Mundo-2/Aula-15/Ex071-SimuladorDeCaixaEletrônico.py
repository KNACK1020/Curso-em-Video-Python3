# Um simulador de caixa eletrônico, em que o usuário digita quantos reais deseja sacar e o programa
# calcula quantas e quais notas serão sacadas. As notas disponíveis são de: 50, 20, 10 e 1 reais.
from time import sleep

saque = int(input('Quantos reais deseja sacar? R$'))
cedula = 50
total_cedulas = 0

print('\033[1;32mCalculando as notas necessárias...\033[m')
sleep(2)
print('='*55)
while True:
    if saque >= cedula:
        saque -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Notas de R${cedula:.2f} retiradas: \033[1;31m{total_cedulas}\033[m totalizando R${cedula * total_cedulas:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        total_cedulas = 0

        if saque == 0:
            break
print('='*55)
print('Saque realizado com sucesso! Agradecemos a preferência!')