# Lê quantos quilômetros serão rodados por um ônibus, e cobra de acordo com a distância: 
# R$0,50/km para viagens de até 200km, ou R$0,45/km para viagens acima de 200km
km = float(input('Digite quantos quilômetros serão rodados pelo ônibus: '))

if km <= 200:
    print(f'O valor da viagem, sendo cobrados R$0,50/km, será de R${km * 0.5:.2f}.')
else:
    print(f'''O valor base da viagem é de R$0,50, porém como a viagem 
    tem mais de 200km serão cobrados R$0,45/km, totalizando R${km * 0.45:.2f}.''')
