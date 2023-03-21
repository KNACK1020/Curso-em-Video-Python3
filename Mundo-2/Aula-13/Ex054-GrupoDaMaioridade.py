# Lê a data de nascimento de várias pessoas e mostra quantas delas têm 21 anos ou mais.
from datetime import date
ano_atual = date.today().year
maior_de_idade = 0
menor_de_idade = 0
todas_idades = ''
num_pessoas = int(input('Digite de quantas pessoas você deseja digitar a data de nascimento: '))
for c in range(1, num_pessoas+1):
    idade = (ano_atual - int(input(f'Digite a data de nascimento da {c}º pessoa: ')))
    todas_idades += str(idade) + ', '
    if idade >= 21:
        maior_de_idade += 1
    else:
        menor_de_idade += 1
print(f'A idade de todas as pessoas digitadas será de, respectivamente, {todas_idades[:-2]} anos ano final desse ano.')
print(f'{maior_de_idade} pessoas têm 21 anos de idade ou mais e {menor_de_idade} pessoas têm menos de 21 anos de idade.')