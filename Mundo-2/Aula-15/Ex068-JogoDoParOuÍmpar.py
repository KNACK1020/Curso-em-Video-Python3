# Jogo de par ou ímpar contra o computador. O programa só acaba quando o jogador perde, no final mostrando quantas vezes seguidas ele ganhou.
from random import randint
print('PAR OU ÌMPAR')
print('O jogo só acaba quando você perder!')

ganhos = 0
while True:
    p_ou_i = input('Escreva P (par) ou I (ímpar): ').upper().strip()
    while p_ou_i != 'P' and p_ou_i != 'I':
        p_ou_i = input('Valor inválido. Digite P para par ou I para ímpar: ')
    jogador = int(input('Digite um número de 1 a 10: '))
    computador = randint(1, 10)
    print(f'Você escolheu \033[1;34m{jogador}\033[m e o computador escolheu \033[1;33m{computador}\033[m, dando \033[1;36m{jogador+computador}\033[m.')

    print('-'*30)
    if (jogador + computador) % 2 == 0:
        if p_ou_i == 'P':
            print('\033[1;32mVocê ganhou!\033[m')
            print('-'*30)
            ganhos += 1
        elif p_ou_i == 'I':
            print('\033[1;31mVocê perdeu!\033[m')
            print('-'*30)
            break
    elif (jogador + computador) % 2 == 1:
        if p_ou_i == 'P':
            print('\033[1;31mVocê perdeu!\033[m')
            print('-'*30)
            break
        elif p_ou_i == 'I':
            print('\033[1;32mVocê ganhou!\033[m')
            print('-'*30)
            ganhos += 1
    
print(f'Você ganhou um total de \033[1;35m{ganhos}\033[m vezes seguidas.')