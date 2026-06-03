class Square:

    def __init__(self, x, y, color, side):
        self.x = x
        self.y = y
        self.color = color
        self.side = side

    def draw(self, canvas):
        canvas.data[self.y : self.y + self.side , self.x : self.x + self.side] = self.color
