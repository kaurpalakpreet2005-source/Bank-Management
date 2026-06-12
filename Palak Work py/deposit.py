from tkinter import *
from tkinter import ttk
import tkinter.font as f
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector as ms
import pandas as pd
from datetime import date
from datetime import datetime
import os
try:
    con=ms.connect(host="localhost",user="root",database="bankmgt")
except:
    print("Error: connection is unsuccessful")
else:
    print("Connection successful")

def submit(user_amount,current_balance,ub):
    ub.set(str(int(current_balance)+int(user_amount)))

def depo(acc,bal):
    pass

def deposit(Us):
    win=Toplevel()
    f1=f.Font(family="Proxima Nova",size=18,weight="bold")
    f2=f.Font(family="Aerial",size=17,weight="bold")
    f3=f.Font(family="Aerial",size=30,weight="bold")
    f4=f.Font(family="Aerial",size=10)
    f5=f.Font(family="Aerial",size=21,weight="bold")
    f6=f.Font(family="Aerial",size=9,weight="bold")

    frame3=Frame(win,height=520,width=600,bd=10,background="#a10e38")
    frame3.pack(padx=0,pady=0)

    title=Label(frame3,text="BALANCE DEPOSIT",font=f5,background="#a10e38",fg="white")
    title.place(x=160,y=30)


    label11=Label(frame3,text="Current Balance",font=f2,background="#a10e38",fg="white")
    label11.place(x=20,y=120)

    cur= con.cursor()
    query= "select Amount from create_table where username=%s"
    cur.execute(query,(Us,))
    data=cur.fetchone()
    
    label15=Label(frame3,text=data[0],width=36,height=1,font=f6)
    label15.place(x=290,y=125)
    
    label12=Label(frame3,text="Amount",font=f2,background="#a10e38",fg="white")
    label12.place(x=20,y=180)

    Am=IntVar()
    am=Entry(frame3,textvariable=Am,width=42)
    am.place(x=290,y=185)

    label13=Label(frame3,text="Updated Balance",font=f2,background="#a10e38",fg="white")
    label13.place(x=20,y=309)
    
    Ub=StringVar()
    ub=Entry(frame3,textvariable=Ub,width=42)
    ub.place(x=290,y=316)

    label15=Label(frame3,text="Description",font=f2,background="#a10e38",fg="white")
    label15.place(x=20,y=242)
    
    des_text= Text(frame3,width= 28,height=2,font=2)
    des_text.place(x=290,y=245)

    submit_bt=Button(frame3,text="Submit",command=lambda:submit(Am.get(),data[0],Ub),font=f1,width=36,relief="groove")
    submit_bt.place(x=20,y=370)

    deposit_bt=Button(frame3,text="Deposit",command=lambda:depo(Us,Am,des_text),font=f1,width=36,relief="groove")
    deposit_bt.place(x=20,y=430)

    image=PhotoImage(file="bank-removebg-preview.png")
    labell=Label(frame3,image=image,bg="#a10e38")
    labell.image=image
    labell.place(x=15,y=12)

    imagee=PhotoImage(file="bank-removebg-preview.png")
    labell=Label(frame3,image=imagee,bg="#a10e38")
    labell.image=imagee
    labell.place(x=450,y=12)
    
def depo(Us,Am,des_text):
    description=des_text.get("1.0",END).strip()
    cur=con.cursor()
    query="update create_table set Amount=Amount+%s where Username=%s"
    amount=Am.get()
    cur.execute(query,(amount,Us))
    con.commit()

    

    if os.path.exists(Us+".csv"):
        df_old=pd.read_csv(Us+".csv")
        sr=len(df_old)+1

    else:
        sr=1

    today = datetime.today().strftime("%d/%m/%Y")    
    data={
        "Sr. no":[sr],
        "Date":[today],
        "Type of Transaction":["Deposit"],
        "Amount":[amount],
        "Description":[description]
    }

    df=pd.DataFrame(data)
    if os.path.exists(Us+".csv"):
        df.to_csv(Us+".csv",mode="a",header=False,index=False)
    else:
        df.to_csv(Us+".csv",index=False)


