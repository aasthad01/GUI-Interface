from tkinter import *
from PIL import ImageTk
from tkcalendar import *
from tkinter import messagebox
import mysql.connector

windows=Tk()
windows.title("Student Registration Form")
windows.geometry('700x750+200+10')
windows.resizable(0,0)
backgroundimage=ImageTk.PhotoImage(file='p1.jpg')
bglabel=Label(windows, image=backgroundimage)
bglabel.place(x=0, y=0)

enrollment=StringVar()
rollno=StringVar()
firstname=StringVar()
middlename=StringVar()
lastname=StringVar()
dob=StringVar()
age=IntVar()
gender=StringVar()
contact=StringVar()
email=StringVar()
course=StringVar()
OM=StringVar()

course=['MBA-MS(5 Yrs.)','MBA-TA(5 Yrs.)','MCA(5 Yrs.)','MTECH(5 Yrs)','BCOM(Hons.)(3 Yrs.)','MBA-APR(2 Yrs.)','MBA-ESHIP(2 Yrs)','MBA-MS(2 Yrs.)','MBA-TA(2 Yrs.)']
OM.set('Select Course')

def pick_date(event):
    global cal, date_window
    date_window=Toplevel()
    date_window.grab_set()
    date_window.title("Choose your Date of Birth")
    date_window.geometry('250x220+590+370')
    cal=Calendar(date_window, selectmode="day", date_pattern="y/mm/dd")
    cal.place(x=0, y=0)

    submitbtn=Button(date_window, text="Submit", command=grab_date)
    submitbtn.place(x=80, y=190)

def grab_date():
    dobEntry.delete(0, END)
    dobEntry.insert(0, cal.get_date())
    date_window.destroy()

def clear():
    enrollmentEntry.delete(3, END)
    rollnoEntry.delete(5, END)  
    firstnameEntry.delete(0, END) 
    middlenameEntry.delete(0, END) 
    lastnameEntry.delete(0, END) 
    dobEntry.delete(0, END) 
    ageEntry.delete(0, END) 
    gender.set(0)
    contactEntry.delete(0, END) 
    emailEntry.delete(0, END)  
    OM.set('Select Course')



def checkenroll(enroll):
    if enroll.isalnum() or enroll=='':
        return True
    else:
        messagebox.showwarning("invalid","Not Allowed ")
        return False  

def checkroll(roll):
    if roll.isalnum() or roll=='':
        return True
    else:
        messagebox.showwarning("invalid","Not Allowed ")                
        return False
 
def checkfname(fname):
    if fname.isalpha() or fname=='':
        return True
    else:
        messagebox.showwarning("invalid","Not Allowed ") 
        return False  

def checkmname(mname):
    if mname.isalpha() or mname=='':
       return True
    else:
        messagebox.showwarning("invalid","Not Allowed ")  
        return False
 
def checklname(lname):
    if lname.isalpha() or lname=='':
        return True
    else:
        messagebox.showwarning("invalid","Not Allowed ")  
        return False         

def checkagee(agee):
    if agee.isdigit() or agee=='':
       return TRUE
    else:
       messagebox.showwarning("invalid","Not Allowed ")    
       return False
       

def checkcont(cont):
    if cont.isdigit() or len(cont)==0:
       return True
    else:
       messagebox.showwarning("Invalid","Not Allowed ") 
       return False
        
def save():
    if enrollmentEntry.get()=='' or len(enrollmentEntry.get())!=9:
        messagebox.showerror('Alert!', 'Please enter valid enrollment number')
    elif rollnoEntry.get()=='' or len(rollnoEntry.get())!=8:
        messagebox.showerror('Alert!', 'Please enter valid roll number')
    elif firstnameEntry.get()=='':
        messagebox.showerror('Alert!', 'Please enter your first name')    
    elif lastnameEntry.get()=='':
        messagebox.showerror('Alert!', 'Please enter your last name')
    elif dobEntry.get()=='':
        messagebox.showerror('Alert!', 'Please enter your date of birth')
    elif ageEntry.get()=='' or len(ageEntry.get())>2:
        messagebox.showerror('Alert!', 'Please enter valid age')  
    elif gender.get()=="0":
        messagebox.showerror('Alert!', 'Please select your gender')         
    elif contactEntry.get()=='' or len(contactEntry.get())!=10:
        messagebox.showerror('Alert!', 'Please enter valid contact number') 
    elif emailEntry.get()=='':
        messagebox.showerror('Alert!', 'Please enter your email')    
    elif OM.get()=='' or OM.get()=="Select Course":
        messagebox.showerror('Alert!', 'Please select your course') 

    else:
        mydb = mysql.connector.connect (host="localhost", user="root", password="iw2baactor", database="Student_form")
        cur= mydb.cursor()

        try:
            query='create database Student_form'
            cur.execute(query)
            query='use Student_form' 
            cur.execute(query)
           # messagebox.showinfo('Success','Successfull connection')
         
            query='create table Student(Enrollment_no varchar(20) primary key not null, Roll_no varchar(10) not null unique, First_name char(50) not null, Middle_name char(50), Last_name char(50) not null, Birthdate date not null, Age int not null, Gender char(10) not null, Contact int not null unique, Email varchar(50) not null unique, Course varchar(30) not null)'
            cur.execute(query)
            messagebox.showinfo('Success','Table created')

        except:
            cur.execute('use Student_form')
            query='insert into student(Enrollment_no, Roll_no, First_name, Middle_name, Last_name, Birthdate, Age, Gender, Contact, Email, Course) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cur.execute(query,(enrollmentEntry.get(), rollnoEntry.get(), firstnameEntry.get(), middlenameEntry.get(), lastnameEntry.get(), dobEntry.get(), ageEntry.get(), gender.get(), contactEntry.get(), emailEntry.get(), OM.get()))
            mydb.commit() 
            mydb.close()
            messagebox.showinfo('Success', 'Submitted')
       
                     
