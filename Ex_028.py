# Gera um número aleatório entre 1 e 5 e pede para o usuário tentar adivinhar esse número.
from random import randint

num = randint(1, 5)# Gera um número aleatório.
num_usua = int(input('Foi gerado um número aleatório entre 1 e 5. Tente adivinhar esse número! '))
print(f'Seu chute foi de {num_usua}, enquanto o número gerado foi {num}.')
if num_usua == num:
    print('Parabéns! Você acertou o número!')
else:
    print('Infelizmente você não acertou o número. Mais sorte da próxima vez!')
