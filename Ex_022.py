nome = input('Digite seu nome completo: ').strip()

print(f'Somente letras minúsculas: {nome.lower()}.')# Mostra o nome digitado, mas somente com letras minúsculas
print(f'Somente letras maiúsculas: {nome.upper()}.')# Mostra o nome digitado, mas somente com letras maiúsculas
print(f'Total de letras (incluindo espaços): {len(nome)}.')# Mostra o número de letras contidas no nome
print(f'Total de letras (excluindo espaços): {len(nome) - nome.count(" ")}.')# Mostra o número de letras contidas no nome, mas não contando espaços (cuidado para não misturar várias aspas do mesmo tipo)
# No caso acima, o número de letras no nome é contado, junto com os espaços, e então é subtraído do número de espaços contidos no nome
# Outra forma de mostrar o número de letras no nome sem contar espaços: 
print(f'Total de letras (excluindo espaços): {len(nome.replace(" ", ""))}.')# Nesse caso os espaços são somente removidos (novamente cuidado para não misturar aspas do mesmo tipo)
print(f'Seu primeiro nome, sendo {nome.split()[0]}, tem {len(nome.split()[0])} letras.')# Mostra o número de letras contidas somente no primeiro nome
# Outra forma de mostrar o número de letras no primeiro nome: 
print(f'Seu primeiro nome, sendo {nome.split()[0]}, tem {nome.find(" ")} letras.')# Nesse caso, encontro qual foi o primeiro índice a ser encontrado um espaço em branco, retornando exatamente o número de letras do primeiro nome (novamente cuidado com as aspas do mesmo tipo)

