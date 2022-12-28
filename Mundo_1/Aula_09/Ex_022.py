# diversas informações sobre um nome.
nome = input('Digite seu nome completo: ').strip()

print(f'Somente letras minúsculas: {nome.lower()}.')
print(f'Somente letras maiúsculas: {nome.upper()}.')
print(f'Total de letras (incluindo espaços): {len(nome)}.')
print(f'Total de letras (excluindo espaços): {len(nome) - nome.count(" ")}.')
# Outra forma de mostrar o número de letras no nome sem contar espaços: 
print(f'Total de letras (excluindo espaços): {len(nome.replace(" ", ""))}.')# Nesse caso os espaços são somente removidos (cuidado para não misturar aspas do mesmo tipo)
print(f'Seu primeiro nome, sendo {nome.split()[0]}, tem {len(nome.split()[0])} letras.')
# Outra forma de mostrar o número de letras no primeiro nome: 
print(f'Seu primeiro nome, sendo {nome.split()[0]}, tem {nome.find(" ")} letras.')# Nesse caso, encontro qual foi o primeiro índice a ser encontrado um espaço em branco, retornando exatamente o número de letras do primeiro nome (novamente cuidado com as aspas do mesmo tipo)

