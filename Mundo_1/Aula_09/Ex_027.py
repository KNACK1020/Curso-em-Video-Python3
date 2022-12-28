# Escre o primeiro e último nome de um nome inteiro.
nome = input('Digite seu nome inteiro (ou o de qualquer outra pessoa): ').split()


print(f'O primeiro nome é: {nome[0]}')
print(f'O último nome é: {nome[len(nome)-1]}')