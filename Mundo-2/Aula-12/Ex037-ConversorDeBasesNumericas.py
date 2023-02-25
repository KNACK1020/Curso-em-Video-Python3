num_int = int(input('Digite um número inteiro: '))
escolha = input('''[1] Binário
[2] Octal
[3] Hexadecimal
Escolha para qual base deseja converter esse número: ''').strip()

if escolha == '1':
    print(f'{num_int} em binário = {bin(num_int)[2:]}')

elif escolha == '2':
    print(f'{num_int} em octal = {oct(num_int)[2:]}')

elif escolha == '3':
    print(f'{num_int} em hexadecimal = {hex(num_int)[2:]}')

else:
    print('Opção inválida. As únicas escolhas válidas são 1, 2 ou 3')