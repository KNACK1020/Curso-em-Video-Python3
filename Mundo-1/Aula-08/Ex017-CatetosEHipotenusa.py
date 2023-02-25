# Cálculo da hipotenusa de um triângulo retângulo.
from math import hypot


opo = float(input('Digite o \033[31;1mcateto adjacente\033[m do seu triângulo retângulo: \033[31;1m'))
adj = float(input('\033[mE agora digite o \033[34;1mcateto oposto\033[m: \033[1;34m'))

print(f'\033[mA \033[35;1mhipotenusa\033[m do triângulo retângulo em questão é \033[35;1m{hypot(opo, adj):.2f}\033[m')

