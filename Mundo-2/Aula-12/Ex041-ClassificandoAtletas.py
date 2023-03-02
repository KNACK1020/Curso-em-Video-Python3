# Lê a data de nascimento de um atleta e, de acordo o ano atual, calcula sua idade e classifica-o com base nela.
from datetime import date
nascimento = int(input('Digite a data de nascimento do(a) atleta: '))
teste = str(input('Esse(a) atleta já fez aniversário esse ano? Digite 1 para sim e 2 para não: ')).strip()
if teste == '1':
    idade = date.today().year - nascimento
elif teste == '2':
    idade = date.today().year - nascimento - 1
else:
    print('Opção inválida. Digite 1 para sim ou 2 para não.')
print(f'A idade do atleta é de {idade} anos')

if teste == '1' or teste == '2':
    if idade < 0:
        categoria_atleta = 'Não-nascido'
    elif idade <= 9:
        categoria_atleta = 'Mirim'
    elif idade <= 14:
        categoria_atleta = 'Infantil'
    elif idade <= 19:
        categoria_atleta = 'Junior'
    elif idade <= 23:
        categoria_atleta = 'Sênior'
    elif idade <= 59:
        categoria_atleta = 'Master'
    elif idade <= 120:
        categoria_atleta = 'Aposentado'
    elif idade > 120:
        categoria_atleta = 'Morto'

    print(f'Sua categoria é: {categoria_atleta}.')

