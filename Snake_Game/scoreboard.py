from turtle import Turtle
FONT = ("Courier,24,normal")
ALIGNMENT = "center"





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def high_s(self):
        if self.score > self.high_score:
           self.high_score = self.score
           with open("data.txt", mode="w") as data:
             data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
       self.score += 1
       self.update_scoreboard()

