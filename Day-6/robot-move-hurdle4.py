#https://bit.ly/3mWEVrF

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def down():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if wall_in_front():
        turn_left()
        while wall_on_right() and is_facing_north():
            move()
        if not wall_on_right():
            down()
    else:
        move()
