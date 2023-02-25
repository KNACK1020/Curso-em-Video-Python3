# Verifica se existe a palavra Santo em um nome.
nome = input('Digite seu nome inteiro (ou o de qualquer outra pessoa): \033[1;32m').title().split()
# Lê o nome, converte para title e separa por espaços.
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

print(f'O nome digitado contém \033[31;1mSilva\033[m nele?R: \033[1;36m{"Silva" in nome}\033[m.')
# Escreve True ou False de acordo com o nome digitado.
