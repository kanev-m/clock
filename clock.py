from tkinter import *
from time import *


def clock():
    # отображение времени
    time_string = strftime("%H:%M:%S")
    time_screen.config(text=time_string)

    # отображение дня недели
    day_string = strftime("%A")
    day_screen.config(text=day_string)

    # отображение даты
    date_string = strftime("%d %B %Y")
    date_screen.config(text=date_string)

    time_screen.after(1000, clock)


window = Tk()

# параметры экрана со временем (шрифт, размер, цвет)
time_screen = Label(window, font=("Times New Roman", 100), fg="#9932CC", bg="black")
time_screen.pack()

# параметры дня недели
day_screen = Label(window, font=("Times New Roman", 30), fg="#48D1CC")
day_screen.pack()

# параметры даты
date_screen = Label(window, font=("Times New Roman", 40), fg="#FF7F50")
date_screen.pack()

clock()

window.mainloop()