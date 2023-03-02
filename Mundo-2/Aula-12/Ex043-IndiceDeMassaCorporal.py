# Lê a altura e o peso de uma pessoa para calcular seu IMC (índice de massa corpórea) e classificar seu status:
# abaixo de 18,5: abaixo do peso; 18,5 a 25: peso ideal; 25 a 30: sobrepeso; 30 a 40: obesidade; acima de 40: obesidade mórbida.
altura = float(input('Digite sua altura, em metros: '))
peso = float(input('Digite seu peso corporal, em quilogramas: '))
imc = peso / (altura * altura)
print(f'Com {altura:.2f}m de altura e {peso:.2f}kg de peso corporal, e seu IMC é de {str(imc).replace(".", ","):.5}kg/m².')

if imc < 18.5:
    status = 'Abaixo do peso ideal'
elif 18.5 <= imc < 25:
    status = 'Peso ideal'
elif 25 <= imc < 30:
    status = 'Sobrepeso'
elif 30 <= imc < 40:
    status = 'Obesidade'
elif imc >= 40:
    status = 'Obesidade mórbida'

print(f'O status do seu IMC é de: {status}.')