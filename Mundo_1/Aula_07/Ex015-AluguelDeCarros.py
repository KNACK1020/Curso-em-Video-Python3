# Calcula o valor do aluguel de um carro.
dias = int(input('Digite por quantos dias o carro foi alugado: \033[33;1m'))
km = float(input('\033[mDigite quantos quilômetros esse carro andou: \033[31;1m'))

print(f'\033[mO valor de aluguel do carro, considerando \033[34;1mR$60,00\033[m por dia e \033[34;1mR$0,15\033[m por km rodado, é de \033[32;1mR${dias * 60 + km * 0.15:.2f}\033[m.')
