# Lê 2 números e mostra na tela qual deles é maior ou se os dois têm o mesmo valor.
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if num1 > num2:
    print(f'O primeiro valor, {num1}, é \033[1;32mmaior\033[m que o segundo valor, {num2}.')
elif num2 > num1:
    print(f'O primeiro valor, {num1}, é \033[1;31mmenor\033[m que o segundo valor, {num2}.')
else:
    print(f'Os valores {num1} e {num2} são \033[1;33miguais\033[m.')