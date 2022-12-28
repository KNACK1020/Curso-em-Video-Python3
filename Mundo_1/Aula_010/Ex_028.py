# Gera um número aleatório entre 1 e 5 e pede para o usuário tentar adivinhar esse número.
from random import randint
from time import sleep

num = randint(1, 5)
num_usua = int(input('Foi gerado um número aleatório entre 1 e 5. Tente adivinhar esse número! '))
print('Testando...')

sleep(2)
print('-=-' * 23)
print(f'Seu chute foi de {num_usua}, enquanto o número gerado foi {num}.')
print('')

if num_usua == num:
    print('Parabéns! Você acertou o número!')
else:
    print('Infelizmente você não acertou o número. Mais sorte da próxima vez!')
print('-=-' * 23)
