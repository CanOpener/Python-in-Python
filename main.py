import pygame
import colours
import snake
import bodyBlock
pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pyhton in Python")


while True :

    gameDisplay.fill(colours.white)
    pygame.draw.rect(gameDisplay, colours.black, [20,20,10,10])
    pygame.display.update()

pygame.quit()
quit()
