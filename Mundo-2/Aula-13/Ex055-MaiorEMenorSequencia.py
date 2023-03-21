# Lê o peso de 5 pessoas e mostra o menor e o maior peso entre os 5.
# Créditos ao Wildmarks Passos (do Youtube) que me inspirou a utilizar listas nesse código, sem a necessidade de if's.
peso = []
for c in range(1, 6):
    peso += [float(input(f'Digite o peso da {c}ª pessoa: '))]
    
print(f'Dentre os pesos citados, o maior deles é de \033[1;34m{max(peso)}kg\033[m.')
print(f'Já o menor deles é de \033[1;31m{min(peso)}kg\033[m.')
