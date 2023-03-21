# Contagem regressiva de 10 segundos para o estouro de fofos de artifício.
from time import sleep
from emoji import emojize
for c in range(10, 0, -1):
    print(f'{c}...')
    sleep(1)
print(emojize('\033[1;31m*EXPLOSÕES ÉPICAS!!!!!!!*:fireworks::fireworks::fireworks::fireworks::fireworks:\033[m'))