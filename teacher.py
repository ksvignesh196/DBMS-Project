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
    datelabel.config(text=f'   Date: {date}\nTime: {currtime}')
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


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..................

def connect_database():
    def connect():
        global cur
        global con

        try:
            con = pymysql.connect(host=hostentry.get(), user=userentry.get(), password=passwordentry.get())
            cur = con.cursor()

        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connectroot)
            return

        try:
            db = 'create database schoolmanagementsystem'
            cur.execute(db)
            db = 'use schoolmanagementsystem'
            cur.execute(db)
            db = "create table teacher(ID int not null primary key, name varchar(50), DOB varchar(50), age int," \
                 "gender varchar(10), qualification varchar(20), post varchar(20), mob_No char(10)," \
                 "subject varchar(20), experience varchar(10), Date varchar(50))"
            cur.execute(db)
        except:
            db = 'use schoolmanagementsystem'
            cur.execute(db)

        messagebox.showinfo('Success', 'Database Connection is Successful', parent=connectroot)
        connectroot.destroy()
        addstubutton.config(state=NORMAL)
        searchstubutton.config(state=NORMAL)
        updatestubutton.config(state=NORMAL)
        showstubutton.config(state=NORMAL)
        exportstubutton.config(state=NORMAL)
        deletestubutton.config(state=NORMAL)

    connectroot = Toplevel()
    connectroot.grab_set()
    connectroot.geometry('470x250+750+200')
    connectroot.title('Data base Connection')
    connectroot.resizable(False, False)

    hostname = Label(connectroot, text='HOST NAME:', font=('arial', 18, 'italic bold'), fg='blue')
    hostname.grid(row=0, column=0, padx=20)
    hostentry = Entry(connectroot, font=('arial', 15), fg='red', bd=3)
    hostentry.grid(row=0, column=1, padx=40, pady=20)

    username = Label(connectroot, text='USER NAME:', font=('arial', 18, 'italic bold'), fg='blue')
    username.grid(row=1, column=0, padx=20)
    userentry = Entry(connectroot, font=('arial', 15), fg='red', bd=3)
    userentry.grid(row=1, column=1, padx=40, pady=20)

    password = Label(connectroot, text='PASSWORD:', font=('arial', 18, 'italic bold'), fg='blue')
    password.grid(row=2, column=0, padx=20)
    passwordentry = Entry(connectroot, font=('arial', 15), fg='red', bd=3, show='*')
    passwordentry.grid(row=2, column=1, padx=40, pady=20)

    connectbutton = ttk.Button(connectroot, text='CONNECT', command=connect)
    connectbutton.grid(row=3, columnspan=3)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..............................
