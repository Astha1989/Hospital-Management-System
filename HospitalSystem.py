import tkinter.messagebox
from tkinter import  *
import mysql.connector as sqlcon
import random as rd

print ("TRY Connection ")
con=sqlcon.connect(host="localhost",user="root",password="abcd1234")#connection to mysql 
##con=sqlcon.connect(host="localhost",user="root")#connection to mysql 
cur=con.cursor()
cur = con.cursor(buffered=True)
if (con):
    # Carry out normal procedure
    print ("Connection successful")
else:
    print ("Connection unsuccessful")
cur.execute("create database if not exists Hospital2")
cur.execute("use Hospital2")
cur.execute("create table if not exists appointment"
            "("
            "idno varchar(12) primary key,"
            "name char(50),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")
cur.execute("create table if not exists appointment_details"
            "("
            "idno varchar(12) primary key,"
            "doctor varchar(50),"
            "date varchar(20),"
            "time varchar(20),"
            "appointment_no varchar(10))")

#  Message for registration
def entry():
    global e1,e2,e3,e4,e5,e6
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()

    query='insert into appointment values("{}", "{}", "{}", "{}", "{}", "{}")'.format(p1,p2,p3,p4,p5,p6)
    con.commit()
    cur.execute(query)
    
        
    
    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED AT KIS HOSPITAL")

#  For registration 
def register():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    label=Label(root1,text="REGISTER YOURSELF",font='arial 25 bold')
    label.pack()
    frame=Frame(root1,height=500,width=500)
    frame.pack()
    l1=Label(root1,text="AADHAR CARD NO.")
    l1.place(x=10,y=130)
    e1=tkinter.Entry(root1)
    e1.place(x=150,y=130)
    l2=Label(root1,text="NAME")
    l2.place(x=10,y=170)
    e2=tkinter.Entry(root1)
    e2.place(x=150,y=170)
    l3=Label(root1,text="AGE")
    l3.place(x=10,y=210)
    e3=tkinter.Entry(root1)
    e3.place(x=150,y=210)
    l4=Label(root1,text="GENDER M F")
    l4.place(x=10,y=250)
    e4=tkinter.Entry(root1)
    e4.place(x=150,y=250)
    l5=Label(root1,text="PHONE")
    l5.place(x=10,y=290)
    e5=tkinter.Entry(root1)
    e5.place(x=150,y=290)
    l6=Label(root1,text="BLOOD GROUP")
    l6.place(x=10,y=330)
    e6=tkinter.Entry(root1)
    e6.place(x=150,y=330)
    b1=Button(root1,text="SUBMIT",command=entry,)
    b1.place(x=150,y=370)
    
    
    root.resizable(False,False)
    root1.mainloop()

#  Message for appointment
def apo_details():
    global x1,x2,p1,p2,p3,o,x4,x3
    p1=x2.get()
    p2=x3.get()
    p3=x4.get()
    if int(p1)==1:

        j=("Dr. Verma \nRoom no:- 10")
        #h=rd.choice(j) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)
        det=("Your appointment is fixed with",j,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)

        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,j,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)

     
    elif int(p1)==2:
        i=("Dr. Kumar \nRoom no. 11")
        #h=rd.choice(i) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",i,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,i,p2,p3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
        
    elif int(p1)==3:
        j=("Dr. singh \nRoom no. 12")
        #h=rd.choice(j) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",j,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,j,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
    elif int(p1)==4:
        j=("Dr. Khan \nRoom no. 13")
        #h=rd.choice(j) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",j,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,j,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
        
    else:
        tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER VALID VALUE')

