from turtle import Screen, Turtle
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import dotted_line

screen = Screen()
screen.bgcolor("black")
screen.screensize(400,400)

player_one_paddle = Paddle((-380, 0))
player_two_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

# Creates the center line for the scoreboard
dotted_line.Dashed_Line()
    
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
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(player_two_paddle) < 50 and ball.xcor() > 350 or ball.distance(player_one_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        

screen.exitonclick()