from snake import Snake
from turtle import Screen
import time

is_move = True
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=500,height=700)
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_move:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()