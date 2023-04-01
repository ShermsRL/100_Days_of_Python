# import colorgram
#
# colors = colorgram.extract('image.jpg', 15)
# color_palette = []
# number = 0
#
# for color in colors:
#     color = colors[number].rgb
#     rgb = (color[0], color[1], color[2])
#     color_palette.append(rgb)
#     number += 1
#
# print(color_palette)

import random
from turtle import Turtle, Screen, colormode

color_palette = [(221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157),
                 (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33)]


def paint_row():
    colormode(255)
    for _ in range(10):
        hirst_turtle.dot(20, random.choice(color_palette))
        hirst_turtle.penup()
        hirst_turtle.forward(50)


position = -250
loop = 0
hirst_turtle = Turtle()
hirst_turtle.penup()
hirst_turtle.setposition(0, position)


painting_done = False
while not painting_done:
    paint_row()
    position += 50
    hirst_turtle.setposition(0, position)
    loop += 1
    if loop >= 10:
        painting_done = True

screen = Screen()
screen.exitonclick()
