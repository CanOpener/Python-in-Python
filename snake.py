import bodyBlock

class snake :
    body = []
    bodyBlockSize = None
    bodyBlockColour = None
    headBlockColour = None

    def move(self, posX, posY) :

        priorX = posX
        priorY = posY

        for bodyPart in body :

            tempX = bodyPart.xPos
            tempY = bodyPart.yPos
            bodyPart.xPos = priorX
            bodyPart.yPos = priorY
            priorX = tempX
            priorY = tempY
            bodyPart.drawSelf()

    def __init__(self, size, x, y, hc, bc) :
        self.bodyBlockSize = size
        self.headBlockColour = hc
        self.bodyBlockColour = bc

        head = bodyBlock(x, y, hc, size)
        body.push(head)
