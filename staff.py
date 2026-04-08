from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
from tkinter import *
import time
import pymysql
import pandas


# functions

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
            db = "create table staff(ID int not null primary key,Name varchar(50),DOB varchar(50),Age int,Gender varchar(10),occupation varchar(30),Mobile_No char(10), Date varchar(50))"
            cur.execute(db)
        except:
            db = 'use schoolmanagementsystem'
            cur.execute(db)

        messagebox.showinfo('Success', 'Database Connection Is Successful', parent=connectroot)
        connectroot.destroy()
        addstaffbutton.config(state=NORMAL)
        searchstaffbutton.config(state=NORMAL)
        updatestaffbutton.config(state=NORMAL)
        showstaffbutton.config(state=NORMAL)
        exportstaffbutton.config(state=NORMAL)
        deletestaffbutton.config(state=NORMAL)

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
    passwordentry = Entry(connectroot, font=('arial', 15), fg='red', bd=3, show='*')
    passwordentry.grid(row=2, column=1, padx=40, pady=20)

    connectbutton = ttk.Button(connectroot, text='CONNECT', command=connect)
    connectbutton.grid(row=3, columnspan=3)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..............................
def add_staff():
    def add_data():
        if identry.get() == '' or nameentry.get() == '' or dobentry.get() == '' or ageentry.get() == '' or genderentry.get() == '' or occupationentry.get() == '' or Mobentry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=addwindow)
        else:
            try:
                db = 'insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s)'

                cur.execute(db, (identry.get(), nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(),
                                 occupationentry.get(), Mobentry.get(), date))
                con.commit()

                result = messagebox.askyesno('Success', 'Data saved successfully. Do you want to clear the form?',
                                             parent=addwindow)
                if result:
                    identry.delete(0, END)
                    nameentry.delete(0, END)
                    dobentry.delete(0, END)
                    ageentry.delete(0, END)
                    genderentry.delete(0, END)
                    occupationentry.delete(0, END)
                    Mobentry.delete(0, END)
                else:
                    pass

            except:
                messagebox.showerror('Error', 'Id cannot be repeated', parent=addwindow)
            db = "select * from staff"
            cur.execute(db)
            fetched_data = cur.fetchall()
            total_record = cur.rowcount
            stafftable.delete(*stafftable.get_children())
            for i in fetched_data:
                data = list(i)

                stafftable.insert('', END, values=data)
        addwindow.destroy()

    addwindow = Toplevel()
    addwindow.title('ADD STAFF DETAILS')
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

    occupationlabel = Label(addwindow, text='OCCUPATION', font=('arial', 20, ' italic bold'), fg='blue')
    occupationlabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    occupationentry = Entry(addwindow, font=('arial', 15, 'bold'))
    occupationentry.grid(row=0, column=4, padx=10, pady=15)

    Moblabel = Label(addwindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(addwindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=1, column=4, padx=10, pady=15)

    addstaffbutton = ttk.Button(addwindow, text='ADD STAFF', command=add_data)
    addstaffbutton.grid(row=5, columnspan=5, pady=15)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..........................................................

def search_staff():
    def search_data():
        db = 'select * from staff where id=%s or name=%s or dob=%s or age=%s or gender=%s or occupation=%s or Mobile_no =%s '
        cur.execute(db, (
            identry.get(), nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(), occupationentry.get(),
            Mobentry.get()))
        stafftable.delete(*stafftable.get_children())
        fetched_data = cur.fetchall()
        total_record = cur.rowcount
        for i in fetched_data:
            stafftable.insert('', END, value=i)
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

    occupationlabel = Label(searchwindow, text='OCCUPATION', font=('arial', 20, ' italic bold'), fg='blue')
    occupationlabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    occupationentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    occupationentry.grid(row=0, column=4, padx=10, pady=15)

    Moblabel = Label(searchwindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(searchwindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=1, column=4, padx=10, pady=15)

    addstaffbutton = ttk.Button(searchwindow, text='SEARCH STAFF', command=search_data)
    addstaffbutton.grid(row=5, columnspan=5, pady=15)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..................................

def delete_staff():
    index = stafftable.focus()
    content = stafftable.item(index)
    content_id = content['values'][0]
    db = 'delete from staff where id=%s'
    cur.execute(db, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'This {content_id} is deleted  succefully')
    show_staff()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>......................
def show_staff():
    db = 'select * from staff'
    cur.execute(db)
    stafftable.delete(*stafftable.get_children())
    fetched_data = cur.fetchall()
    total_record = cur.rowcount
    for i in fetched_data:
        stafftable.insert('', END, value=i)
    messagebox.showinfo('total record', total_record)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..........................
def update_staff():
    def updatedata():
        db = 'update staff set name=%s,dob=%s,age=%s,gender=%s,occupation=%s,Mobile_No=%s where id=%s'
        cur.execute(db, (
            nameentry.get(), dobentry.get(), ageentry.get(), genderentry.get(), occupationentry.get(),
            Mobentry.get(), identry.get()))
        con.commit()
        messagebox.showinfo('Success', f'Id {identry.get()} is modified successfully', parent=updatewindow)
        updatewindow.destroy()
        show_staff()

    updatewindow = Toplevel()
    updatewindow.title('UPDATE STAFF')
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

    occupationlabel = Label(updatewindow, text='OCCUPATION', font=('arial', 20, ' italic bold'), fg='blue')
    occupationlabel.grid(row=0, column=3, padx=30, pady=15, sticky=W)
    occupationentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    occupationentry.grid(row=0, column=4, padx=10, pady=15)

    Moblabel = Label(updatewindow, text='MOBILE NO.', font=('arial', 20, ' italic bold'), fg='blue')
    Moblabel.grid(row=1, column=3, padx=30, pady=15, sticky=W)
    Mobentry = Entry(updatewindow, font=('arial', 15, 'bold'))
    Mobentry.grid(row=1, column=4, padx=10, pady=15)

    updatestaffbutton = ttk.Button(updatewindow, text='UPDATE STAFF', command=updatedata)
    updatestaffbutton.grid(row=5, columnspan=5, pady=15)

    index = stafftable.focus()
    content = stafftable.item(index)
    data = content['values']
    identry.insert(0, data[0])
    nameentry.insert(0, data[1])
    dobentry.insert(0, data[2])
    ageentry.insert(0, data[3])
    genderentry.insert(0, data[4])
    occupationentry.insert(0, data[5])
    Mobentry.insert(0, data[6])


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>........................
def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    index = stafftable.get_children()
    newlist = []
    for i in index:
        content = stafftable.item(i)
        data = content['values']
        newlist.append(data)
    table = pandas.DataFrame(newlist,
                             columns=['ID', 'Name', 'DOB', 'Age', 'Gender', 'occupation',
                                      'Mobile No.'])
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
root.geometry('1200x700+0+0')
root.title('SCHOOL MANAGEMENT SYSTEM')
root.resizable(False, False)

datelabel = Label(root, font=('times new roman', 18, 'bold'))
datelabel.place(x=5, y=5)
clock()
s = 'STAFF MANAGEMENT SYSTEM'
sliderlabel = Label(root, font=('ALGERIAN', 25, 'italic bold'), fg='red', width=30)
sliderlabel.place(x=300, y=0)
slider()

connectbutton = ttk.Button(root, text='Connect Database', command=connect_database)
connectbutton.place(x=1000, y=0)

leftframe = Frame(root)
leftframe.place(x=50, y=80, width=300, height=550)

logoimage = PhotoImage(file='staff_image.png')
logolabel = Label(leftframe, image=logoimage)
logolabel.grid(row=0, column=0)

addstaffbutton = ttk.Button(leftframe, text='Add Staff', width=25, state=DISABLED, command=add_staff)
addstaffbutton.grid(row=1, column=0, pady=5)

searchstaffbutton = ttk.Button(leftframe, text='Search Staff', width=25, state=DISABLED, command=search_staff)
searchstaffbutton.grid(row=2, column=0, pady=5)

deletestaffbutton = ttk.Button(leftframe, text='Delete Staff', width=25, state=DISABLED, command=delete_staff)
deletestaffbutton.grid(row=3, column=0, pady=5)

updatestaffbutton = ttk.Button(leftframe, text='Update Staff', width=25, state=DISABLED, command=update_staff)
updatestaffbutton.grid(row=4, column=0, pady=5)

showstaffbutton = ttk.Button(leftframe, text='Show Staff', width=25, state=DISABLED, command=show_staff)
showstaffbutton.grid(row=5, column=0, pady=5)

exportstaffbutton = ttk.Button(leftframe, text='Export Staff', width=25, state=DISABLED, command=export_data)
exportstaffbutton.grid(row=6, column=0, pady=5)

exitbutton = ttk.Button(leftframe, text='EXIT', width=25, command=exit_sms)
exitbutton.grid(row=7, column=0, pady=5)

rightframe = Frame(root)
rightframe.place(x=350, y=80, width=820, height=550)

scrollbar1 = Scrollbar(rightframe, orient=HORIZONTAL)
scrollbar2 = Scrollbar(rightframe)

stafftable = ttk.Treeview(rightframe, columns=(
    'ID', 'Name', 'DOB', 'Age', 'Gender', 'occupation', 'Mobile No.'),
                          xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar2.set)

scrollbar1.config(command=stafftable.xview)
scrollbar2.config(command=stafftable.yview)

scrollbar1.pack(side=BOTTOM, fill=X)
scrollbar2.pack(side=RIGHT, fill=Y)

stafftable.pack(fill=BOTH, expand=2)

stafftable.heading('ID', text='ID')
stafftable.heading('Name', text='Name')
stafftable.heading('DOB', text='DOB')
stafftable.heading('Age', text='Age')
stafftable.heading('Gender', text='Gender')
stafftable.heading('occupation', text='occupation')
stafftable.heading('Mobile No.', text='Mobile No.')

stafftable.column('ID', width=200, anchor=CENTER)
stafftable.column('Name', width=200, anchor=CENTER)
stafftable.column('DOB', width=200, anchor=CENTER)
stafftable.column('Age', width=200, anchor=CENTER)
stafftable.column('Gender', width=200, anchor=CENTER)
stafftable.column('occupation', width=200, anchor=CENTER)
stafftable.column('Mobile No.', width=200, anchor=CENTER)

style = ttk.Style()

style.configure('Treeview', rowheight=40, font=('times new roman', 15), foreground='purple', background='white',
                fieldbackground='white')
style.configure('Treeview.Heading', font=('times new roman', 15), foreground='Royal blue')
stafftable.config(show='headings')

root.mainloop()