#  For appointment
def get_apoint():
    global x1,x2,x3,x4
    p1=x1.get()  
    cur.execute('select * from appointment where idno=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root3=Tk()
        label=Label(root3,text="APPOINTMENT",font='arial 25 bold')
        label.pack()
        frame=Frame(root3,height=500,width=600)
        frame.pack()
        if i[3]=='M' or i[3]=='m':
                x="Mr."
                name2=Label(root3,text=i[1])
                name2.place(x=140,y=80)
        else:
                x="Mrs Ms."
                name2=Label(root3,text=i[1])
                name2.place(x=170,y=80)
        for i in dat:
            name=Label(root3,text='WELCOME')
            name.place(x=50,y=80)
            name1=Label(root3,text=x)
            name1.place(x=120,y=80)
            age=Label(root3,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root3,text=i[2])
            age1.place(x=100,y=100)
            phone=Label(root3,text='PHONE:-')
            phone.place(x=50,y=120)
            phone1=Label(root3,text=i[4])
            phone1.place(x=100,y=120)
            bg=Label(root3,text='BLOOD GROUP:-')
            bg.place(x=50,y=140)
            bg1=Label(root3,text=i[5])
            bg1.place(x=150,y=140)


        L=Label(root3,text='DEPARTMENTS')
        L.place(x=50,y=220)
        L1=Label(root3,text="1.Orthopaedic surgeon ")
        L1.place(x=50,y=250)
        L2=Label(root3,text='2.Physician')
        L2.place(x=50,y=270)
        L3=Label(root3,text='3.Nephrologist')
        L3.place(x=50,y=290)
        L4=Label(root3,text='4.Neurologist')
        L4.place(x=50,y=310)
        L7=Label(root3,text='Enter your choice')
        L7.place(x=100,y=370)
        x2=tkinter.Entry(root3)
        x2.place(x=200,y=370)
        
        L7=Label(root3,text=('enter date')).place(x=100,y=400)
        x3=tkinter.Entry(root3)
        x3.place(x=200,y=400)

        L8=Label(root3,text=('enter time in 24 hour format')).place(x=48,y=430)
        x4=tkinter.Entry(root3)
        x4.place(x=200,y=430)
        
        B1=Button(root3,text='Submit',command=apo_details)
        B1.place(x=120,y=480)   
        root3.resizable(False,False)
        root3.mainloop()



#  For AADHAAR no input
def apoint():
    global x1
    root2=Tk()
    label=Label(root2,text="APPOINTMENT",font='arial 25 bold')
    label.pack()
    frame=Frame(root2,height=250,width=400)
    frame.pack()
    l1=Label(root2,text="AADHAAR NO.")
    l1.place(x=10,y=130)
    x1=tkinter.Entry(root2)
    x1.place(x=150,y=130)
    b1=Button(root2,text='Submit',command=get_apoint)
    b1.place(x=150,y=160)
    root2.resizable(False,False)
    root2.mainloop()
    
#  List of doctors
def lst_doc():
    root4=Tk()
    
    l=["Dr. Kumar","Dr. Khan","Dr. Singh","Dr. Verma",]
    ll = l
    m=["Orthopaedic surgeon","Nephrologist","Physician","Neurologist"]
    n=[10,11,12,13]

    frame=Frame(root4,height=500,width=500)
    frame.pack()
    
    
    l1=Label(root4,text='NAME OF DOCTORS') 
    l1.place(x=20,y=10)
    count=20
    for i in l:
       count=count+20
       l=Label(root4,text=i)
       l.place(x=20,y=count)

    l2=Label(root4,text='DEPARTMENT')
    l2.place(x=180,y=10)
    count1=20
    for i in m:
       count1=count1+20
       l3=Label(root4,text=i)
       l3.place(x=180,y=count1)

    l4=Label(root4,text='ROOM NO')
    l4.place(x=350,y=10)
    count2=20
    for i in n:
       count2=count2+20
       l5=Label(root4,text=i)
       l5.place(x=350,y=count2)
       
    root.resizable(False,False)
    root4.mainloop()

def ser_avail():
    
    root5=Tk()
    frame=Frame(root5,height=500,width=500)
    frame.pack()
    l1=Label(root5,text='SERVICES AVAILABLE')
    l1.place(x=20,y=10)
    f=["ULTRASOUND","X-RAY","CT Scan","BLOOD COLLECTION","DIALYSIS","ECG","CHEMIST","LAB"]
    count1=20
    for i in f:
       count1=count1+20
       l3=Label(root5,text=i)
       l3.place(x=20,y=count1)
    l2=Label(root5,text='ROOM NO.')
    l2.place(x=200,y=10)
    g=[1,2,3,4,5,6,7,8]
    count2=20
    for i in g:
       count2=count2+20
       l4=Label(root5,text=i)
       l4.place(x=200,y=count2)
    root5.resizable(False,False)
    root5.mainloop()
   

def search_data():
    global x3,ad
    root7=Tk()
    label=Label(root7,text="APPOINTMENT DETAILS",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=500,width=500)
    frame.pack()
    l1=Label(root7,text="AADHAAR NO.")
    l1.place(x=10,y=130)
    x3=tkinter.Entry(root7)
    x3.place(x=150,y=130)
    ad=x3.get()
    b1=Button(root7,text='Submit',command=view_data)
    b1.place(x=150,y=160)
    root7.resizable(False,False)
    root7.mainloop()

def view_data():
    global p1
    p1=x3.get()
    cur.execute('select * from appointment where idno=(%s)',(p1,))
    
    dat=cur.fetchall()
    print(dat)
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        det=a
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
        
root=Tk()
label=Label(root,text="KIS HOSPITAL",font="arial 100 bold",bg='light blue',)
b1=Button(text="Registration",font="arial 20 bold",fg='dark blue',command=register)
b2=Button(text="Appointment",font="arial 20 bold",fg='dark blue',command=apoint)
b3=Button(text="List of Doctors",font="arial 20 bold",fg='dark blue',command=lst_doc)
b4=Button(text="Services available",font='arial 20 bold',fg='dark blue',command=ser_avail)
b7=Button(text="View data",font='arial 20 bold',fg='dark blue',command=search_data)
b8=Button(text="View appointment data",font='arial 20 bold',fg='dark blue',command=search_data)
b6=Button(text="Exit",font='arial 20 bold',command=root.destroy,fg='red')
label.pack()
b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
b3.pack(side=LEFT,padx=10)
b4.pack(side=LEFT,padx=10)
b7.pack(side=LEFT,padx=10)
b8.pack(side=LEFT,padx=10)
b6.pack(side=LEFT,padx=10)

frame=Frame(root,height=600,width=70)
frame.pack()
root.resizable(False,False)
root.mainloop()



