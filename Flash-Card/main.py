from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
word = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dict = original_data.to_dict(orient="records")
else:
  dict = data.to_dict(orient="records")

def next_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(dict)
    current_word = word["French"]
    canvas.itemconfig(Title,text = "French",fill = "black")
    canvas.itemconfig(Word,text = current_word,fill = "black")
    flip_timer = window.after(3000,eng_word)


def is_known():
    dict.remove(word)
    next_word()
    data = pandas.DataFrame(dict)
    data.to_csv("data/words_to_learn.csv",index = False)


def eng_word():
    global word
    answer =  word["English"]
    canvas.itemconfig(front_image, image=back_img)
    canvas.itemconfig(Title, text = "English",fill = "white")
    canvas.itemconfig(Word, text = answer,fill = "white")


window = Tk()
window.config(padx=50,pady= 50, bg = BACKGROUND_COLOR)
canvas = Canvas(width= 900, height= 526,bg= BACKGROUND_COLOR ,highlightthickness=0)
img_front = PhotoImage(file="images/card_front.png")
front_image = canvas.create_image(450, 270, image = img_front)
Title = canvas.create_text(430,150, text= "",font = ("Ariel",40,"italic"),fill = "black")
Word = canvas.create_text(430,263, text= "",font = ("Ariel",60,"bold"),fill = "black")
back_img = PhotoImage(file="images/card_back.png")
flip_timer = window.after(3000, eng_word)
canvas.grid(column=0,row= 0,columnspan= 2)



button_right = PhotoImage(file= "images/right.png")
button1 = Button(image= button_right, highlightthickness=0,command=is_known)
button1.grid(column=0,row = 1)
button_wrong = PhotoImage(file="images/wrong.png")
button2 = Button(image= button_wrong,highlightthickness=0,command=next_word)
button2.grid(column=1,row= 1)

next_word()

window.mainloop()





