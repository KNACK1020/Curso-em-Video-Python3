# Simplesmente roda um arquivo de áudio com a biblioteca "playsound".
# Essa biblioteca é muito mais simples que a "pygame", proposta na resolução da aula,
# porém não faz mais nada além de reproduzir um áudio.
from playsound import playsound
from time import sleep

print('\033[1;31mPATOMOSTIO INTENSIFIES\033[m')
sleep(0.5)
playsound('C:\workspace\Curso-em-Video-Python\Mundo_1\Aula_08\Ex_021_audio.WAV')
# É necessário apenas colocar o local do áudio como argumento na única função da biblioteca, também chamda "Playsound".