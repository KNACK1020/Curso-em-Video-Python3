# calcula se um ano é bissexto ou não.
from datetime import date

ano = int(input('Digite um ano qualquer para descobrir se ele é bissexto (digite 0 para analizar o ano atual): \033[1m'))
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

if ano == 0:
    ano = date.today().year# Pega o ano atual de quem estiver escrevendo no terminal.

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de \033[1m{ano}\033[1;34m é bissexto\033[m.')
else:
    print(f'O ano de \033[1m{ano}\033[1;31m não é bissexto\033[m.')
