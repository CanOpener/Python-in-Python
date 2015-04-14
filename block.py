class Block :
    x = None
    y = None
    colour = None
    pygame = None
    gameDisplay = None
    size = None

    def __init__(self, cos, col, pGame, gDisplay, s) :
        self.x = cos[0]
        self.y = cos[1]
        self.colour = col
        self.pygame = pGame
        self.gameDisplay = gDisplay
        self.size = s

    def getCoordinates(self) :
        return [self.x, self.y]

    def draw(self) :
        self.pygame.draw.rect(self.gameDisplay, self.colour, [self.x,self.y, self.size ,self.size])
