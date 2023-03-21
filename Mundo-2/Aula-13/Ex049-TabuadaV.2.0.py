# Como o exercício 009, mostra uma tabuada, mas dessa vez utilizando laços de repetição
# e o usuário escolhe até que número a tabuada vai.
num = int(input('Digite um número para mostrar sua tabuada: '))
tabuada = int(input('Digite até que número deseja que a tabuada vá: '))
for c in range(1, tabuada+1):
    print(f'{num} x {c} = {num*c}')