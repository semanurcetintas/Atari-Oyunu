from turtle import Turtle

class Top(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10 #Bu, topun her döngüde x ekseninde 10, y ekseninde 10 birim hareket edeceği anlamına gelir
        self.y_move=10
        self.move_speed=0.1


    def move(self):
         new_x=self.xcor() + self.x_move
         new_y=self.ycor() + self.y_move
         self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *=-1

    def bounce_x(self):
        self.x_move *=-1
        self.move_speed *= 0.9

    def reset_posision(self):
        self.goto(0,0)
        self.bounce_x()








