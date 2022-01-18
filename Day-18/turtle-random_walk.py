from os import minor
from turtle import Turtle, Screen
from random import choice


#colors = ["gold", "red", "salmon", "yellow", "purple", "black", "DarkGreen", "blue3", "hotpink", "LightCyan", "lavender"]
direction = [0, 90, 180, 270]

minion = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = choice(range(0,255))
    g = choice(range(0,255))
    b = choice(range(0,255))
    random_color = (r, g, b)
    return random_color

minion.shape('circle')
minion.pensize(10)
minion.speed('fastest')

for _ in range(200):
    colors = choice(range(1,256))
    #minion.color(choice(colors))
    minion.color(random_color())
    minion.setheading(choice(direction))
    minion.forward(20)

screen.exitonclick()


