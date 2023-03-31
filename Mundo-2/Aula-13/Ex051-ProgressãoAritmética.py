# Lê o primeiro termo de uma progressão aritmética (PA) e sua razão e,
# com isso, mostra os 10 primeiros termos dessa progressão.
primeiro = int(input('Digite o primeiro termo de uma PA (progressão artitmética): '))
razao = int(input('Agora digite a razão dessa PA: '))
contador = 0

print('-=' * 7)
for c in range(1, 11):
    print(f'{c:2}º termo: {primeiro + contador}')
    contador += razao
print('-=' * 7)