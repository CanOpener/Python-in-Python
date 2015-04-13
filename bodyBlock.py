class bodyBlock :
    xPos = None
    yPos = None
    colour = None
    size = None

    def __init__(self, x, y, c, s) :
        self.xPos = x
        self.yPos = y
        self.colour = c
        self.size = s

    def drawSelf(self, pygame, gameDisplay) :
        pygame.draw.rect(gameDisplay, self.colour, [self.xPos,self.yPos,self.size,self.size])
