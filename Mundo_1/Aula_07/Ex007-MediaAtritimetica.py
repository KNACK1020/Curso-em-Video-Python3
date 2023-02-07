# Média entre dois número dados.
nota_1 = float(input('Escreva a primeira nota do aluno: \033[1;32m'))
nota_2 = float(input('\033[mEscreva a segunda nota: \033[1;33m'))

print(f'\033[mA média do aluno foi de \033[1;35m{(nota_1 + nota_2) / 2:.1f}\033[m.')
