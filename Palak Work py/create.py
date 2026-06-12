from tkinter import *
from tkinter import ttk
import tkinter.font as f
import pandas as pd
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector as ms
from datetime import datetime
try:
    con=ms.connect(host="localhost",user="root",database="bankmgt",password="",port=3306)
except:
    print("Error: connection is unsuccessful")
else:
    print("Connection successful")


    
def create(oldwin):
    win=Toplevel(oldwin)
    f1=f.Font(family="Proxima Nova",size=18,weight="bold")
    f2=f.Font(family="Aerial",size=17,weight="bold")
    f3=f.Font(family="Aerial",size=30,weight="bold")
    f4=f.Font(family="Aerial",size=10)

    frame2=Frame(win,height=1000,width=2000,bd=10,background="#a10e38")
    frame2.pack(padx=0,pady=0)

    frame2.pack_propagate(False)

    cre=Label(frame2,text="CREATE ACCOUNT",font=f1)
    cre.pack(fill=X)

    def move_next(event):
         event.widget.tk_focusNext().focus()
         return "break"

    label3=Label(frame2,text="Username",font=f2,background="#a10e38",fg="white")
    label3.place(x=50,y=110)

    Us=StringVar()
    us=Entry(frame2,textvariable=Us,width=50)
    us.place(x=300,y=115)
    us.bind("<Return>",move_next)
    

    label3=Label(frame2,text="Password",font=f2,background="#a10e38",fg="white")
    label3.place(x=50,y=160)

    Pas=StringVar()
    pas=Entry(frame2,textvariable=Pas,width=50)
    pas.place(x=300,y=165)
    pas.bind("<Return>",move_next)

    label4=Label(frame2,text="Account Number",font=f2,background="#a10e38",fg="white")
    label4.place(x=50,y=212)

    Acc=StringVar()
    acc=Entry(frame2,textvariable=Acc,width=50)
    acc.place(x=300,y=216)
    acc.bind("<Return>",move_next)

    label5=Label(frame2,text="Name",font=f2,background="#a10e38",fg="white")
    label5.place(x=50,y=265)

    Nam=StringVar()
    nam=Entry(frame2,textvariable=Nam,width=50)
    nam.place(x=300,y=266)
    nam.bind("<Return>",move_next)

    label6=Label(frame2,text="Account Type",font=f2,background="#a10e38",fg="white")
    label6.place(x=50,y=317)

    
    typee=ttk.Combobox(frame2,width=47,state="readonly")
    typee.set("Select Account Type")
    typee['values']=("Savings account",
                   "Current account"
                   )
    typee.place(x=300,y=320)
    typee.bind("<Return>",move_next)

    label7=Label(frame2,text="Initial Amount",font=f2,background="#a10e38",fg="white")
    label7.place(x=50,y=370)

    Amt=StringVar()
    amt=Entry(frame2,textvariable=Amt,width=50)
    amt.place(x=300,y=373)
    amt.bind("<Return>",move_next)

    label8=Label(frame2,text="Phone Number",font=f2,background="#a10e38",fg="white")
    label8.place(x=50,y=422)

    Phn=StringVar()
    phn=Entry(frame2,textvariable=Phn,width=50)
    phn.place(x=300,y=425)
    phn.bind("<Return>",move_next)

    label9=Label(frame2,text="Gender",font=f2,background="#a10e38",fg="white")
    label9.place(x=50,y=473)

    gen=ttk.Combobox(frame2,width=47,state="readonly")
    gen["values"]=("Female",
                   "Male",
                   "Transgender"
                   )
    gen.set("Select Gender")
    gen.place(x=300,y=475)
    gen.bind("<Return>",move_next)

    label9=Label(frame2,text="Date of Birth",font=f2,background="#a10e38",fg="white")
    label9.place(x=50,y=522)

    cal=DateEntry(frame2,selectmode="day",state="readonly",date_pattern="yyyy-mm-dd")
    cal.place(x=300,y=524)
    cal.bind("<Return>",move_next)
    
    label10=Label(frame2,text="Email",font=f2,background="#a10e38",fg="white")
    label10.place(x=750,y=200)

    def generate():
        cursor=con.cursor()
        sql="select Account_No from create_table order by account_no desc limit 1"
        cursor.execute(sql)
        global result
        result = cursor.fetchone()
        con.commit()
        Acc.set(result[0]+1)

    generate_bt=Button(frame2,text="Generate Account Number",command=generate,font=f2,bg="white",relief="groove")
    generate_bt.place(x=750,y=100)

    Email=StringVar()
    email=Entry(frame2,textvariable=Email,width=50)
    email.place(x=860,y=205)
    email.bind("<Return>",move_next)

    def submit():
        cursor=con.cursor()
        sql="insert into create_table(Account_no,Name,Account_Type,Amount,Phone_Number,Gender,DOB,Email,Username,Password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        val=(result[0]+1,
             Nam.get(),
             typee.get(),
             Amt.get(),
             Phn.get(),
             gen.get(),
             cal.get(),
             Email.get(),
             Us.get(),
             Pas.get())
        cursor.execute(sql, val)
        con.commit()
        print(cursor.rowcount, "record inserted.")

        today = datetime.today().strftime("%d/%m/%Y")
        
        data = {
            "Sr. no" :[1],
            "Date" :[today],
            "Type of Transaction" :["Deposit"],
            "Amount" :[Amt.get()],
            "Description":["Initial Amount"]
            }
        
        df = pd.DataFrame(data)
        df.to_csv(Us.get()+".csv", index=False)

    clear_bt=Button(frame2,text="Submit",font=f2,bg="white",relief="groove",command=submit)
    clear_bt.place(x=750,y=370)

    quit_bt=Button(frame2,text="Quit",font=f2,bg="white",command=quit,relief="groove")
    quit_bt.place(x=890,y=370)    

    checkbox = Checkbutton(frame2,bg="#9e163c",fg="white",font=f4,text="I hereby declare all these details are correct and all the documents have been submitted.")
    checkbox.place(x=730,y=300)

    us.focus_set()
