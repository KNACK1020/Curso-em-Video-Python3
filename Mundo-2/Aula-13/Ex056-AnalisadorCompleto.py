# Lê o nome, idade e sexo de 4 pessoas, e então mostra as seguintes informações:
# > A média de idade das pessoas.
# > Quem é o homem mais velho entre eles.
# > Quantas mulheres têm menos de 20 anos.
todas_idades = 0
idade_homem_mais_velho = 0
mulheres_menos_20_anos = 0
for pessoa in range(1,5):
    print('-'*7, f'{pessoa}ª PESSOA', '-'*7)
    nome = input('Nome: ').strip()
    genero = input('Gênero (M ou F, qualquer outra coisa para não-binário): ').upper().strip()
    idade = int(input('Digite a idade: '))


    todas_idades += idade

    if genero == 'M' and pessoa == 1:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    elif genero == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    
    if genero == 'F' and idade < 20:
        mulheres_menos_20_anos += 1


print(f'A média de idade entre as 4 pessoas citadas é de aproximadamente {todas_idades / 4:.2f} anos.')
if idade_homem_mais_velho == 0:
    print('Não houve nenhum homem citado, logo não há homem mais velho.')
else:
    print(f'O homem mais velho citado, com {idade_homem_mais_velho} anos de idade, se chama {nome_homem_mais_velho}.')
print(f'Há um total de {mulheres_menos_20_anos} mulhere(s) com menos de 20 anos.')