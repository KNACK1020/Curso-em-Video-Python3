# Lê 3 retas e analiza se é possível criar um triângulo com essas retas, usando o princípio matemático de que: a soma de duas retas do triângulo deve ser maior que a terceira reta.
tria = input('Digite o comprimento de 3 retas: ').split()
r1 = float(tria[0])
r2 = float(tria[1])
r3 = float(tria[2])

if r1 + r2 > r3  and  r1 + r3 > r2  and  r2 + r3 > r1:
    print('Com as retas dadas,\033[1;34m é possível fazer um triângulo.\033[m')
else:
    print('Com as retas dadas, \033[1;31mnão é possível fazer um triângulo.\033[m')