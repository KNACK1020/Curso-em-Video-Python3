nota_1 = float(input('Escreva a primeira nota do aluno: '))
if 0 > nota_1 > 10:
    print('Nota inválida. Tente novamente.')
nota_2 = float(input('Escreva a segunda nota do aluno: '))
if 0 > nota_2 > 10:
    print('Nota inválida. Tente novamente.')
media = (nota_1 + nota_2) / 2
print(f'A média do aluno é de: {media}')