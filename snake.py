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

    def __init__(self, locationList, blockSize, hc, bc) :
        self.headColour = hc
        self.bodyColour = bc
        self.bodyBlockSize = blockSize

        self.head = locationList

    def move(self, pygame, gameDisplay) :
        previous = [self.head[0], self.head[1]] #force pass by value

        if self.direction == 1 : #up
            self.head[1] -= self.bodyBlockSize
        elif self.direction == 2 : #down
            self.head[1] += self.bodyBlockSize
        elif self.direction == 3 : #left
            self.head[0] -= self.bodyBlockSize
        elif self.direction == 4 : #right
            self.head[0] += self.bodyBlockSize

        pygame.draw.rect(gameDisplay, self.headColour, [self.head[0],self.head[1],self.bodyBlockSize,self.bodyBlockSize])

        for bodyBlock in self.body :
            temp =[bodyBlock[0], bodyBlock[1]]

            bodyBlock[0] = previous[0]
            bodyBlock[1] = previous[1]

            previous = temp

            pygame.draw.rect(gameDisplay, self.bodyColour, [bodyBlock[0],bodyBlock[1],self.bodyBlockSize,self.bodyBlockSize])

        if self.needsGrowth :
            self.body.append(previous)
            pygame.draw.rect(gameDisplay, self.bodyColour, [previous[0],previous[1],self.bodyBlockSize,self.bodyBlockSize])
            self.size+=1
            self.needsGrowth = False


    def dirChange(self, event, pygame) :
        if self.turnedThisTurn :
            return

        if event.key == pygame.K_UP :
            if self.direction != 2 :
                self.direction = 1
        elif event.key == pygame.K_DOWN :
            if self.direction != 1 :
                self.direction = 2
        elif event.key == pygame.K_LEFT :
            if self.direction != 4 :
                self.direction = 3
        elif event.key == pygame.K_RIGHT :
            if self.direction != 3 :
                self.direction = 4
        self.turnedThisTurn = True
