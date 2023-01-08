# Escre o primeiro e último nome de um nome inteiro.
nome = input('Digite seu nome inteiro (ou o de qualquer outra pessoa): \033[1;35m').split()
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

print(f'O primeiro nome é: \033[1;34m{nome[0]}\033[m')
print(f'O último nome é: \033[1;36m{nome[len(nome)-1]}\033[m')