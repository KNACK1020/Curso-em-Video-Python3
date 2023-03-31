# Analiza e escreve vários detalhes sobre uma string.
n = (input('Digite algo: '))

print('Esse algo é um \033[31;4mnúmero?\033[m', n.isnumeric())
print('Esse algo é um \033[32;4mtexto?\033[m', n.isalpha())
print('Esse algo é um \033[33;4mtexto/número?\033[m', n.isalnum())
print('Esse algo é um \033[34;4mespaço em branco?\033[m', n.isspace())
print('Esse algo é \033[36;4mimprimível?\033[m', n.isprintable())
print('Esse algo está somente em \033[37;4mletras maiúsculas?\033[m', n.isupper())
print('Esse algo está somente em \033[31;4mletras minúsculas?\033[m', n.islower())
print('Esse algo tem apenas as \033[32;4mprimeiras letras de cada palavra maiúsculas?\033[m', n.istitle())