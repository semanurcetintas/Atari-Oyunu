from turtle import Turtle, Screen
from paddle import Paddle
from top import Top
from  scoreboard import  Scoreboard
import time


screen=Screen()
screen.title("Atari Oyunum")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)  # animasyonu kapattı

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
top=Top()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    top.move()

    if top.ycor() > 280 or top.ycor() <-280:
        # bu durumda sıçraması gerekecek
        top.bounce_y()

    if top.distance(r_paddle) <50 and top.xcor() >340 or top.distance(l_paddle) <50 and top.xcor() <-340:
        top.bounce_x()

    if top.xcor() >380:
        top.reset_posision()
        scoreboard.l_point()

    if top.xcor() <-380:
        top.reset_posision()
        scoreboard.r_point()







screen.exitonclick()