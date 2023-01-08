# Um velocímetro, no qual mede a velocidade de um carro e aplica uma multa caso o
# carro esteja acima de 80Km/h, tendo que pagar R$7,00 para cada Km/h ultrapassado de 80.
carro = float(input('Digite a velocidade do carro: \033[1m'))
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.
multa = (carro - 80) * 7

if carro > 80:
    print(f'''\033[1;31mInfelizmente o carro ultrapassou a velocidade limite permitida,
    logo será multado em R$7,00 para cada quilômetro por hora acima de 80, sendo então \033[37mR${multa:.2f}\033[1;31m de multa para o motorista.\033[m''')
else: 
    print('\033[32;1mO carro está dentro da velocidade limite permitida. Sem problemas.\033[m')
