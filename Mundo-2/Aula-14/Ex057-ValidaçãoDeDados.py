# Lê o sexo de uma pessoa: M para masculino, F para feminino ou NB para não-binário.
# Caso seja digitado qualquer outra opção, é pedido que o usuário digite uma opção válida até que isso aconteça.
print('Digite seu sexo: M para masculino, F para feminino ou NB para não-binário:')
sexo = input().strip()

while 'F' != sexo.upper() != 'M' and sexo.upper() != 'NB':
    sexo = input(f'"{sexo}" \033[1;31mnão é uma opção válida. Digite M, F ou NB: \033[m').strip()
print('\033[1;32mOpção válida.\033[m')
