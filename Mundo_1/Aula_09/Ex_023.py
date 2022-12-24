num = int(input('Digite um número inteiro de 1 até 9999: ')) + 1000# Lê o número e adiciona 1000 nele, para que tenha as 4 casas necessárias.
strnum = str(num)# Trasforma o número em uma string para poder ser usado com os colchetes (se não me engano isso se chama idexação, ou algo assim).

print(f'Unidade: {strnum[3]}')# O número tem 4 casas por conta dos 1000 adicionados acima,
print(f'Dezena: {strnum[2]}')# então não existe problema caso o número digitado seja de menos de menos de 4 casas.
print(f'Centena: {strnum[1]}')
print(f'Milhar: {int(strnum[0]) - 1}')# trasforma a primeira casa do número em inteiro, e então subtrai 1 dele, para remover aqueles 1000 adicionados anteriormente.