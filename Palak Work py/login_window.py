from tkinter import *
from tkinter import ttk
import tkinter.font as f
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector as ms

try:
    con=ms.connect(host="localhost",user="root",database="bankmgt",password="",port=3306)
except:
    print("Error: connection is unsuccessful")
else:
    print("Connection successful")
win= Tk()
win.state("zoomed")
import create
import clicked
import deposit
import withdraw
import statement
import transaction


f1=f.Font(family="Proxima Nova",size=18,weight="bold")
f2=f.Font(family="Aerial",size=17,weight="bold")
f3=f.Font(family="Aerial",size=30,weight="bold")
f4=f.Font(family="Aerial",size=10)
f5=f.Font(family="Aerial",size=21,weight="bold")


#FIRST WINDOW

frame=Frame(win,height=1000,width=2000,background="#a10e38")
frame.pack(padx=0,pady=0)

frame1=Frame(win,height=3000,width=2000,bd=10,background="#a10e38")
frame1.pack(padx=0,pady=0)

label=Label(frame,text="Username",font=f1,background="#a10e38",fg="white")
label.place(x=100,y=260)

Name=StringVar()
name=Entry(frame,textvariable=Name,width=50)
name.place(x=300,y=260)
   
label1=Label(frame,text="Password",font=f1,background="#a10e38",fg="white")
label1.place(x=100,y=350)
  
Pass=StringVar()
pas=Entry(frame,textvariable=Pass,width=50)
pas.place(x=300,y=350)

label2=Label(frame,text="LOGIN WINDOW",font=f3,background="#a10e38",fg="white")
label2.place(x=220,y=100)

im=PhotoImage(file="C:/Users/DELL/Documents/Palak Work py/pnb.png")
label=Label(frame,image=im,bg="#a10e38")
label.image=im
label.place(x=800,y=260)

def clickedd():
    namee=Name.get()
    passs=Pass.get()
    cursor=con.cursor()
    n="select * from create_table"
    cursor.execute(n)
    result=cursor.fetchall()
    found=0
    for i in result:
        if(namee==i[8] and passs==i[9]):
            found=1
            na= i[0]
            pa= i[7]

            ba =i[2]
            import clicked
            clicked.clicked(win,na,pa,ba,i[8])
            break
    if found==0:
        messagebox.showerror("error", "Wrong Username or Password \n Try again")
        
bt=Button(frame,text="Create an account",font=f2,bg="#9e163c",fg="white",command=lambda:create.create(win),relief='flat')
bt.place(x=330,y=525)

login_bt=Button(frame,text="Login",command=clickedd,font=f2,width=10)
login_bt.place(x=370,y=450)

win.mainloop()


