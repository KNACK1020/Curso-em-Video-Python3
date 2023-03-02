# Como o ex035, lê 3 retas e calcula se é possível fazer um triângulo com elas, mas também classifica esse triângulo em:
# equilátero, com todos os lados iguais; isósceles, com dois lados iguais; ou escaleno, com todos os lados diferentes.
triangulo = input('Digite o comprimento de 3 retas, separadas por espaços: ').split()
r1 = int(triangulo[0])
r2 = int(triangulo[1])
r3 = int(triangulo[2])

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Com as retas dadas, \033[1;32mé possível fazer um triângulo\033[m.')
    tipo = '\033[1;35mescaleno\033[m'
    if r1 == r2 == r3:
        tipo = '\033[1;36mEquilátero\033[m'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        tipo = '\033[1;33misósceles\033[m'

    print(f'O tipo do triângulo criado com essas retas seria: {tipo}.')
    
else:
    print('Com as retas dadas, \033[1;31mnão é possível fazer um triângulo\033[m.')

