# Lê 6 números e faz a soma entre todos os números pares dados.
num = ''
soma = 0
contador = 0
for c in range(0, 6):
    num += input(f'Digite o {c+1}º número: ') + ' '
    if int(num.split()[c]) % 2 == 0:
        soma += int(num.split()[c])
        contador += 1
print(f'A soma dos {contador} números PARES dados é igual a {soma}.')