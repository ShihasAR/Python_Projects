from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(3, 5))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    input_3.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input.get().title()
    email = input_2.get()
    passw = input_3.get()
    new_data = {
        website:
            {
                "email": email,
                "password": passw
            }
    }
    if len(website) == 0 or len(passw)==0 :
        messagebox.showinfo(title="EMPTY FIELDS",message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Email is : {email}\nPassword is : {passw}\n"
                                                             f"Is this ok? ")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data, data_file, indent= 4)
            finally:
                input.delete(0, 'end')
                input_3.delete(0, 'end')

def find_password():
    website = input.get().title()
    try:
      with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No such File Exists")
    else:
      if website in data:
         messagebox.showinfo(title=website, message=f"Email : {data[website]['email']}\n"
                                                   f"Password : {data[website]['password']}")
      else:
          messagebox.showinfo(title="Error",message="No details of such website exits")








# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20,bg= "white")
canvas = Canvas(width= 200, height= 200,bg="white",highlightthickness=0)
logo = PhotoImage(file="logo.png")


canvas.create_image(100,100,image = logo)
canvas.grid(column=1,row=0)


website_label = Label(text= "Website :")
website_label.grid(column=0,row= 1)
input = Entry(width=21)
input.focus()
input.grid(column=1,row=1)


email_label = Label(text= "Email:")
email_label.grid(column=0,row= 2)
input_2 = Entry(width=39)
input_2.insert(0,"@gmail.com")
input_2.grid(column=1,row=2,columnspan = 2)


password_label = Label(text= "Password :")
password_label.grid(column=0, row= 3)
input_3 = Entry(width=21)
input_3.grid(column=1, row= 3)



button = Button(text="Generate Password",bg="white",command=generate_password)
button.grid(column=2, row = 3)

button_add = Button(text="Add", width= 30,bg="white",command=save)
button_add.grid(column=1, row= 4,columnspan=2)

search_button = Button(text="search",width=10,bg="white",command=find_password)
search_button.grid(column=3,row=1)






window.mainloop()