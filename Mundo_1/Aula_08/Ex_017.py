# Cálculo da hipotenusa de um triângulo retângulo.
from math import hypot


opo = float(input('Digite o cateto oposto do seu triângulo retângulo: '))
adj = float(input('E agora digite o cateto oposto: '))

print(f'A hipotenusa do triângulo retângulo em questão é {hypot(opo, adj):.2f}')

