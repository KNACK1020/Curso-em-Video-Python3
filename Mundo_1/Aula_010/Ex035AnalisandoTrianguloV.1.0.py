# Lê 3 retas e analiza se é possível criar um triângulo com essas retas, usando o princípio matemático de que: a soma de duas retas deve ser maior que a terceira reta.
tria = input('Digite o comprimento de 3 retas (separadas por espaços): \033[1m').split()
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.
r1 = float(tria[0])
r2 = float(tria[1])
r3 = float(tria[2])

if r1 + r2 > r3  and  r1 + r3 > r2  and  r2 + r3 > r1:
    print('Com as retas dadas,\033[1;34m é possível fazer um triângulo.\033[m')
else:
    print('Com as retas dadas, \033[1;31mnão é possível fazer um triângulo.\033[m')