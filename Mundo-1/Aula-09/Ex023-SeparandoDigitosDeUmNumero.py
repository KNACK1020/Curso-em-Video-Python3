# Solução proposta por @VashBSJ, do Youtube.
# Mostra as casas de unidade, dezena, centena e milhar de um número entre 1 e 9999.
num = int(input('Digite um número inteiro de 0 até 9999: \033[1;37m')) + 10000# Assim o número terá 4 dígitos de qualquer forma.
num = str(num)# Pare que possa ser usado o sistema de pegar caractéres de uma string.
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

print(f'Unidade: \033[34;1m{num[4]}\033[m')
print(f'Dezena: \033[36;1m{num[3]}\033[m')
print(f'Centena: \033[1;35m{num[2]}\033[m')
print(f'Milhar: \033[1;31m{num[1]}\033[m')