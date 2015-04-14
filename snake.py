import block

class Snake :
    head = None
    body = []
    size = 0
    bodyBlockSize = 0
    direction = 1
    headColour = None
    bodyColour = None
    needsGrowth = False
    turnedThisTurn = False
    pygame = None
    gameDisplay = None

    def __init__(self, locationList, blockSize, hc, bc, pGame, gDisplay) :
        self.headColour = hc
        self.bodyColour = bc
        self.bodyBlockSize = blockSize
        self.pygame = pGame
        self.gameDisplay = gDisplay

        self.head = block.Block(locationList, hc, pGame, gDisplay, blockSize)

    def move(self) :
        previous = self.head.getCoordinates()

        if self.direction == 1 : #up
            self.head.y -= self.bodyBlockSize
        elif self.direction == 2 : #down
            self.head.y += self.bodyBlockSize
        elif self.direction == 3 : #left
            self.head.x -= self.bodyBlockSize
        elif self.direction == 4 : #right
            self.head.x += self.bodyBlockSize

        self.head.draw()

        for bodyBlock in self.body :
            temp = bodyBlock.getCoordinates()

            bodyBlock.x = previous[0]
            bodyBlock.y = previous[1]

            previous = temp
            bodyBlock.draw()

        if self.needsGrowth :
            newBlock = block.Block(previous, self.bodyColour, self.pygame, self.gameDisplay, self.bodyBlockSize)
            self.body.append(newBlock)
            newBlock.draw()
            self.size+=1
            self.needsGrowth = False
            print(self.size)


    def dirChange(self, event) :
        if self.turnedThisTurn :
            return

        if event.key == self.pygame.K_UP :
            if self.direction != 2 :
                self.direction = 1
        elif event.key == self.pygame.K_DOWN :
            if self.direction != 1 :
                self.direction = 2
        elif event.key == self.pygame.K_LEFT :
            if self.direction != 4 :
                self.direction = 3
        elif event.key == self.pygame.K_RIGHT :
            if self.direction != 3 :
                self.direction = 4
        self.turnedThisTurn = True

    def badMove(self,boundx, boundy) :
        headCO = self.head.getCoordinates()
        if self.head.x > boundx or self.head.x < 0 :
            return False
        elif self.head.y > boundy or self.head.y <0 :
            return False
        else :
            for bodyBlock in self.body :
                if bodyBlock.getCoordinates() == headCO :
                    return False
        return True
