# Lê um número e calcula se ele é primo ou não.
num = int(input('Digite um número inteiro qualquer: '))
contador = 0
for c in range(1, num):
    if num % c == 0:
        contador += 1

if contador == 1 or num == 1:
    print(f'O número {num} \033[1;32mÉ PRIMO!\033[m')
else:
    print(f'O número {num} \033[1;31mNÃO É PRIMO!\033[m')