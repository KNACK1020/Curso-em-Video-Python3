# Cálculo do seno, cosseno e tangente de um ângulo.
from math import sin, cos, tan, radians

ang = int(input('Digite um ângulo qualquer: \033[31;1m'))

print(f'\033[mO \033[32;1mSeno\033[m desse ângulo é \033[32;1m{sin(radians(ang)):.2f}\033[m,')
print(f'seu \033[34;1mCosseno\033[m é \033[34;1m{cos(radians(ang)):.2f}\033[m')
print(f'e seu \033[35;1mTangente\033[m é \033[35;1m{tan(radians(ang)):.2f}\033[m.')