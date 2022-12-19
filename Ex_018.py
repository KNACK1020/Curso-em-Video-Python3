from math import sin, cos, tan, radians

ang = int(input('Digite um ângulo qualquer: '))

print(f'O Seno desse ângulo é {sin(radians(ang)):.2f},')
print(f'seu Cosseno é {cos(radians(ang)):.2f}')
print(f'e seu Tangente é {tan(radians(ang)):.2f}')