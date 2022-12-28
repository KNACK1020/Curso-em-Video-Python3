# Um velocímetro, no qual mede a velocidade de um carro e aplica uma multa caso o
# carro esteja acima de 80Km/h, tendo que pagar R$7,00 para cada Km/h ultrapassado de 80.
carro = float(input('Digite a velocidade do carro: '))
multa = (carro - 80) * 7

if carro > 80:
    print(f'''Infelizmente o carro ultrapassou a velocidade limite permitida,
    logo será multado em R$7,00 para cada quilômetro por hora acima de 80, sendo então R${multa:.2f} de multa para o motorista.''')
else: 
    print('O carro está dentro da velocidade limite permitida. Sem problemas.')