frame=Frame(windows, width=500, height=600, bd=8, bg='#eaeafa')
frame.place(x=100, y=100)

heading=Label(windows, text='Student Registration Form', font=('Calibre', 20, 'bold', 'underline'), bg='#eaeafa')
heading.place(x=170, y=10)

enrollment=Label(frame, text='Enrollment No.:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
enrollment.place(x=10, y=10)
enrollmentEntry=Entry(frame, width=40, borderwidth=2)
enrollmentEntry.place(x=200, y=10)
#enrollmentEntry.insert(0, 'DE')
validate_enroll=windows.register(checkenroll)
enrollmentEntry.config(validate="key", validatecommand=(validate_enroll, "%P"))

rollno=Label(frame, text='Roll No.:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
rollno.place(x=10, y=50)
rollnoEntry=Entry(frame, width=40, borderwidth=2)
rollnoEntry.place(x=200, y=50)
#rollnoEntry.insert(0, 'IT2K')
validate_roll=windows.register(checkroll)
rollnoEntry.config(validate="key", validatecommand=(validate_roll, "%P"))

firstname=Label(frame, text='First Name:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
firstname.place(x=10, y=90)
firstnameEntry=Entry(frame, width=40, borderwidth=2)
firstnameEntry.place(x=200, y=90)
validate_fname=windows.register(checkfname)
firstnameEntry.config(validate="key", validatecommand=(validate_fname, "%P"))

middlename=Label(frame, text='Middle Name:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
middlename.place(x=10, y=130)
middlenameEntry=Entry(frame, width=40, borderwidth=2)
middlenameEntry.place(x=200, y=130)
validate_mname=windows.register(checkmname)
middlenameEntry.config(validate="key", validatecommand=(validate_mname, "%P"))

lastname=Label(frame, text='Last Name:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
lastname.place(x=10, y=170)
lastnameEntry=Entry(frame, width=40, borderwidth=2)
lastnameEntry.place(x=200, y=170)
validate_lname=windows.register(checklname)
lastnameEntry.config(validate="key", validatecommand=(validate_lname, "%P"))

dob=Label(frame, text='Date of Birth:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
dob.place(x=10, y=210)
dobEntry=Entry(frame, width=40, borderwidth=2)
dobEntry.place(x=200, y=210)
dobEntry.bind("<1>", pick_date)

age=Label(frame, text='Age:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
age.place(x=10, y=250)
ageEntry=Entry(frame, width=40, borderwidth=2)
ageEntry.place(x=200, y=250)
validate_agee=windows.register(checkagee)
ageEntry.config(validate="key", validatecommand=(validate_agee, "%P"))

gen=Label(frame, text='Gender:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
gen.place(x=10, y=290)

gender.set(0)
genderRadio1=Radiobutton(frame, text='Male', variable=gender, value='Male',  font='Tahoma 13 bold', bg='#eaeafa')
genderRadio1.place(x=200, y=290)
genderRadio2=Radiobutton(frame, text='Female', variable=gender, value='Female',  font='Tahoma 13 bold', bg='#eaeafa')
genderRadio2.place(x=200, y=320)
genderRadio3=Radiobutton(frame, text='Other', variable=gender, value='Other',  font='Tahoma 13 bold', bg='#eaeafa')
genderRadio3.place(x=200, y=350)

con=Label(frame, text='Contact:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
con.place(x=10, y=390)
contactEntry=Entry(frame, width=40, borderwidth=2,)
contactEntry.place(x=200, y=390)
validate_cont=windows.register(checkcont)
contactEntry.config(validate="key", validatecommand=(validate_cont, "%P"))

email=Label(frame, text='Email:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
email.place(x=10, y=430)
emailEntry=Entry(frame, width=40, borderwidth=2)
emailEntry.place(x=200, y=430)

courseLabelDropdown=Label(frame, text='Course:', font=('Calibre', 15, 'bold'), bg='#eaeafa')
courseLabelDropdown.place(x=10, y=470)
courseLabelDropdown=OptionMenu(frame, OM, *course)
courseLabelDropdown.place(x=200, y=470)
courseLabelDropdown.config(width=18, font=('calibre', 13, 'bold'), fg='black')

savebtn=Button(frame, text='Save', width=8, borderwidth=5, height=1, font=('calibre', 13, 'bold'), cursor='hand2', command=save)
savebtn.place(x=100, y=545)

clearbtn=Button(frame, text='Clear', width=8, borderwidth=5, height=1, font=('calibre', 13, 'bold'), cursor='hand2', command=clear)
clearbtn.place(x=250, y=545)

windows.mainloop()