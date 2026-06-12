from tkinter import *
from tkinter import ttk
import tkinter.font as f
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector as ms
import deposit
import withdraw
import transaction
import statement

try:
    con=ms.connect(host="localhost",user="root",database="bankmgt")
except:
    print("Error: connection is unsuccessful")
else:
    print("Connection successful")


f1=f.Font(family="Proxima Nova",size=18,weight="bold")
f2=f.Font(family="Aerial",size=17,weight="bold")
f3=f.Font(family="Aerial",size=30,weight="bold")
f4=f.Font(family="Aerial",size=10)

def logout(oldwin):
    oldwin.destroy()

def withdraww():
    pass

def clicked(oldwin,cname,accno,ba,Us):
    win=Toplevel(oldwin)
    
    frame1=Frame(win,height=3000,width=2000,bd=10,background="#a10e38")
    frame1.pack(padx=0,pady=0)

    wel=Label(frame1,text="WELCOME, ADMIN!",font=f1)
    wel.pack(fill=X)

    na=Label(frame1,text="Name:",font=f1,bg="#a10e38",fg="white")
    na.place(x=100,y=100)

    pa=Label(frame1,text=cname ,font=f1,bg="#a10e38",fg="white")
    pa.place(x=360,y=100)

    ac=Label(frame1,text="Account Number:",font=f1,bg="#a10e38",fg="white")
    ac.place(x=100,y=150)

    no=Label(frame1,text=accno,font=f1,bg="#a10e38",fg="white")
    no.place(x=360,y=150)

    bal=Label(frame1,text="Balance:",font=f1,bg="#a10e38",fg="white")
    bal.place(x=100,y=200)

   
    balance=Label(frame1,text=ba,font=f1,bg="#a10e38",fg="white")
    balance.place(x=360,y=200)

    depo_bt_img=PhotoImage(file="C:/Users/DELL/Documents/Palak Work py/depo-removebg-preview.png")
    depo_bt=Button(frame1,image=depo_bt_img,text="DEPOSIT",command=lambda:deposit.deposit(Us),relief="groove",compound= 'left',font=f2)
    depo_bt.image=depo_bt_img
    depo_bt.place(x=70,y=350,width=220,height=160)  

    with_bt_img=PhotoImage(file="withdraw-removebg-preview.png")
    with_bt=Button(frame1,image=with_bt_img,text="WITHDRAW",command=lambda:withdraw.withdraw(Us),relief="groove",font=f2,compound= 'left')
    with_bt.image=with_bt_img
    with_bt.place(x=340,y=350,width=240,height=160)

    trans_bt_img=PhotoImage(file="trans-removebg-preview.png")
    trans_bt=Button(frame1,image=trans_bt_img,text="TRANSACTIONS",relief="groove",command= lambda:transaction.trans(Us),font=f2,compound= 'left')    
    trans_bt.image=trans_bt_img
    trans_bt.place(x=630,y=350,width=290,height=160)

    state_bt_img=PhotoImage(file="C:/Users/DELL/Documents/Palak Work py/statement-removebg-preview.png")
    state_bt=Button(frame1,image=state_bt_img,text="STATEMENT",relief="groove",command= lambda:statement.statement(Us,cname),font=f2,compound= 'left')
    state_bt.image=state_bt_img
    state_bt.place(x=970,y=350,width=250,height=160)

    frame1.pack_propagate(False)


    logout_bt=Button(frame1,text="Logout",font=f2,command=lambda:logout(win),width=10,relief="groove")
    logout_bt.place(x=1100,y=46)
