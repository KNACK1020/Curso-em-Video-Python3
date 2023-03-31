# Nova versão do Ex028-JogoDaAdivinhaçãoV1.0, em que o programa só termina quando o usuário acertar o número
# e, quando ele acertar, mostra quantas tentativas o usuário teve.
from random import randint

computador = randint(1, 10)
print('Foi gerado um número aleatório entre 1 e 10. Tente adivinhá-lo!')
jogador = int(input('Seu chute: '))
tentativas = 1

while jogador != computador:
    tentativas += 1
    jogador = int(input('\033[1;31mInfelizmente você errou.\033[m Tente novamente: '))
    if jogador - 2 == computador or jogador + 2 == computador or jogador + 1 == computador or jogador - 1 == computador:
        print('\033[1;33mEstá perto...\033[m')

print('\033[1;32mPalpite correto!\033[m')
print(f'Você acertou na sua \033[1;35m{tentativas}ª\033[m tentativa.')

if tentativas <= 4:
    print('Ótimo! Acertou em poucas tentativas.')
else:
    print('Demorou um pouco, mas acertou!')