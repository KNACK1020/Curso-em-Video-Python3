# Nova versão do Ex064-TratandoVáriosValoresV1.0
from time import sleep

print('Digite 999 para parar o código.')

soma = contador = 0
while True:
    num = int(input(f'{contador+1}º número: '))
    if num == 999:
        break
    soma += num
    contador += 1
print('Calculando Valores...')
sleep(2)

print('Desconsiderando o \033[1;31m999\033[m:')
print(f'Foram digitados \033[1;34m{contador}\033[m números.')
print(f'A soma de todos os números digitados é igual a \033[1;35m{soma}\033[m.')

