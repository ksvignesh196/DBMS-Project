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
            db = "create table student(ID int not null primary key,Name varchar(50),DOB varchar(50),Age int,Gender varchar(10),Father_Name varchar(50),Mother_Name varchar(50),Mobile_No varchar(10)," \
                 "Address varchar(200),Email varchar(50),Date varchar(50))"
            cur.execute(db)
        except:
            db = 'use schoolmanagementsystem'
            cur.execute(db)
        messagebox.showinfo('Success', 'Database Connection Is Successful', parent=connectroot)
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

    hostname = Label(connectroot, text='HOST NAME', font=('arial', 18, 'italic bold'), fg='blue')
    hostname.grid(row=0, column=0, padx=20)

    hostentry = Entry(connectroot, font=('arial', 15), fg='red', bd=3)
    hostentry.grid(row=0, column=1, padx=40, pady=20)

    username = Label(connectroot, text='USER NAME', font=('arial', 18, 'italic bold'), fg='blue')
    username.grid(row=1, column=0, padx=20)

    userentry = Entry(connectroot, font=('arial', 15), fg='red', bd=3)
    userentry.grid(row=1, column=1, padx=40, pady=20)

    password = Label(connectroot, text='PASSWORD', font=('arial', 18, 'italic bold'), fg='blue')
    password.grid(row=2, column=0, padx=20)

    passwordentry = Entry(connectroot, font=('arial', 15), fg='red', bd=3)
    passwordentry.grid(row=2, column=1, padx=40, pady=20)

    connectbutton = ttk.Button(connectroot, text='CONNECT', command=connect)
    connectbutton.grid(row=3, columnspan=3)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..............................
