from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time_count = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(time_count)
    canvas.itemconfig(timer_text,text= "0:00")
    label.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    long_break  = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    reps += 1
    if reps == 8:
        count_down(long_break)
        label.config(text="Break",fg=RED)
    elif reps % 2!= 0 :
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
    else:
        count_down(short_break)
        label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count>0:
        global time_count
        time_count = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
            check.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 50,pady=50, bg=YELLOW)
canvas = Canvas(width=300,height=300, bg= YELLOW)
tomato_img = PhotoImage(file="tomato.png")
label = Label(text="TIMER",bg=YELLOW,fg= GREEN,font=(FONT_NAME,50,"bold"))
label.grid(column=1,row=0)
check = Label(text="", fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)
canvas.create_image(160,150, image= tomato_img)
timer_text = canvas.create_text(160,170,text="0:00",fill = "white",font=(FONT_NAME,24,"bold"))
canvas.grid(column=1,row=1)
button_start = Button(text="Start",command=start_timer)
button_reset = Button(text="Reset",command=reset_timer)
button_start.grid(column=0,row=3)
button_reset.grid(column=2,row=3)


window.mainloop()