from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self):
        super().__init__()        
        self.shape('square')
        self.penup()
        self.setheading(UP)
        self.shapesize(stretch_len= 5.0, stretch_wid= 0.5)
        self.color('white')
        self.speed('fastest')  
           
    def player(self, player):
        if player == 'player_one':
            self.goto(-400, 0)   
        if player == 'player_two':
            self.goto(400, 0)   
            
    def up(self):
        self.setheading(UP)        
        self.forward(MOVE_DISTANCE)

            
    def down(self):
        self.setheading(DOWN)     
        self.forward(MOVE_DISTANCE)  

        