# Jokempô contra o computador.
from random import randint
from time import sleep
escolhas = ['Pedra', 'Papel', 'Tesoura']
escolha_jog = int(input('''\033[1;33mEscolha entre:
[1] Pedra
[2] Papel
[3] Tesoura\033[m
Digite o número da alternativa: ''')) - 1
print('\033[1;37mVerificando...\033[m')
sleep(2)
print('')
escolha_comp = randint(1, 3) - 1

print(f'Enquanto você escolheu \033[1;35m{escolhas[escolha_jog]}\033[m, o computador escolheu \033[1;34m{escolhas[escolha_comp]}\033[m.')
if escolhas[escolha_jog] == escolhas[escolha_comp - 1]:
    print('\033[1;31mO Computador te derrotou!\033[m Mais sorte na próxima.')

if escolhas[escolha_comp] == escolhas[escolha_jog - 1]:
    print(f'\033[1;32mParabéns!\033[m Você conseguiu ganhar!')

if escolhas[escolha_jog] == escolhas[escolha_comp]:
    print(f'\033[1;36mEmpate!\033[m Ambos tiveram a mesma escolha.')
