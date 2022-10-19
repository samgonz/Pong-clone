from turtle import Turtle
 
def Dashed_Line():
    dashed_line = Turtle()
    dashed_line.speed('fastest')
    dashed_line.goto(0, 400)
    dashed_line.setheading(270)
    dashed_line.shape("circle")
    dashed_line.color("white")

    for _ in range(40):
        dashed_line.pencolor("white")
        dashed_line.forward(10)
        dashed_line.penup()
        dashed_line.forward(10)
        dashed_line.pendown()
    dashed_line.hideturtle()