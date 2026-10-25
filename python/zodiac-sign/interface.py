from tkinter import *

root = Tk()
root.geometry('300x500')
root.title('Зодиаки')
zodiac_names = ['Неправильная дата рождения!', 'Козерог', 'Водолей', 'Рыбы', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец']
zodiac_files = ['start.gif', 'capricorn.gif', 'aquarius.gif', 'pisces.gif', 'aries.gif', 'taurus.gif', 'gemini.gif', 'cancer.gif', 'leo.gif', 'virgo.gif', 'libra.gif', 'scorpio.gif', 'sagittarius.gif']
frame1 = LabelFrame(root, text='Дата рождения', width=280, height=120)
name = Label(root, text='Сначала введите дату рождения')
gif = PhotoImage(file='img/start.gif')
image = Label(image=gif)
text1 = Label(frame1, text='Введите день')
text2 = Label(frame1, text='Введите месяц')
entry1 = Entry(frame1)
entry2 = Entry(frame1)
button = Button(frame1, text='Определить знак')
frame1.grid(padx=10, pady=10)
name.grid()
image.grid()
text1.grid(sticky=W, padx=17, pady=5, column=0, row=1)
text2.grid(sticky=W, padx=17, pady=5, column=0, row=2)
entry1.grid(padx=17, pady=5, column=1, row=1)
entry2.grid(padx=17, pady=5, column=1, row=2)
button.grid(padx=17, pady=5, columnspan=2, row=3)

if __name__ == '__main__':
    root.mainloop()