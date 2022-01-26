from turtle import Turtle, Screen

minion = Turtle()

screen = Screen()

def moveforward():
    minion.fd(10)

def moveback():
    minion.bk(10)

def moveright():
#    minion.rt(10)
    setheading = minion.heading() + 10
    minion.setheading(setheading)

def moveleft():
#    minion.lt(10)
    setheading = minion.heading() - 10
    minion.setheading(setheading)

def resetscreen():
    screen.reset()

screen.onkey(moveforward, "w")
screen.onkey(moveright, "d")
screen.onkey(moveleft, "a")
screen.onkey(moveback, "s")
screen.onkey(resetscreen, "c")

screen.listen()
screen.exitonclick()