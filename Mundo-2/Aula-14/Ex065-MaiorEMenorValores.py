# Lê vários valores até o usuário querer parar. Em seguida mostra as seguintes informações:
# Quantos valores foram digitados
# A média de todos os valores digitados
# O menor e o maior número entre todos.
soma = 0
validacao = 'S'
quantia_num = 0

while validacao == 'S':
    num = int(input('Digite um número qualquer: '))
    soma += num
    validacao = input('Deseja continuar? S para sim e N para não: ').upper().strip()
    quantia_num += 1

    if soma == num:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'A média de todos os {quantia_num} valores digitados é igual a {soma / quantia_num}')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}.')