# Lê a idade e sexo de várias pessoas até o usuário não desejar mais.
# Com base nisso, mostra as seguintes informações:
# > Número de pessoas com 18 anos de idade ou mais;
# > Números de homens;
# > Número de mulheres com menos que 20 anos de idade.
from time import sleep

pessoa = maior_18 = homens = mulheres_menor_20 = 0
while True:
    pessoa += 1
    print('='*30)
    print(f'\033[1;33m{pessoa}ª PESSOA\033[m')
    print('='*30)

    idade = int(input('Digite sua idade: '))
    sexo = 'a'
    while 'F' != sexo != 'M':
        sexo = input('Digite seu sexo (M/F): ').upper().strip()

    if idade >= 18:
        maior_18 += 1

    if sexo == 'M':
        homens += 1
    
    if idade < 20 and sexo == 'F':
        mulheres_menor_20 += 1

    continuar = 'r'
    while 'S' != continuar != 'N':
        continuar = input('Deseja continuar os cadastros? (S/N): ').upper().strip()

    if continuar == 'N':
        break

print('\033[1;32mCalculando...\033[m')
sleep(3)
print(f'Há um total de {maior_18} pessoas com mais de 18 anos.')
print(f'foram cadastrados {homens} homens.')
print(f'{mulheres_menor_20} mulheres têm menos que 20 anos.')