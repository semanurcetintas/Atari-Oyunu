from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,posision):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        # stretch_wid = yüksekliği kontrol eder (varsayılan = 1) ,stretch_len = genişliği kontrol eder (varsayılan = 1)
        # ekstra genişlikde değişiklik yapmak istediğin zman kullanıyorsun
        self.penup()
        self.goto(posision)


    def go_up(self):
       new_y= self.ycor() + 20
       self.goto(self.xcor(), new_y)

    def go_down(self):
       new_y = self.ycor() - 20
       self.goto(self.xcor(), new_y)


