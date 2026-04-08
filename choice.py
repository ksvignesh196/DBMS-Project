from tkinter import *
import time
import ttkthemes
from PIL import ImageTk
from tkinter import ttk


def clock():
    date = time.strftime('%d/%m/%Y')
    currtime = time.strftime('%H:%M:%S')
    datelabel.config(text=f'   Date:{date}\nTime:{currtime}')
    datelabel.after(1000, clock)


count = 0
text = ''


def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    count += 1
    sliderlabel.config(text=text)
    sliderlabel.after(200, slider)


def stu():
    root.destroy()
    import student


def teacher():
    root.destroy()
    import teacher


# gui

root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')
root.geometry('%dx%d' % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.title('SCHOOL MANAGEMENT SYSTEM')
root.resizable(False, False)
BGImage = PhotoImage(file='blank.png')
BGLabel = Label(root, image=BGImage)
BGLabel.place(x=0, y=0)

datelabel = Label(root, font=('times new roman', 12, 'italic'), bg='white')
datelabel.place(x=5, y=5)
clock()
s = 'STUDENT MANAGEMENT SYSTEM'
sliderlabel = Label(root, font=('ALGERIAN', 25, 'italic bold'), fg='red', width=30, bg='white')
sliderlabel.place(x=200, y=0)
slider()

Teacherbutton = ttk.Button(root, text='TEACHER', width=20, command=teacher)
Teacherbutton.place(x=100, y=400)

loginimage = ImageTk.PhotoImage(file='presentation.png')
Tlogolabel = Label(root, image=loginimage, bg='white')
Tlogolabel.place(x=30, y=130)

Studentbutton = ttk.Button(root, text='STUDENT', width=20, command=stu)
Studentbutton.place(x=550, y=400)

Studentlogo = ImageTk.PhotoImage(file='audience.png')
Slogolabel = Label(root, image=Studentlogo)
Slogolabel.place(x=550, y=150)

root.mainloop()