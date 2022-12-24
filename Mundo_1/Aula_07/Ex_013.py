salario = float(input('Digite o salário atual do funcionário: R$'))

salario += salario * float(input('Digite o aumento em percentagem do salário: ')) / 100
print(f'O novo salário do funcionário em questão é de R${salario:.2f}')
