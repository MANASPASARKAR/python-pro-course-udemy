class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def draw(self, canvas):
        canvas.data[self.y : self.y + self.height , self.x : self.x + self.width] = self.color
