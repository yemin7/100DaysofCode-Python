from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

is_move = True
WIDTH = 800
HEIGHT= 800
WIDTH_MINUS = -(WIDTH/2)+20
WIDTH_PLUS= (WIDTH/2)-20
HEIGHT_MINUS= -(HEIGHT/2)+20
HEIGHT_PLUS= (HEIGHT/2)-20

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=WIDTH,height=HEIGHT)
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard(HEIGHT_PLUS)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_move:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh(x_minus=WIDTH_MINUS, x_plus=WIDTH_PLUS, y_minus=HEIGHT_MINUS, y_plus=HEIGHT_PLUS)
        snake.extend()
        score.score_plus()
    
    #Detect collision with the wall
    if snake.head.xcor() < WIDTH_MINUS or snake.head.xcor() > WIDTH_PLUS or snake.head.ycor() < HEIGHT_MINUS or snake.head.ycor() > HEIGHT_PLUS:
        is_move = False
        score.gameover()

    #Detect collision with tail
    for segment in snake.new_position[1:]:
        if snake.head.distance(segment) < 15:
            is_move = False
            score.gameover()


screen.exitonclick()