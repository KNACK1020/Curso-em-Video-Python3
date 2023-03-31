# Lê um número inteiro n qualquer e mostra os n primeiros elementos da sequência de Fibonacci.
# Os números dessa sequência seguem a seguinte regra: cada elemento da sequência é uma soma dos dois elementos anteriores.
from time import sleep

n = int(input('Digite um número inteiro maior que zero qualquer (de preferência não muito grande, você vai entender): '))
print('Calculando a Sequência de Fibonacci até o número digitado...')
sleep(3)
contador = 3

elemento1 = 0
elemento2 = 1
print('/' * 20)
print('''1º Elemento: 0
2º elemento: 1''')
while contador <= n:
    elementon = elemento1 + elemento2
    elemento1 = elemento2
    elemento2 = elementon
    print(f'{contador}º elemento: {elementon}')
    contador += 1
print('/' * 20)