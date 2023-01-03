# Calcula um preço com desconto.
preco = float(input('Digite o preço de um produto: \033[32;1mR$'))
desconto = float(input('\033[mDigite o desconto desse protudo em porcentagem: \033[36;1m'))

print(f'\033[1;32mR${preco:.2f}\033[m com \033[1;36m{desconto}%\033[m de desconto fica \033[1;35mR${preco - (preco * desconto / 100)}\033[m.')
