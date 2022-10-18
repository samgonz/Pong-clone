import time
from turtle import Turtle, Screen
from ball import Ball

from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.screensize(400,400)

player_one_paddle = Paddle()
player_two_paddle = Paddle()
ball = Ball()

player_one_paddle.player('player_one')
player_two_paddle.player('player_two')

# Creates a listener to listen for keyboard events
screen.listen()
screen.onkey(player_one_paddle.up,"w")
screen.onkey(player_one_paddle.down,"s")
screen.onkey(player_two_paddle.up,"Up")
screen.onkey(player_two_paddle.down,"Down")

game_is_on = True
# Creates a loop that updates the screen every .1 second.
while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.move()
    
    if ball.distance(player_one_paddle) < 5 or ball.distance(player_two_paddle) < 5:
        ball_heading = ball.heading()
        
        if ball_heading > 180:
            new_heading = int(ball_heading) + 180
            print(new_heading)
            if new_heading > 360:
                new_heading -= 360
            print(new_heading)
            ball.move(new_heading)    
        else:
            new_heading = int(ball_heading) + 180
            print(new_heading)
            if new_heading < 0:
                new_heading += 360   
            print(new_heading)
            ball.move(new_heading)   

        print(ball_heading)

screen.exitonclick()
