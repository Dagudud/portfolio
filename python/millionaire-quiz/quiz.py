from tkinter import *
from tkinter import messagebox
from random import shuffle

root = Tk()
root.geometry('900x700+300+200')

questions = [['Как заканчивается призказка: "Мы и сами с..."?', 'с волосами', 'с усами', 'с часами', 'с долгами', 'с усами',],
             ['Как в обиходе называют растение, которое часто \n дарят женщинам к празднику 8 марта?', 'оливье', 'винигрет', 'мимоза', 'селёдка под шубой', 'мимоза'],
             ['На каком курсе школы Хогвартс учился Гарри Поттер,\n когда раскрыл секрет Тайной комнаты?', 'на первом', 'на втором', 'на третьем', 'на четвёртом', 'на втором']]
numQue = 0
btns = questions[numQue][1:5]
shuffle(btns)
pic = PhotoImage(file='img/logo.gif')
picl = Label(root, image=pic)

queL = Label(root, text=questions[numQue][0], font='Verdana 22')
btn1 = Button(root, text=btns[0], font='Verdana 22', width=20, command=lambda: check(btns[0]))
btn2 = Button(root, text=btns[1], font='Verdana 22', width=20, command=lambda: check(btns[1]))
btn3 = Button(root, text=btns[2], font='Verdana 22', width=20, command=lambda: check(btns[2]))
btn4 = Button(root, text=btns[3], font='Verdana 22', width=20, command=lambda: check(btns[3]))

picl.grid(row=0, column=0, columnspan=2)
queL.grid(row=1, column=0, columnspan=2)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=3, column=0)
btn4.grid(row=3, column=1)

def check(otv):
    global numQue
    if otv == questions[numQue][5]:
        messagebox.showinfo('Правильно!', 'Молодец!')
        numQue += 1
        btns = questions[numQue][1:5]
        shuffle(btns)
        queL.config(text=questions[numQue][0])
        btn1.config(text=btns[0], command=lambda: check(btns[0]))
        btn2.config(text=btns[1], command=lambda: check(btns[1]))
        btn3.config(text=btns[2], command=lambda: check(btns[2]))
        btn4.config(text=btns[3], command=lambda: check(btns[3]))
    else:
        messagebox.showerror('Неправильно!', 'Жаль, но на этом ваша игра окончена :(')

root.mainloop()