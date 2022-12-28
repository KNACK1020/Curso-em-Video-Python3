# Aumenta o salário de um funcionário:
# +15% caso o salário seja inferior a R$1250,00.
# +10% caso o salário seja igual ou superior a R$1250,00.
salário = float(input('Digite o salário do funcionário que deseja aumentar: R$'))

if salário < 1250:
    print(f'Com um aumento de 15%, o novo salário será de R${salário + salário * 15 / 100:.2f}')
else:
    print(f'Com um aumento de 10%, o novo salário será de R${salário + salário * 10 / 100:.2f}')
