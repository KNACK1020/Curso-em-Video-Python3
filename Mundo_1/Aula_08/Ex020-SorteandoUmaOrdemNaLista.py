# Aleatória a ordem de apresentação dos alunos.
from random import shuffle


al1 = input('Primeiro aluno: \033[32;1m')
al1 = f'\033[32;1m{al1}'
al2 = input('\033[mSegundo aluno: \033[35;1m')
al2 = f'\033[35;1m{al2}'
al3 = input('\033[mTerceiro aluno: \033[34;1m')
al3 = f'\033[34;1m{al3}'
al4 = input('\033[mQuarto aluno: \033[33;1m')
al4 = f'\033[33;1m{al4}'
# Cada nome já tem a própria cor, então, quando forem escritos na nova ordem,
# serão escritos com as próprias cores.

ordem = [al1, al2, al3, al4]
shuffle(ordem)

print(f'\033[mA ordem das apresentações será: {ordem[0]}\033[m, {ordem[1]}\033[m, {ordem[2]}\033[m e {ordem[3]}\033[m')
