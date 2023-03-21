# Mostra todos os números ímpares e múltiplos de três de 1 até un número dado pelo usuário.
soma = 0
quantia = 0
for c in range(3, int(input('Digite até que número deseja fazer o teste: '))+1, 6):
    soma += c
    quantia += 1
print(f'A soma de todos os \033[1;34m{quantia} números ímpares e múltiplos de 3\033[m entre 1 e 500 é igual a \033[1;34m{soma}\033[m')
