# Simplesmente roda um arquivo de áudio com a biblioteca "pygame".
import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('Ex_021_MP3.wav')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
print('Fim')