def add_student():
    def add_data():
        if identry.get() == '' or nameentry.get() == '' or dobentry.get() == '' or ageentry.get() == '' or genderentry.get() == '' or Fnameentry.get() == '' or Mnameentry.get() == '' or Mobentry.get() == '' \
                or Addressentry.get() == '' or emailentry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=addwindow)
        else:
            try:
                db = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

                cur.execute(db, (
                identry.get(), nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(), Fnameentry.get(),
                Mnameentry.get(), Mobentry.get(), Addressentry.get(), emailentry.get(), date))
                con.commit()

                result = messagebox.askyesno('Success', 'Data saved successfully. Do you want to clear the form',
                                             parent=addwindow)
                if result:
                    identry.delete(0, END)
                    nameentry.delete(0, END)
                    dobentry.delete(0, END)
                    ageentry.delete(0, END)
                    genderentry.delete(0, END)
                    Fnameentry.delete(0, END)
                    Mnameentry.delete(0, END)
                    Mobentry.delete(0, END)
                    Addressentry.delete(0, END)
                    emailentry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'Id cannot be repeated', parent=addwindow)
            db = "select * from student"
            cur.execute(db)
            fetched_data = cur.fetchall()
            total_record = cur.rowcount
            studenttable.delete(*studenttable.get_children())
            for i in fetched_data:
                data = list(i)

                studenttable.insert('', END, values=data)
        addwindow.destroy()

    addwindow = Toplevel()
    addwindow.title('ADD STUDENT DETAILS')
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

    Fnamelabel = Label(addwindow, text='FATHER NAME', font=('arial', 20, ' italic bold'), fg='blue')
    Fnamelabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    Fnameentry = Entry(addwindow, font=('arial', 15, 'bold'))
    Fnameentry.grid(row=0, column=4, padx=10, pady=15)

    Mnamelabel = Label(addwindow, text='MOTHER NAME', font=('arial', 20, ' italic bold'), fg='blue')
    Mnamelabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    Mnameentry = Entry(addwindow, font=('arial', 15, 'bold'))
    Mnameentry.grid(row=1, column=4, padx=10, pady=15)

    Moblabel = Label(addwindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=2, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(addwindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=2, column=4, padx=10, pady=15)

    Addresslabel = Label(addwindow, text='ADDRESS', font=('arial', 20, ' italic bold'), fg='blue')
    Addresslabel.grid(row=3, column=3, padx=30, pady=15, sticky=W)
    Addressentry = Entry(addwindow, font=('arial', 15, 'bold'))
    Addressentry.grid(row=3, column=4, padx=10, pady=15)

    emaillabel = Label(addwindow, text='EMAIL', font=('arial', 20, ' italic bold'), fg='blue')
    emaillabel.grid(row=4, column=3, padx=30, pady=15, sticky=W)
    emailentry = Entry(addwindow, font=('arial', 15, 'bold'))
    emailentry.grid(row=4, column=4, padx=10, pady=15)

    addstudentbutton = ttk.Button(addwindow, text='ADD STUDENT', command=add_data)
    addstudentbutton.grid(row=5, columnspan=5, pady=15)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..........................................................

def search_student():
    def search_data():
        db = 'select * from student where id=%s or name=%s or dob=%s or age=%s or gender=%s or Father_name=%s or Mother_name=%s or Mobile_no =%s or address=%s or email=%s'
        cur.execute(db, (
        identry.get(), nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(), Fnameentry.get(),
        Mnameentry.get(), Mobentry.get(), Addressentry.get(), emailentry.get()))
        studenttable.delete(*studenttable.get_children())
        fetched_data = cur.fetchall()
        total_record = cur.rowcount
        for i in fetched_data:
            studenttable.insert('', END, value=i)
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

    Fnamelabel = Label(searchwindow, text='FATHER NAME', font=('arial', 20, ' italic bold'), fg='blue')
    Fnamelabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    Fnameentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    Fnameentry.grid(row=0, column=4, padx=10, pady=15)

    Mnamelabel = Label(searchwindow, text='MOTHER NAME', font=('arial', 20, ' italic bold'), fg='blue')
    Mnamelabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    Mnameentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    Mnameentry.grid(row=1, column=4, padx=10, pady=15)

    Moblabel = Label(searchwindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=2, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=2, column=4, padx=10, pady=15)

    Addresslabel = Label(searchwindow, text='ADDRESS', font=('arial', 20, ' italic bold'), fg='blue')
    Addresslabel.grid(row=3, column=3, padx=30, pady=15, sticky=W)
    Addressentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    Addressentry.grid(row=3, column=4, padx=10, pady=15)

    emaillabel = Label(searchwindow, text='EMAIL', font=('arial', 20, ' italic bold'), fg='blue')
    emaillabel.grid(row=4, column=3, padx=30, pady=15, sticky=W)
    emailentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    emailentry.grid(row=4, column=4, padx=10, pady=15)

    addstudentbutton = ttk.Button(searchwindow, text='SEARCH STUDENT', command=search_data)
    addstudentbutton.grid(row=5, columnspan=5, pady=15)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..................................

def delete_student():
    index = studenttable.focus()
    content = studenttable.item(index)
    content_id = content['values'][0]
    db = 'delete from student where id=%s'
    cur.execute(db, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'This {content_id} is deleted  succefully')
    show_student()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>......................
def show_student():
    db = 'select * from student'
    cur.execute(db)
    studenttable.delete(*studenttable.get_children())
    fetched_data = cur.fetchall()
    total_record = cur.rowcount
    for i in fetched_data:
        studenttable.insert('', END, value=i)
    messagebox.showinfo('total record', total_record)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..........................
def update_student():
    def updatedata():
        db = 'update student set name=%s,dob=%s,age=%s,gender=%s,Father_Name=%s,Mother_Name=%s,Mobile_No=%s,Address=%s,Email=%s,Date=%s where id=%s'
        cur.execute(db, (
        nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(), Fnameentry.get(), Mnameentry.get(),
        Mobentry.get(), Addressentry.get(), emailentry.get(), date, identry.get()))
        con.commit()
        messagebox.showinfo('Success', f'Id {identry.get()} is modified successfully', parent=updatewindow)
        updatewindow.destroy()
        show_student()

    updatewindow = Toplevel()
    updatewindow.title('UPDATE STUDENT')
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

    Fnamelabel = Label(updatewindow, text='FATHER NAME', font=('arial', 20, ' italic bold'), fg='blue')
    Fnamelabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    Fnameentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    Fnameentry.grid(row=0, column=4, padx=10, pady=15)

    Mnamelabel = Label(updatewindow, text='MOTHER NAME', font=('arial', 20, ' italic bold'), fg='blue')
    Mnamelabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    Mnameentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    Mnameentry.grid(row=1, column=4, padx=10, pady=15)

    Moblabel = Label(updatewindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=2, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=2, column=4, padx=10, pady=15)

    Addresslabel = Label(updatewindow, text='ADDRESS', font=('arial', 20, ' italic bold'), fg='blue')
    Addresslabel.grid(row=3, column=3, padx=30, pady=15, sticky=W)
    Addressentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    Addressentry.grid(row=3, column=4, padx=10, pady=15)

    emaillabel = Label(updatewindow, text='EMAIL', font=('arial', 20, ' italic bold'), fg='blue')
    emaillabel.grid(row=4, column=3, padx=30, pady=15, sticky=W)
    emailentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    emailentry.grid(row=4, column=4, padx=10, pady=15)

    updatestudentbutton = ttk.Button(updatewindow, text='UPDATE STUDENT', command=updatedata)
    updatestudentbutton.grid(row=5, columnspan=5, pady=15)

    index = studenttable.focus()
    content = studenttable.item(index)
    data = content['values']
    identry.insert(0, data[0])
    nameentry.insert(0, data[1])
    dobentry.insert(0, data[2])
    ageentry.insert(0, data[3])
    genderentry.insert(0, data[4])
    Fnameentry.insert(0, data[5])
    Mnameentry.insert(0, data[6])
    Mobentry.insert(0, data[7])
    Addressentry.insert(0, data[8])
    emailentry.insert(0, data[9])


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>........................
def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    index = studenttable.get_children()
    newlist = []
    for i in index:
        content = studenttable.item(i)
        data = content['values']
        newlist.append(data)
    table = pandas.DataFrame(newlist,
                             columns=['Admission No.', 'Name', 'DOB', 'Age', 'Gender', 'Father Name', 'Mother Name',
                                      'Mobile No.', 'Address', 'Email', 'Date'])
    print(table)
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data saved successfully')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>........................
def exit_sms():
    res = messagebox.askyesno('Confirm', 'Do you want to EXIT!!! ')
    if res == True:
        root.destroy()
    else:
        pass


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...................


# gui###############################################################################################################################
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

connectbutton = ttk.Button(root, text='Connect Database', command=connect_database)
connectbutton.place(x=1000, y=0)

leftframe = Frame(root)
leftframe.place(x=50, y=80, width=300, height=550)

logoimage = PhotoImage(file='students.png')
logolabel = Label(leftframe, image=logoimage)
logolabel.grid(row=0, column=0)

addstubutton = ttk.Button(leftframe, text='Add Student', width=25, state=DISABLED, command=add_student)
addstubutton.grid(row=1, column=0, pady=10)

searchstubutton = ttk.Button(leftframe, text='Search Student', width=25, state=DISABLED, command=search_student)
searchstubutton.grid(row=2, column=0, pady=10)

deletestubutton = ttk.Button(leftframe, text='Delete Student', width=25, state=DISABLED, command=delete_student)
deletestubutton.grid(row=3, column=0, pady=10)

updatestubutton = ttk.Button(leftframe, text='Update Student', width=25, state=DISABLED, command=update_student)
updatestubutton.grid(row=4, column=0, pady=10)

showstubutton = ttk.Button(leftframe, text='Show Student', width=25, state=DISABLED, command=show_student)
showstubutton.grid(row=5, column=0, pady=10)

exportstubutton = ttk.Button(leftframe, text='Export Student', width=25, state=DISABLED, command=export_data)
exportstubutton.grid(row=6, column=0, pady=10)

exitbutton = ttk.Button(leftframe, text='EXIT', width=25, command=exit_sms)
exitbutton.grid(row=8, column=0, pady=10)

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
