from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
ball.speed('slow')
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.forward, 'Up')
screen.onkeypress(r_paddle.backward, 'Down')
screen.onkeypress(l_paddle.forward, 'w')
screen.onkeypress(l_paddle.backward, 's')

game_on = True
i = -5

while game_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270 :
        ball.bounce_y()

    elif ball.distance(r_paddle) < 50 and ball.xcor() > 340  or ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.bounce_x()


    elif ball.xcor() > 420:
        ball.reset_pos()
        scoreboard.l_point()

    elif ball.xcor() < -420:
        ball.reset_pos()
        scoreboard.r_point()






screen.exitonclick()
