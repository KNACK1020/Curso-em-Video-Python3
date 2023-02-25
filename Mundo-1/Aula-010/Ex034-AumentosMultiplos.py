# Aumenta o salário de um funcionário:
# +15% caso o salário seja inferior a R$1250,00.
# +10% caso o salário seja igual ou superior a R$1250,00.
salário = float(input('Digite o salário do funcionário que deseja aumentar: \033[1;32mR$'))
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

if salário < 1250:
    print(f'Com um aumento de \033[31;1m15%\033[m, o novo salário será de \033[1;34mR${salário + salário * 15 / 100:.2f}\033[m')
else:
    print(f'Com um aumento de \033[31;1m10%\033[m, o novo salário será de \033[1;34mR${salário + salário * 10 / 100:.2f}\033[m')
