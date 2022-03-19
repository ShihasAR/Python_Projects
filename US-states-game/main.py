import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("States Game, type 'exit' to quit")
screen.addshape(image)
turtle.shape(image)
guess = screen.textinput(title="Enter State",prompt="Enter a state").title()
turtle.penup()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
game = True
score = 0
right_answer = ['none']
new_score = [0]

def check():
 for i in all_states:
    global guess
    if guess == i:
        right_answer.append(i)
        return 1

def repeat_ans():
  for j in right_answer:
    global guess
    if guess == j:
        return 2





def gameplay():
     global score
     global guess
     b = data[data.state == f"{guess}"]
     xcor = int(b.x)
     ycor = int(b.y)
     new_t = turtle.Turtle()
     new_t.penup()
     new_t.hideturtle()
     new_t.goto(xcor, ycor)
     new_t.write(f"{guess}")


def add_score():
    global guess
    global score
    score += 1
    new_score.append(score)
    guess = screen.textinput(title=f"{new_score[-1]}/50 States Correct", prompt="Enter a state").title()

def prompt():
    global guess
    guess = screen.textinput(title=f"{new_score[-1]}/50 States Correct", prompt="Enter a state").title()


while game:
    if guess == "Exit":
        game = False
    elif repeat_ans() == 2:
        prompt()
    elif check() == 1:
      gameplay()
      add_score()
    elif check() != 1:
        prompt()













turtle.mainloop()