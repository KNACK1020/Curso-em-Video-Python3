# Lê números e mostra a tabua de cada um deles, um oor um, até que o usuário digite um número negativo.
from time import sleep

contador = 0
while True:
    print('\033[1;34mDigite um número negativo para interromper a execução do código.\033[m')
    num = int(input(('Deseja ver a tabuada de qual número? ')))
    if num < 0:
        break
    print('\033[1;32mCalculando...\033[m')
    sleep(2)

    print('\033[1;33m<>\033[m'*10)
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('\033[1;33m<>\033[m'*10)
    contador += 1

print(f'\033[1;31mExecução encerrada.\033[m Foram calculadas a tabuada de \033[1;36m{contador} número(s)\033[m.')