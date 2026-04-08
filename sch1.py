from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameentry.get() == '' or passwordentry.get() == '':
        messagebox.showerror('ERROR', 'Fields cannot be empty')
    elif usernameentry.get() == 'root' and passwordentry.get() == 'SMS':
        messagebox.showinfo('Success', 'Welcome')
        root.destroy()
        import choice

    else:
        messagebox.showerror('Error', 'Enter correct credentials')


root = Tk()
root.geometry('%dx%d' % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.title('LOGIN')

root.resizable(False, False)

BGImage = ImageTk.PhotoImage(file='sms.png')
BGLabel = Label(root, image=BGImage)
BGLabel.place(x=0, y=0)

loginframe = Frame(root, bg='white')
loginframe.place(x=340, y=200)

loginimage = ImageTk.PhotoImage(file='graduated.png')
logolabel = Label(loginframe, image=loginimage)
logolabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameimage = ImageTk.PhotoImage(file='id-card.png')
usernamelabel = Label(loginframe, image=usernameimage, text='Username', compound=LEFT, font=('times new roman', 20),
                      bg='white')
usernamelabel.grid(row=1, column=0, pady=10, padx=20)

usernameentry = Entry(loginframe, font=('ARIAL', 18), bd=5, fg='royalblue')
usernameentry.grid(row=1, column=1, pady=10, padx=20)

passwordimage = ImageTk.PhotoImage(file='lock.png')
passwordlabel = Label(loginframe, image=passwordimage, text='Password', compound=LEFT, font=('times new roman', 20),
                      bg='white')
passwordlabel.grid(row=2, column=0, pady=10, padx=20)

passwordentry = Entry(loginframe, font=('ARIAL', 18), bd=5, fg='royalblue', show='*')
passwordentry.grid(row=2, column=1, pady=10, padx=20)

loginbutton = Button(loginframe, text='LOGIN', font=('times new roman', 17), width=15, fg='white', bg='blue',
                     activebackground='blue', activeforeground='white',
                     cursor='hand2', command=login)
loginbutton.grid(row=3, column=1, pady=10)

root.mainloop()
