# calcula se um ano é bissexto ou não.
from datetime import date

ano = int(input('Digite um ano qualquer para descobrir se ele é bissexto (digite 0 para analizar o ano atual): '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')
