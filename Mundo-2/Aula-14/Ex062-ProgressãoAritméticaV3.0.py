# Uma versão melhorada do Ex061-ProgressãoAritmética. Ao mostrar os 10 primeiros termos,
# o programa pergunta quantos termos a mais o usuário deseja ver até o usuário digitar "0".
primeiro = int(input('Digite o primeiro termo de uma PA (progressão aritmética): '))
razao = int(input('Digite a razão dessa PA: '))

contador = 1
valor = 0
while contador <= 10:
    print(f'{contador}º termo: {primeiro + valor}')
    valor += razao
    contador += 1

num_termos = int(input('Quantos termos mais deseja ver? Digite 0 para terminar o programa: '))
while num_termos != 0:
    for c in range(num_termos):
        print(f'{contador}º termo: {primeiro + valor}')
        valor += razao
        contador += 1
    num_termos = int(input('Quantos termos mais deseja ver? Digite 0 para terminar o programa: '))

print(f'\033[1;32mPrograma terminado com êxito.\033[m Foram mostrados \033[1;34m{contador-1} termos\033[m no total.')
        