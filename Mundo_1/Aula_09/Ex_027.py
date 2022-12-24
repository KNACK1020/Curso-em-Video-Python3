nome = input('Digite seu nome inteiro (ou o de qualquer outra pessoa): ').split()
# Separa o nome com split para poder ler os nomes separadamente.

print(f'O primeiro nome é: {nome[0]}')# Primeiro nome.
print(f'O último nome é: {nome[len(nome)-1]}')# Último nome.