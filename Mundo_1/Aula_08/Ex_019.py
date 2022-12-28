# Escolha aleatória de um entre quatro alunos.
from random import choice


al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

print(f'O aluno {choice([al1, al2, al3, al4])} foi escolhido para apagar o quadro')

