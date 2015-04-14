import pygame
import colours
import snake
pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
snakey = snake.Snake([400, 500], 10, colours.blue, colours.black)
apple = [100, 100]
pygame.display.set_caption("Pyhton in Python")


def clear() :
    gameDisplay.fill(colours.white)

def update() :
    snakey.move(pygame, gameDisplay)
    if snakey.head == apple :
        snakey.needsGrowth = True
    else :
        pygame.draw.rect(gameDisplay, colours.red, [apple[0],apple[1],10,10])

def render() :
    pygame.display.update()

def eventHandler() :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN :
            snakey.dirChange(event, pygame)

while True :

    clear()
    eventHandler()
    update()
    render()
    clock.tick(30)

pygame.quit()
quit()
