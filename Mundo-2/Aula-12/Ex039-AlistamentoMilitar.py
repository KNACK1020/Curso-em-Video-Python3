# Lê a idade de uma pessoa e a informa sobre o alistamento militar.
from datetime import date

nascimento = int(input('Em que ano você nasceu? '))
if int(input('Você já fez aniversário esse ano? Digite 1 para sim e 2 para não: ')) == 2:
    nascimento += 1
idade = date.today().year - nascimento
print(f'Atualmente, você tem {idade} anos de idade.')
sexo = int(input('Qual é o seu gênero? Digite 1 para homem e 2 para mulher: '))

if idade < 18 and sexo == 1:
    print(f'Você ainda não precisa se alistar para o exército, falta(m) {18 - idade} ano(s) para isso.')
    print(f'Seu alistamento deverá ocorrer no ano de {nascimento + 18}.')
elif idade > 18 and sexo == 1:
    print(f'Já passou da hora de se alistar no exército! Isso faz {idade - 18} anos!')
    print(f'O ano que seu alistamento deveria ter ocorrido no ano de {nascimento + 18}.')
elif idade == 18 and sexo == 1:
    print('Está na hora de se alistar no exército! Esse ano!')
elif sexo == 2:
    print('Como você é mulher, seu alistamento não é obrigatório. Que sorte!')