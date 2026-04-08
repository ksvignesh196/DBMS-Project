from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas


def clock():
    global date
    global currtime
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


def search_student():
    def search_data():
        con = pymysql.connect(host='localhost', user='root', passwd='root', database='schoolmanagementsystem')
        cur = con.cursor()
        db = 'select * from student where id=%s or name=%s or Mobile_no =%s '
        cur.execute(db, (identry.get(), nameentry.get(), Mobentry.get()))
        studenttable.delete(*studenttable.get_children())
        fetched_data = cur.fetchall()
        for i in fetched_data:
            studenttable.insert('', END, value=i)

        searchwindow.destroy()

    searchwindow = Toplevel()
    searchwindow.title('SEARCH')
    searchwindow.grab_set()
    searchwindow.resizable(False, False)

    idlabel = Label(searchwindow, text='ID', font=('arial', 20, ' italic bold'), fg='blue')
    idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    identry = Entry(searchwindow, font=('arial', 15, 'bold'))
    identry.grid(row=0, column=1, padx=10, pady=15)

    namelabel = Label(searchwindow, text='NAME', font=('arial', 20, ' italic bold'), fg='blue')
    namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    nameentry.grid(row=1, column=1, padx=10, pady=15)

    Moblabel = Label(searchwindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    Mobentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=2, column=1, padx=10, pady=15)

    searchstudentbutton = ttk.Button(searchwindow, text='SEARCH STUDENT', command=search_data)
    searchstudentbutton.grid(row=5, columnspan=5, pady=15)


def exit_sms():
    res = messagebox.askyesno('Confirm', 'Do you want to exit')
    if res == True:
        root.destroy()
    else:
        pass


####
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')
root.geometry('%dx%d' % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.title('SCHOOL MANAGEMENT SYSTEM')
root.resizable(False, False)

datelabel = Label(root, font=('times new roman', 18, 'bold'))
datelabel.place(x=5, y=5)
clock()
s = 'STUDENT MANAGEMENT SYSTEM'
sliderlabel = Label(root, font=('ALGERIAN', 25, 'italic bold'), fg='red', width=30)
sliderlabel.place(x=300, y=0)
slider()

leftframe = Frame(root)
leftframe.place(x=50, y=80, width=300, height=550)

exitbutton = ttk.Button(leftframe, text='EXIT', width=25, command=exit_sms)
exitbutton.grid(row=7, column=0, pady=5)

logoimage = PhotoImage(file='students.png')
logolabel = Label(leftframe, image=logoimage)
logolabel.grid(row=0, column=0)

searchstubutton = ttk.Button(leftframe, text='Search Student', width=25, command=search_student)
searchstubutton.grid(row=1, column=0, pady=10)

rightframe = Frame(root)
rightframe.place(x=350, y=80, width=820, height=550)

scrollbar1 = Scrollbar(rightframe, orient=HORIZONTAL)
scrollbar2 = Scrollbar(rightframe)

studenttable = ttk.Treeview(rightframe, columns=(
    'Admission No.', 'Name', 'DOB', 'Age', 'Gender', 'Father Name', 'Mother Name', 'Mobile No.', 'Address', 'Email',
    'Date'),
                            xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set)

scrollbar1.config(command=studenttable.xview)
scrollbar2.config(command=studenttable.yview)

scrollbar1.pack(side=BOTTOM, fill=X)
scrollbar2.pack(side=RIGHT, fill=Y)

studenttable.pack(fill=BOTH, expand=2)

studenttable.heading('Admission No.', text='Admission No.')
studenttable.heading('Name', text='Name')
studenttable.heading('DOB', text='DOB')
studenttable.heading('Age', text='Age')
studenttable.heading('Gender', text='Gender')
studenttable.heading('Father Name', text='Father Name')
studenttable.heading('Mother Name', text='Mother Name')
studenttable.heading('Mobile No.', text='Mobile No.')
studenttable.heading('Address', text='Address')
studenttable.heading('Email', text='Email')
studenttable.heading('Date', text='Date')

studenttable.column('Admission No.', width=200, anchor=CENTER)
studenttable.column('Name', width=200, anchor=CENTER)
studenttable.column('DOB', width=200, anchor=CENTER)
studenttable.column('Age', width=200, anchor=CENTER)
studenttable.column('Gender', width=200, anchor=CENTER)
studenttable.column('Father Name', width=200, anchor=CENTER)
studenttable.column('Mother Name', width=200, anchor=CENTER)
studenttable.column('Mobile No.', width=200, anchor=CENTER)
studenttable.column('Address', width=200, anchor=CENTER)
studenttable.column('Email', width=200, anchor=CENTER)
studenttable.column('Date', width=200, anchor=CENTER)

style = ttk.Style()

style.configure('Treeview', rowheight=40, font=('times new roman', 15), foreground='purple', background='white',
                fieldbackground='white')
style.configure('Treeview.Heading', font=('times new roman', 15), foreground='Royal blue')
studenttable.config(show='headings')

root.mainloop()
