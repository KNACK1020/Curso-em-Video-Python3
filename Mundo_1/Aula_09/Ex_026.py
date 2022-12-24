frase = input('Digite uma frase qualquer: ').upper().strip()# 'Upper' para poder contar com precisão e 'strip' para não contar os espaços no começo e fim.
frase = frase.replace('Á', 'A')# Lê a frase e substitui toda letra com acento
frase = frase.replace('Ã', 'A')# para que também conte os A's acentuados.
frase = frase.replace('À', 'A')
frase = frase.replace('Â', 'A')

print(f'A letra "A" aparece {frase.count("A")} vezes nessa frase.')# Número de vezes que a letra A aparece.
print(f'A primeira vez que a letra "A" aparece na frase é na {frase.find("A") + 1}° letra')# Posição na qual o primeiro A aparece (+1 para que não conte da posição 0)
print(f'A última vez que a letra "A" aparece na frase é na {frase.rfind("A") + 1}° letra ')# Posição na qual o último A aparece.
