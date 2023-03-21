# Lê uma frase e diz se ela é um palíndromo (se ela continua igual de tráz pra frente, ignorando espaços).
# Achei muito mais simples sem usar um laço de repecição.
frase = input('Digite uma frase qualquer sem acentuação: ').replace(' ', '').upper()
nova_frase = frase[::-1]
print(f'De tráz pra frente e sem espaços, \033[1;34m{frase}\033[m fica: \033[1;36m{nova_frase}\033[m.')
if frase == nova_frase:
    print('Logo, a frase digitada \033[1;32mÉ UM POLÍNDROMO!\033[m')
else:
    print('Logo, a frase digitada \033[1;31mNÃO É UM POLÍNDROMO!\033[m')


