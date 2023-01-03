# Calcula o aumento em porcentagem do salário de um funcionário.
salario = float(input('Digite o salário atual do funcionário: \033[1;32mR$'))

salario += salario * float(input('\033[mDigite o aumento em percentagem do salário: \033[33;1m')) / 100
print(f'\033[mO novo salário do funcionário em questão é de \033[36;1mR${salario:.2f}\033[m.')
