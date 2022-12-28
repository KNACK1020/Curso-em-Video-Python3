# Verifica se existe a palavra Santo em um nome.
nome = input('Digite seu nome inteiro (ou o de qualquer outra pessoa): ').title().split()
# Lê o nome, converte para title e separa por espaços.

print(f'O nome digitado contém Silva nele?R: {"Silva" in nome}')
# Escreve True ou False de acordo com o nome digitado.
