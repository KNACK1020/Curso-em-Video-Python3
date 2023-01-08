# Escolha aleatória de um entre quatro alunos.
from random import choice


al1 = input('Digite o nome do primeiro aluno: \033[32;1m')
al2 = input('\033[mDigite o nome do segundo aluno: \033[1;34m')
al3 = input('\033[mDigite o nome do terceiro aluno: \033[1;33m')
al4 = input('\033[mDigite o nome do quarto aluno: \033[1;35m')

print(f'\033[mO aluno \033[1;4;31m{choice([al1, al2, al3, al4])}\033[m foi escolhido para apagar o quadro')

