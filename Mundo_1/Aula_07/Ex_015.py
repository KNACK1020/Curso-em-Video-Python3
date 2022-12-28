# Calcula o valor do aluguel de um carro.
dias = int(input('Digite por quantos dias o carro foi alugado: '))
km = float(input('Digite quantos quilômetros esse carro andou: '))

print(f'O valor de aluguel do carro, considerando R$60,00 por dia e R$0,15 por km rodado, é de R${dias * 60 + km * 0.15:.2f}')
