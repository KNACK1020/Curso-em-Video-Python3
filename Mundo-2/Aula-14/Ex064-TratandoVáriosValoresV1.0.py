# Continua lendo números até o usuário digitar 999.
n = int(input('Digite um número inteiro (999 para parar o código): '))
soma = 0
contador = 0

while n != 999:
    soma += n
    contador += 1
    n = int(input('Mais um número (999 para parar o código): '))

print(f'Foram digitados um total de \033[1;34m{contador}\033[m números, desconsiderando o 999.')
print(f'A soma de todos os números digitados (menos o 999) é igual a \033[1;35m{soma}\033[m')