def add_teacher():
    addwindow = Toplevel()
    addwindow.title('ADD TEACHER DETAILS')
    addwindow.grab_set()
    addwindow.resizable(False, False)

    idlabel = Label(addwindow, text='ID', font=('arial', 20, ' italic bold'), fg='blue')
    idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    identry = Entry(addwindow, font=('arial', 15, 'bold'))
    identry.grid(row=0, column=1, padx=10, pady=15)

    namelabel = Label(addwindow, text='NAME', font=('arial', 20, ' italic bold'), fg='blue')
    namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameentry = Entry(addwindow, font=('arial', 15, 'bold'))
    nameentry.grid(row=1, column=1, padx=10, pady=15)

    doblabel = Label(addwindow, text='DOB', font=('arial', 20, ' italic bold'), fg='blue')
    doblabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    dobentry = Entry(addwindow, font=('arial', 15, 'bold'))
    dobentry.grid(row=2, column=1, padx=10, pady=15)

    agelabel = Label(addwindow, text='AGE', font=('arial', 20, ' italic bold'), fg='blue')
    agelabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    ageentry = Entry(addwindow, font=('arial', 15, 'bold'))
    ageentry.grid(row=3, column=1, padx=10, pady=15)

    genderlabel = Label(addwindow, text='GENDER', font=('arial', 20, ' italic bold'), fg='blue')
    genderlabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    genderentry = Entry(addwindow, font=('arial', 15, 'bold'))
    genderentry.grid(row=4, column=1, padx=10, pady=15)

    qfnlabel = Label(addwindow, text='QUALIFICATION', font=('arial', 20, ' italic bold'), fg='blue')
    qfnlabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    qfnentry = Entry(addwindow, font=('arial', 15, 'bold'))
    qfnentry.grid(row=0, column=4, padx=10, pady=15)

    postlabel = Label(addwindow, text='POST', font=('arial', 20, ' italic bold'), fg='blue')
    postlabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    postentry = Entry(addwindow, font=('arial', 15, 'bold'))
    postentry.grid(row=1, column=4, padx=10, pady=15)

    Moblabel = Label(addwindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=2, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(addwindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=2, column=4, padx=10, pady=15)

    subjectlabel = Label(addwindow, text='SUBJECT', font=('arial', 20, ' italic bold'), fg='blue')
    subjectlabel.grid(row=3, column=3, padx=30, pady=15, sticky=W)
    subjectentry = Entry(addwindow, font=('arial', 15, 'bold'))
    subjectentry.grid(row=3, column=4, padx=10, pady=15)

    experiencelable = Label(addwindow, text='EXPERIENCE', font=('arial', 20, ' italic bold'), fg='blue')
    experiencelable.grid(row=4, column=3, padx=30, pady=15, sticky=W)
    experienceentry = Entry(addwindow, font=('arial', 15, 'bold'))
    experienceentry.grid(row=4, column=4, padx=10, pady=15)

    def add_data():
        l = [identry.get(), nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(), qfnentry.get(),
             postentry.get(), Mobentry.get(), subjectentry.get(), experienceentry.get()]

        for i in l:
            if i == '':
                messagebox.showerror('Error', 'All fields are required', parent=addwindow)
            else:
                try:
                    db = 'insert into teacher values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

                    cur.execute(db, (
                        identry.get(), nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(),
                        qfnentry.get(), postentry.get(), Mobentry.get(), subjectentry.get(), experienceentry.get(),
                        date))
                    con.commit()

                    result = messagebox.askyesno('Success', 'Data saved successfully. Do you want to clear the form?',
                                                 parent=addwindow)
                    if result:
                        identry.delete(0, END)
                        nameentry.delete(0, END)
                        dobentry.delete(0, END)
                        ageentry.delete(0, END)
                        genderentry.delete(0, END)
                        qfnentry.delete(0, END)
                        postentry.delete(0, END)
                        Mobentry.delete(0, END)
                        subjectentry.delete(0, END)
                        experienceentry.delete(0, END)

                except:
                    messagebox.showerror('Error', 'ID cannot be repeated', parent=addwindow)

                db = "select * from teacher"
                cur.execute(db)
                fetched_data = cur.fetchall()
                total_record = cur.rowcount
                teachertable.delete(*teachertable.get_children())
                for i in fetched_data:
                    data = list(i)
                    teachertable.insert('', END, values=data)
            addwindow.destroy()

    addteacherbutton = ttk.Button(addwindow, text='ADD TEACHER', command=add_data)
    addteacherbutton.grid(row=5, columnspan=5, pady=15)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..........................................................

def search_teacher():
    def search_data():
        db = 'select * from teacher where id=%s or name=%s or dob=%s or age=%s or gender=%s or qualification=%s ' \
             'or post=%s or mob_No=%s or subject=%s or experience=%s'

        cur.execute(db, (
            identry.get(), nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(), qfnentry.get(),
            postentry.get(), Mobentry.get(), subjectentry.get(), experienceentry.get()))

        teachertable.delete(*teachertable.get_children())
        fetched_data = cur.fetchall()
        total_record = cur.rowcount
        for i in fetched_data:
            teachertable.insert('', END, value=i)
        messagebox.showinfo('total record', total_record)
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

    doblabel = Label(searchwindow, text='DOB', font=('arial', 20, ' italic bold'), fg='blue')
    doblabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    dobentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    dobentry.grid(row=2, column=1, padx=10, pady=15)

    agelabel = Label(searchwindow, text='AGE', font=('arial', 20, ' italic bold'), fg='blue')
    agelabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    ageentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    ageentry.grid(row=3, column=1, padx=10, pady=15)

    genderlabel = Label(searchwindow, text='GENDER', font=('arial', 20, ' italic bold'), fg='blue')
    genderlabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    genderentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    genderentry.grid(row=4, column=1, padx=10, pady=15)

    qfnlabel = Label(searchwindow, text='QUALIFICATIONS', font=('arial', 20, ' italic bold'), fg='blue')
    qfnlabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    qfnentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    qfnentry.grid(row=0, column=4, padx=10, pady=15)

    postlabel = Label(searchwindow, text='POST', font=('arial', 20, ' italic bold'), fg='blue')
    postlabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    postentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    postentry.grid(row=1, column=4, padx=10, pady=15)

    Moblabel = Label(searchwindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=2, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=2, column=4, padx=10, pady=15)

    subjectlabel = Label(searchwindow, text='SUBJECT', font=('arial', 20, ' italic bold'), fg='blue')
    subjectlabel.grid(row=3, column=3, padx=30, pady=15, sticky=W)
    subjectentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    subjectentry.grid(row=3, column=4, padx=10, pady=15)

    experiencelabel = Label(searchwindow, text='EXPERIENCE', font=('arial', 20, ' italic bold'), fg='blue')
    experiencelabel.grid(row=4, column=3, padx=30, pady=15, sticky=W)
    experienceentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    experienceentry.grid(row=4, column=4, padx=10, pady=15)

    addteacherbutton = ttk.Button(searchwindow, text='SEARCH TEACHERS', command=search_data)
    addteacherbutton.grid(row=5, columnspan=5, pady=15)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..................................

def delete_teacher():
    index = teachertable.focus()
    content = teachertable.item(index)
    content_id = content['values'][0]
    db = 'delete from teacher where id=%s'
    cur.execute(db, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'This {content_id} is deleted  successfully')
    show_teacher()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>......................
def show_teacher():
    db = 'select * from teacher'
    cur.execute(db)
    teachertable.delete(*teachertable.get_children())
    fetched_data = cur.fetchall()
    total_record = cur.rowcount
    for i in fetched_data:
        teachertable.insert('', END, value=i)
    messagebox.showinfo('total record', total_record)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..........................
def update_teacher():
    def update_data():
        db = 'update teacher set name=%s, dob=%s, age=%s, gender=%s, qualification=%s, post=%s, ' \
             'mob_No=%s, subject=%s, experience=%s, Date=%s where id=%s'

        cur.execute(db,
                    (nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(), qfnentry.get(),
                     postentry.get(), Mobentry.get(), subjectentry.get(), experienceentry.get(), date, identry.get()))
        con.commit()
        messagebox.showinfo('Success', f'Id {identry.get()} is modified successfully', parent=updatewindow)
        updatewindow.destroy()
        show_teacher()

    updatewindow = Toplevel()
    updatewindow.title('UPDATE TEACHER')
    updatewindow.grab_set()
    updatewindow.resizable(False, False)

    idlabel = Label(updatewindow, text='ID', font=('arial', 20, ' italic bold'), fg='blue')
    idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    identry = Entry(updatewindow, font=('arial', 15, 'bold'))
    identry.grid(row=0, column=1, padx=10, pady=15)

    namelabel = Label(updatewindow, text='NAME', font=('arial', 20, ' italic bold'), fg='blue')
    namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    nameentry.grid(row=1, column=1, padx=10, pady=15)

    doblabel = Label(updatewindow, text='DOB', font=('arial', 20, ' italic bold'), fg='blue')
    doblabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    dobentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    dobentry.grid(row=2, column=1, padx=10, pady=15)

    agelabel = Label(updatewindow, text='AGE', font=('arial', 20, ' italic bold'), fg='blue')
    agelabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    ageentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    ageentry.grid(row=3, column=1, padx=10, pady=15)

    genderlabel = Label(updatewindow, text='GENDER', font=('arial', 20, ' italic bold'), fg='blue')
    genderlabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    genderentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    genderentry.grid(row=4, column=1, padx=10, pady=15)

    qfnlabel = Label(updatewindow, text='QUALIFICATION', font=('arial', 20, ' italic bold'), fg='blue')
    qfnlabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    qfnentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    qfnentry.grid(row=0, column=4, padx=10, pady=15)

    postlabel = Label(updatewindow, text='POST', font=('arial', 20, ' italic bold'), fg='blue')
    postlabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    postentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    postentry.grid(row=1, column=4, padx=10, pady=15)

    Moblabel = Label(updatewindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=2, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=2, column=4, padx=10, pady=15)

    subjectlabel = Label(updatewindow, text='SUBJECT', font=('arial', 20, ' italic bold'), fg='blue')
    subjectlabel.grid(row=3, column=3, padx=30, pady=15, sticky=W)
    subjectentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    subjectentry.grid(row=3, column=4, padx=10, pady=15)

    experiencelabel = Label(updatewindow, text='EXPERIENCE', font=('arial', 20, ' italic bold'), fg='blue')
    experiencelabel.grid(row=4, column=3, padx=30, pady=15, sticky=W)
    experienceentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    experienceentry.grid(row=4, column=4, padx=10, pady=15)

    updateteacherbutton = ttk.Button(updatewindow, text='UPDATE TEACHERS', command=update_data)
    updateteacherbutton.grid(row=5, columnspan=5, pady=15)

    index = teachertable.focus()
    content = teachertable.item(index)
    data = content['values']

    identry.insert(0, data[0])
    nameentry.insert(0, data[1])
    dobentry.insert(0, data[2])
    ageentry.insert(0, data[3])
    genderentry.insert(0, data[4])
    qfnentry.insert(0, data[5])
    postentry.insert(0, data[6])
    Mobentry.insert(0, data[7])
    subjectentry.insert(0, data[8])
    experienceentry.insert(0, data[9])


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>........................
def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    index = teachertable.get_children()
    newlist = []
    for i in index:
        content = teachertable.item(i)
        data = content['values']
        newlist.append(data)
    table = pandas.DataFrame(newlist,
                             columns=['ID', 'Name', 'DOB', 'Age', 'Gender', 'Qualification', 'Post',
                                      'Mobile No.', 'Subject', 'Experience', 'Date'])
    print(table)
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data saved successfully')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>........................
def exit_sms():
    res = messagebox.askyesno('Confirm', 'Do you want to exit')
    if res == True:
        root.destroy()
    else:
        pass


# gui#################################################################################################################################
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')
root.geometry('%dx%d' % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.title('SCHOOL MANAGEMENT SYSTEM')
root.resizable(False, False)

datelabel = Label(root, font=('times new roman', 18, 'bold'))
datelabel.place(x=5, y=5)
clock()
s = 'TEACHER MANAGEMENT SYSTEM'
sliderlabel = Label(root, font=('ALGERIAN', 25, 'italic bold'), fg='red', width=30)
sliderlabel.place(x=300, y=0)
slider()

connectbutton = ttk.Button(root, text='Connect Database', command=connect_database)
connectbutton.place(x=1000, y=0)

leftframe = Frame(root)
leftframe.place(x=50, y=80, width=300, height=550)

logoimage = PhotoImage(file='teacher.png')
logolabel = Label(leftframe, image=logoimage)
logolabel.grid(row=0, column=0)

addstubutton = ttk.Button(leftframe, text='Add Teacher', width=25, state=DISABLED, command=add_teacher)
addstubutton.grid(row=1, column=0, pady=5)

searchstubutton = ttk.Button(leftframe, text='Search Teacher', width=25, state=DISABLED, command=search_teacher)
searchstubutton.grid(row=2, column=0, pady=5)

deletestubutton = ttk.Button(leftframe, text='Delete Teacher', width=25, state=DISABLED, command=delete_teacher)
deletestubutton.grid(row=3, column=0, pady=5)

updatestubutton = ttk.Button(leftframe, text='Update Teacher', width=25, state=DISABLED, command=update_teacher)
updatestubutton.grid(row=4, column=0, pady=5)

showstubutton = ttk.Button(leftframe, text='Show Teacher', width=25, state=DISABLED, command=show_teacher)
showstubutton.grid(row=5, column=0, pady=5)

exportstubutton = ttk.Button(leftframe, text='Export Teacher', width=25, state=DISABLED, command=export_data)
exportstubutton.grid(row=6, column=0, pady=5)

exitbutton = ttk.Button(leftframe, text='EXIT', width=25, command=exit_sms)
exitbutton.grid(row=7, column=0, pady=5)

rightframe = Frame(root)
rightframe.place(x=350, y=80, width=820, height=550)

scrollbar1 = Scrollbar(rightframe, orient=HORIZONTAL)
scrollbar2 = Scrollbar(rightframe)

teachertable = ttk.Treeview(rightframe, columns=(
    'ID', 'Name', 'DOB', 'Age', 'Gender', 'Qualification', 'Post', 'Mobile No.', 'Subject', 'Experience', 'Date'),
                            xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set)

scrollbar1.config(command=teachertable.xview)
scrollbar2.config(command=teachertable.yview)

scrollbar1.pack(side=BOTTOM, fill=X)
scrollbar2.pack(side=RIGHT, fill=Y)

teachertable.pack(fill=BOTH, expand=2)

teachertable.heading('ID', text='ID')
teachertable.heading('Name', text='Name')
teachertable.heading('DOB', text='DOB')
teachertable.heading('Age', text='Age')
teachertable.heading('Gender', text='Gender')
teachertable.heading('Qualification', text='Qualification')
teachertable.heading('Post', text='Post')
teachertable.heading('Mobile No.', text='Mobile No.')
teachertable.heading('Subject', text='Subject')
teachertable.heading('Experience', text='Experience')
teachertable.heading('Date', text='Date')

teachertable.column('ID', width=200, anchor=CENTER)
teachertable.column('Name', width=200, anchor=CENTER)
teachertable.column('DOB', width=200, anchor=CENTER)
teachertable.column('Age', width=200, anchor=CENTER)
teachertable.column('Gender', width=200, anchor=CENTER)
teachertable.column('Qualification', width=200, anchor=CENTER)
teachertable.column('Post', width=200, anchor=CENTER)
teachertable.column('Mobile No.', width=200, anchor=CENTER)
teachertable.column('Subject', width=200, anchor=CENTER)
teachertable.column('Experience', width=200, anchor=CENTER)
teachertable.column('Date', width=200, anchor=CENTER)

style = ttk.Style()

style.configure('Treeview', rowheight=40, font=('times new roman', 15), foreground='purple', background='white',
                fieldbackground='white')
style.configure('Treeview.Heading', font=('times new roman', 15), foreground='Royal blue')
teachertable.config(show='headings')

root.mainloop()
