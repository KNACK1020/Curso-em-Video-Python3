import math
test = 2

num = float(input('Digite um número com vírgula qualquer: '))
num = str(f'{num:.9f}')
print(f' 0: {num[0]}, 1: {num[1]}, 2: {num[2]}, 3: {num[3]},  4: {num[4]},  5: {num[5]},  6: {num[6]},  {num[7]},  {num[8]}')
print(float(num[test]))

if float(num[test]) == 5:
    test += 1
print(float(num[test]))

if float(num[2]) == 5 and float(num[3]) == 0 or float(num[any(range(10))]) < 5:
    print(f'A versão arredondada desse número é {int(math.floor(float(num)))}')

else:
    print(f'A versão arredondada desse número é {int(math.ceil(float(num)))}')


