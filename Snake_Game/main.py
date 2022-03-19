from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
score= Scoreboard()
game_on = True
snk = Snake()
food = Food()
screen.listen()
screen.onkey(snk.up,"Up")
screen.onkey(snk.down,"Down")
screen.onkey(snk.right,"Right")
screen.onkey(snk.left,"Left")

while game_on:
    time.sleep(0.1)
    screen.update()
    snk.move()

    if snk.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snk.extend_segment()

    if snk.head.xcor() > 280 or snk.head.xcor() < -280 or snk.head.ycor() > 280 or snk.head.ycor() < -280:
        snk.reset()
        score.high_s()


























screen.exitonclick()