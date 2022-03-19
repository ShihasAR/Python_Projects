import random
from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.color("purple")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)

    def extend_segment(self):
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for t in range(len(self.turtle_list) - 1, 0, -1):
                new_xcor = self.turtle_list[t - 1].xcor()
                new_ycor = self.turtle_list[t - 1].ycor()
                self.turtle_list[t].goto(new_xcor, new_ycor)
        self.head.forward(DISTANCE)

    def reset(self):
        for s in self.turtle_list:
            s.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    def up(self):
        if self.head.heading() != DOWN:
          self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
          self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
          self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
          self.head.setheading(RIGHT)



