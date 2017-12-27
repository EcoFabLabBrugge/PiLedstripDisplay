class PatternCreator:
    xPixel = 10
    yPixel = 10
    frame = 0
    x = 0
    y = 0
    c = 1
    color = [0xc1c059, 0x37b3cc]
    def __init__(self, xPixel, yPixel):
        self.xPixel = xPixel
        self.yPixel = yPixel

        self.frame = [[0xc1c059 for x in range(xPixel)] for y in range(yPixel)] 

    def AllRed(self):
        return self.frame
    def GetFrame(self):
        self.frame[self.y][self.x] = self.color[self.c]
        self.x += 1
        if self.xPixel == self.x:
            self.x = 0
            self.y += 1
        if self.yPixel == self.y:
            self.y = 0
            if self.c == 0:
                self.c = 1
            else:
                self.c = 0

        return self.frame