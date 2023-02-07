# Lê quantos quilômetros serão rodados por um ônibus, e cobra de acordo com a distância: 
# R$0,50/km para viagens de até 200km, ou R$0,45/km para viagens acima de 200km
km = float(input('Digite quantos quilômetros serão rodados pelo ônibus: \033[1;31m'))
print('\033[m')# Para escrever uma linha em branco no terminal e para não ter que escrever isso no começo do próximo print, deixando o código mais organizado.

if km <= 200:
    print(f'O valor da viagem, sendo cobrados \033[1;34mR$0,50/km\033[m, será de \033[1;32mR${km * 0.5:.2f}\033[m.')
else:
    print(f'''O valor base da viagem é de \033[1;34mR$0,50\033[m, porém, como a viagem
tem mais de 200km, serão cobrados \033[1;36mR$0,45/km\033[m, totalizando \033[1;32mR${km * 0.45:.2f}\033[m.''')
