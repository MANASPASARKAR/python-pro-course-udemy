from canvas import Canvas
from rectangle import Rectangle
from square import Square

# canvas = Canvas(width=50, height=50, color=(255, 255, 255))
# square = Square(x=20, y=25, color=(50, 200, 200), side=5)
# square.draw(canvas)
# rectangle = Rectangle(x=35, y=40, color=(50, 250, 150), width=5, height=9)
# rectangle.draw(canvas)
# canvas.make('canvas.png')

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

colors = {"white" : (255, 255, 255), "black": (0,0,0)}
canvas_color = str(input("Enter canvas color (only black or white): "))

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])


while True:

    shape = str(input("What would you like to draw (square or rectangle)? write quit to quit: "))

    if shape.lower() == "rectangle":
        rec_x = int(input("Enter x of rectangle: "))
        rec_y = int(input("Enter y of rectangle: "))
        rec_width = int(input("Enter width of rectangle: "))
        rec_height = int(input("Enter height of rectangle: "))
        red = int(input("Enter red value (0-255) : "))
        green = int(input("Enter green value (0-255) : "))
        blue = int(input("Enter blue value (0-255) : "))
        rectangle = Rectangle(rec_x, rec_y, rec_width, rec_height, color=(red, green, blue))
        rectangle.draw(canvas)

    elif shape.lower() == "square":
        sq_x = int(input("Enter x of square: "))
        sq_y = int(input("Enter y of square: "))
        sq_side = int(input("Enter side of square: "))
        red = int(input("Enter red value (0-255) : "))
        green = int(input("Enter green value (0-255) : "))
        blue = int(input("Enter blue value (0-255) : "))
        square = Square(sq_x, sq_y, side=sq_side, color=(red, green, blue))
        square.draw(canvas)

    elif shape.lower() == "quit":
        break

    else:
        print("Sorry we cant make that shape yet!!")


canvas.make("canvas.png")
print("Image saved successfully as canvas.png")



