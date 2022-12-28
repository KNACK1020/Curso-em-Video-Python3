# Aleatória a ordem de apresentação dos alunos.
from random import shuffle


al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')

ordem = [al1, al2, al3, al4]
shuffle(ordem)
nal1 = ordem[0]
nal2 = ordem[1]
nal3 = ordem[2]
nal4 = ordem[3]

print(f'A ordem das apresentações será: {nal1}, {nal2}, {nal3} e {nal4}')
