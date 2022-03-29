from csv import writer
import pandas
import datetime as dt
import random
# 1. Update the birthdays.csv
# row = ["tom","tom@gmail.com",1996,2,30]
# with open("birthdays.csv","a",newline='') as file:
#     csvwriter = writer(file)
#     csvwriter.writerow(row)


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
d = now.day
m = now.month
data = pandas.read_csv("birthdays.csv")
day = True
i=0
Letter = ""
while day:
 if data.day[i] == d and data.month[i] == m:
    day = False
    num = random.randint(1, 3)
    with open(f"letter_templates/letter_{num}.txt", "r") as file:
        fd = file.read()
        fd = fd.replace('[NAME]', f'{data.name[i]}')
    with open(f"letter_templates/letter_{num}.txt", "w") as file:
        file.write(fd)
        print(file)
else:
     i+=1


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv





# 4. Send the letter generated in step 3 to that person's email address.




