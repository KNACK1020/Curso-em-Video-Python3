notas = input('Digite as duas notas do aluno (separadas por espaço): ').split()
nota1 = float(notas[0])
nota2 = float(notas[1])
media = (nota1 + nota2) / 2
if 0 > nota1 or nota1 > 10 or 0 > nota2 or nota2 > 10:
    print('Alguma das notas digitadas é inválida. Tente novamente.')
else:
    print(f'A média do aluno é de {media:.2f}.')
    if media >= 7:
        print('Aluno Aprovado!')
    elif 5 <= media < 7:
        print('Aluno em recuperação!')
    elif media < 5:
        print('Aluno reprovado!')