# Tabuada de um número.
cores = {'limpa':'\033[m',
'verde':'\033[1;32m',
'vermelho':'\033[1;31m'}
# Dicionário de cores

num = float(input('Digite um número, e será mostrada sua taboada: \033[1;32m'))

print('\033[m', '-'*13)
print('{}{}{} x  1 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num, cores['limpa']))
print('{}{}{} x  2 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*2, cores['limpa']))
print('{}{}{} x  3 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*3, cores['limpa']))
print('{}{}{} x  4 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*4, cores['limpa']))
print('{}{}{} x  5 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*5, cores['limpa']))
print('{}{}{} x  6 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*6, cores['limpa']))
print('{}{}{} x  7 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*7, cores['limpa']))
print('{}{}{} x  8 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*8, cores['limpa']))
print('{}{}{} x  9 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*9, cores['limpa']))
print('{}{}{} x 10 = {}{}{}'.format(cores['verde'], num, cores['limpa'], cores['vermelho'], num*10, cores['limpa']))
print('\033[m', '-'*13)
