import pygame
import random
import colours
import snake
import block
pygame.init()

FRAMEX = 500
FRAMEY = 500
BOUNDSX = 500
BOUNDSY = 500
FPS = 20
pastSize = 0

gameDisplay = pygame.display.set_mode((FRAMEX, FRAMEY))
clock = pygame.time.Clock()
snakey = snake.Snake([250, 450], 10, colours.blue, colours.black, pygame, gameDisplay)
apple = block.Block([BOUNDSX/2, BOUNDSY/2], colours.red, pygame, gameDisplay, 10)


def clear() :
    gameDisplay.fill(colours.white)

def update() :
    global FPS
    global pastSize
    snakey.move()

    if snakey.head.getCoordinates() == apple.getCoordinates() :
        snakey.needsGrowth = True
        newX = random.randint(0, (FRAMEX-10)/10) * 10
        newY = random.randint(0, (FRAMEY-10)/10) * 10
        apple.x = newX
        apple.y = newY
    else :
        if not snakey.badMove(BOUNDSX, BOUNDSY) :
            pygame.quit()
            quit()

    apple.draw()
    snakey.turnedThisTurn = False
    if (snakey.size != pastSize) :
        pastSize = snakey.size
        if (snakey.size%10 == 0) and (snakey.size != 0) :
            FPS += 1
    pygame.display.set_caption("Pyhton in Python - " + str(snakey.size))

def render() :
    pygame.display.update()

def eventHandler() :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN :
            snakey.dirChange(event)

while True :

    clear()
    eventHandler()
    update()
    render()
    clock.tick(FPS)

pygame.quit()
quit()
