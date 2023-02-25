# Verifica informações sobre a letra A em uma frase.
frase = input('Digite uma frase qualquer: \033[1;30m').upper().strip()# 'Upper' para poder contar com precisão e 'strip' para não contar os espaços no começo e fim da string.
frase = frase.replace('Á', 'A')# Lê a frase e substitui toda letra com acento
frase = frase.replace('Ã', 'A')# para que também conte os A's acentuados.
frase = frase.replace('À', 'A')
frase = frase.replace('Â', 'A')
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

print(f'A letra "A" aparece \033[1;34m{frase.count("A")}\033[m vezes nessa frase.')# Número de vezes que a letra A aparece.
print(f'A primeira vez que a letra "A" aparece na frase é na \033[1;32m{frase.find("A") + 1}°\033[m letra')# Posição na qual o primeiro A aparece (+1 para que não conte da posição 0)
print(f'A última vez que a letra "A" aparece na frase é na \033[1;31m{frase.rfind("A") + 1}°\033[m letra ')# Posição na qual o último A aparece.
