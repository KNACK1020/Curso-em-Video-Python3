idade = int(input('Digite a idade do atleta: '))
categoria_atleta = 0

if 0 <= idade <= 9:
    categoria_atleta = 'Mirim'
    print(categoria_atleta)
elif 9 < idade <= 14:
    categoria_atleta = 'Infantil'
    print(categoria_atleta)
elif 14 < idade <= 19:
    categoria_atleta = 'Junior'
    print(categoria_atleta)
elif 19 < idade <= 23:
    categoria_atleta = 'Sênior'
    print(categoria_atleta)
elif 23 < idade <= 59:
    categoria_atleta = 'Master'
    print(categoria_atleta)
elif 60 <= idade <= 120:
    categoria_atleta = 'Aposentado'
    print(categoria_atleta)
elif idade > 120:
    categoria_atleta = 'Morto'
    print(categoria_atleta)
elif 0 > idade:
    categoria_atleta = 'Não-nascido'
    print(categoria_atleta)

if idade.upper() in idade:
    print(idade.upper())