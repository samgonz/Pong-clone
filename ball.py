from random import randint
from turtle import Turtle

MOVE_DISTANCE = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()        
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color('white')
        self.speed('fastest')  
        
    def move(self, direction=randint(0, 360)):
        self.setheading(direction)
        self.forward(10)