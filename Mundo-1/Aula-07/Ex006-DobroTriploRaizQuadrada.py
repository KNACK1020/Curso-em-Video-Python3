# Contas matemáticas com um número dado.
num = int(input('Escreva um número qualquer: \033[32;1m'))


print(f'\033[mO dobro desse número é \033[33;4;1m{num * 2}\033[m e seu triplo é \033[34;4;1m{num * 3}\033[m.')
print(f'Sua potência elevada a 2 é \033[35;1;4m{num ** 2}\033[m e sua raiz quadrada é \033[36;1;4m{num ** (1/2)}\033[m.')
print(f'Sua potência elevada a 3 é \033[31;1;4m{num ** 3}\033[m e sua raiz cúbica é \033[1;4;34m{num ** (1/3)}\033[m.')
print(f'A versão simplificada de sua raiz quadrada é \033[33;1;4m{num ** (1/2):.3f}\033[m \ne de sua raiz cúbica é \033[34;1;4m{num ** (1/3):.3f}\033[m.')