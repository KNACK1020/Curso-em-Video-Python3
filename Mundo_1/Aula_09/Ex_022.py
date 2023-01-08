# diversas informações sobre um nome.
nome = input('Digite seu nome completo: \0331;30').strip()
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

print(f'Somente letras minúsculas: \033[1;33m{nome.lower()}\033[m.')
print(f'Somente letras maiúsculas: \033[1;31m{nome.upper()}\033[m.')
print(f'Total de letras (incluindo espaços): \033[1;34m{len(nome)}\033[m.')
print(f'Total de letras (excluindo espaços): \033[1;35m{len(nome) - nome.count(" ")}\033[m.')

# Outra forma de mostrar o número de letras no nome sem contar espaços: 
alt_sem_esp = f'Total de letras (excluindo espaços): \033[1;35m{len(nome.replace(" ", ""))}.'
# Nesse caso os espaços são somente removidos da string (cuidado para não misturar aspas do mesmo tipo).

print(f'Seu primeiro nome, sendo \033[1;32m{nome.split()[0]}\033[m, tem \033[1;36m{len(nome.split()[0])}\033[m letras.')

# Outra forma de mostrar o número de letras no primeiro nome: 
alt_pri_letra = f'Seu primeiro nome, sendo \033[1;32m{nome.split()[0]}\033[m, tem \033[36;1m{nome.find(" ")}\033[m letras.'
# Nesse caso, encontro qual foi o primeiro índice a ser encontrado um espaço em branco, retornando exatamente o número de letras do primeiro nome (novamente cuidado com as aspas do mesmo tipo).
