# Conversão de Celcius para Fahrenheit.
c = float(input('Digite uma temperatura em Celcius: \033[31;1m'))

print(f'\033[mNa escala de Fahrenheit, \033[31;1m{c:.2f}°C\033[m fica \033[1;35m{c / 5 * 9 + 32:.2f}°F\033[m.')