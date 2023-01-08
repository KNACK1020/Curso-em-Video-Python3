# Verifica se o nome de uma cidade começa com Santos.
cidade = input('Digite um nome qualquer: \033[1;32m').title().split()# Lê o nome da cidade, converte ele para title e separa por espaços.
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

print(f'O nome da cidada começa com \033[1;36mSanto\033[m?R: \033[35;1m{"Santo" in cidade[0]}\033[m')# Escreve False ou True de acordo com o teste.
