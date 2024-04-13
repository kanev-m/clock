import tkinter
from tkinter import *
from time import *
from datetime import datetime
import pytz


def clock():
    # отображение дня недели
    day_string = strftime("%A")
    day_screen.config(text=day_string)

    # отображение даты
    date_string = strftime("%d %B %Y")
    date_screen.config(text=date_string)

    # отображение московского времени
    time_string = strftime("%H:%M:%S  EU/Moscow")
    time_screen_msc.config(text=time_string)

    time_screen_msc.after(1000, clock)


def newyork():
    # отображение времени в Нью-Йорке
    time_now = datetime.now(pytz.timezone('America/New_York'))
    current_time = time_now.strftime('%H:%M:%S  USA/New-York')
    time_screen_ny.config(text=current_time)
    time_screen_ny.after(1000, newyork)


def tokyo():
    # отображение времени в Токио
    time_now = datetime.now(pytz.timezone('Asia/Tokyo'))
    current_time = time_now.strftime('%H:%M:%S  Asia/Tokyo')
    time_screen_tky.config(text=current_time)
    time_screen_tky.after(1000, tokyo)


def dubai():
    # отображение времени в Дубай
    time_now = datetime.now(pytz.timezone('Asia/Dubai'))
    current_time = time_now.strftime('%H:%M:%S  Asia/Dubai')
    time_screen_db.config(text=current_time)
    time_screen_db.after(1000, dubai)


def london():
    # отображение времени в Лондоне
    time_now = datetime.now(pytz.timezone('Europe/London'))
    current_time = time_now.strftime('%H:%M:%S  EU/London')
    time_screen_lnd.config(text=current_time)
    time_screen_lnd.after(1000, london)


def sydney():
    # отображение времени в Сидней
    time_now = datetime.now(pytz.timezone('Australia/Sydney'))
    current_time = time_now.strftime('%H:%M:%S  Australia/Sydney')
    time_screen_sdn.config(text=current_time)
    time_screen_sdn.after(1000, sydney)


def beijing():
    # отображение времени в Пекине
    time_now = datetime.now(pytz.timezone('Asia/Shanghai'))
    current_time = time_now.strftime('%H:%M:%S  Asia/Beijing')
    time_screen_pk.config(text=current_time)
    time_screen_pk.after(1000, beijing)


window = Tk()
window.geometry('850x700')

# кнопка для отображения времени в Пекине
btn = tkinter.Button(window,
                     text='Beijing',
                     command=beijing,
                     activebackground='#A9A9A9')
btn.place(x=0, y=0)

# кнопка для отображения времени в Сиднее
btn = tkinter.Button(window,
                     text='Sydney',
                     command=sydney,
                     activebackground='#A9A9A9')
btn.place(x=47, y=0)

# кнопка для отображения времени в Лондоне
btn = tkinter.Button(window,
                     text='London',
                     command=london,
                     activebackground='#A9A9A9')
btn.place(x=96, y=0)

# кнопка для отображения времени в Дубай
btn = tkinter.Button(window,
                     text='Dubai',
                     command=dubai,
                     activebackground='#A9A9A9')
btn.place(x=148, y=0)

# кнопка для отображения времени в Токио
btn = tkinter.Button(window,
                     text='Tokyo',
                     command=tokyo,
                     activebackground='#A9A9A9')
btn.place(x=190, y=0)

# кнопка для отображения времени в Нью-Йорке
btn = tkinter.Button(window,
                     text='New-Yorke',
                     command=newyork,
                     activebackground='#A9A9A9')
btn.place(x=233, y=0)

# параметры дня недели
day_screen = Label(window, font=("Times New Roman", 30), fg="#48D1CC")
day_screen.pack()

# параметры даты
date_screen = Label(window, font=("Times New Roman", 40), fg="#FF7F50")
date_screen.pack()

# параметры экрана со временем мск (шрифт, размер, цвет)
time_screen_msc = Label(window, font=("Times New Roman", 60), fg="black")
time_screen_msc.pack()

# параметры экрана со временем в Лондоне
time_screen_lnd = Label(window, font=("Times New Roman", 50), fg="#696969")
time_screen_lnd.pack()

# параметры экрана со временем в Нью-Йорке
time_screen_ny = Label(window, font=("Times New Roman", 50), fg="#696969")
time_screen_ny.pack()

# параметры экрана со временем в Токио
time_screen_tky = Label(window, font=("Times New Roman", 50), fg="#696969")
time_screen_tky.pack()

# параметры экрана со временем в Дубай
time_screen_db = Label(window, font=("Times New Roman", 50), fg="#696969")
time_screen_db.pack()

# параметры экрана со временем в Сидней
time_screen_sdn = Label(window, font=("Times New Roman", 50), fg="#696969")
time_screen_sdn.pack()

# параметры экрана со временем в Пекине
time_screen_pk = Label(window, font=("Times New Roman", 50), fg="#696969")
time_screen_pk.pack()

window.title('Clock')

clock()

window.mainloop()