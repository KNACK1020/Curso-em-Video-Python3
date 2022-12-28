# Mostra as casas de unidade, dezena, centena e milhar de um número entre 1 e 9999.
num = int(input('Digite um número inteiro de 1 até 9999: '))

print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')