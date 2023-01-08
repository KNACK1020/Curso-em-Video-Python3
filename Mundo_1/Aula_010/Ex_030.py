# Verificando se um número é par ou ímpar.
num = int(input('Digite um número inteiro qualquer: \033[1;31m'))
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

print(f'O número \033[1;36m{num}\033[m é \033[1;34mpar\033[m!' if num % 2 == 0 else f'O número \033[1;36m{num}\033[m é \033[1;32mímpar\033[m!')
