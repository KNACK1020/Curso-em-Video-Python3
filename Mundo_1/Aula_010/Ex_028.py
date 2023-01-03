# Gera um número aleatório entre 1 e 5 e pede para o usuário tentar adivinhar esse número.
from random import randint
from time import sleep

num = randint(1, 5)
num_usua = int(input('Foi gerado um número aleatório entre 1 e 5. Tente adivinhar esse número! \033[32;1m'))
print('\033[1;32mTestando...\033[m')

sleep(2)
print('-=-' * 23)
print(f'Seu chute foi de \033[36;1m{num_usua}\033[m, enquanto o número gerado foi \033[1;35m{num}\033[m.')
print('')

if num_usua == num:
    print('\033[1;36mParabéns! Você acertou o número!\033[m')
else:
    print('\033[1;31mInfelizmente você não acertou o número.\033[m Mais sorte da próxima vez!')
print('-=-' * 23)
