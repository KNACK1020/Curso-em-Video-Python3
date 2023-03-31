# Igual ao Ex051-ProgressãoAritmética, porém utilizando o laço de repetição "while" ao invés do "for".
primeiro = int(input('Digite o primeiro termo de uma PA (progressão aritmética): '))
razao = int(input('Agora digite a razão dessa PA: '))

contador = 1
valor = 0
while contador <= 10:
    print(f'{contador:2}º termo: {primeiro + valor}')
    valor += razao
    contador += 1
