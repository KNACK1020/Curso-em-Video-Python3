# Analiza e escreve vários detalhes sobre um número.
n = (input('Digite algo: '))

print('Esse algo é um número?', n.isnumeric())
print('Esse algo é um texto?', n.isalpha())
print('Esse algo é um texto/número?', n.isalnum())
print('Esse algo é um espaço em branco?', n.isspace())
print('Esse algo é imprimível?', n.isprintable())
print('Esse algo está somente em letras maiúsculas?', n.isupper())
print('Esse algo está somente em letras minúsculas?', n.islower())
print('Esse algo tem apenas as primeiras letras de cada palavra maiúsculas?', n.istitle())