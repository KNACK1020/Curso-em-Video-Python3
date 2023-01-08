# Mostra as casas de unidade, dezena, centena e milhar de um número entre 1 e 9999.
num = int(input('Digite um número inteiro de 1 até 9999: \033[1;37m'))
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

print(f'Unidade: \033[34;1m{num // 1 % 10}\033[m')
print(f'Dezena: \033[36;1m{num // 10 % 10}\033[m')
print(f'Centena: \033[1;35m{num // 100 % 10}\033[m')
print(f'Milhar: \033[1;31m{num // 1000 % 10}\033[m')