# Arredonda um número para cima e para baixo.
import math

num = float(input('Digite um \033[33;1mnúmero com vírgula\033[m qualquer: \033[33;1m'))

print(f'\033[mArredondando esse número para \033[31;1mcima\033[m, fica \033[31;1m{math.ceil(num)}\033[m;')
print(f'Já arredondando para \033[34;1mbaixo\033[m, fica \033[34;1m{math.floor(num)}\033[m.')



