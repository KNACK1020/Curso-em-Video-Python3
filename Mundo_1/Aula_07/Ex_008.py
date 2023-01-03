# Convertendo metros para centímetros e milímetros. 
medida = float(input('Digite qualquer medida, que seja em metros: \033[32;1m'))

print(f'\033[mEssa mesma medida em centímetros fica \033[1;33m{medida * 100:.2f}\033[m.')
print(f'Já em milimetros, fica \033[1;36m{medida * 100 * 100:.2f}\033[m.')