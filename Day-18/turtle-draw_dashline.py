from turtle import Turtle, Screen

minion = Turtle()
minion.shape("turtle")

for _ in range(4):
    for _ in range(20):
        minion.down()
        minion.forward(1)
        minion.up()
        minion.forward(4)
    minion.left(90)

screen = Screen()
screen.exitonclick()