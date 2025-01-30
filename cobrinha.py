import pygame #Biblioteca de jogos
from pygame.locals import *

WINDOWS_WIDTH = 600 #Constante
WINDOWS_HEIGHT = 600 #Constante

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT)) #Variável

while True: 
    window.fill((65, 105, 225)) 

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()