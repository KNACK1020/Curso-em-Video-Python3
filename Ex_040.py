media = float(input('Escreva a média do aluno: '))

if 0 <= media < 5:
    print('Aluno reprovado.')
elif 5 <= media <= 6.9:
    print('Aluno terá que fazer a recuperção.')
elif 7 <= media <= 10:
    print('Aluno aprovado.')
elif media < 0 or media > 10:
    print('Nota inválida.')
