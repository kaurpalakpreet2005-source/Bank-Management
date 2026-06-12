from tkinter import *
from tkinter import ttk
import tkinter.font as f
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector as ms
import pandas as pd
from datetime import datetime
try:
    con=ms.connect(host="localhost",user="root",database="bankmgt")
except:
    print("Error: connection is unsuccessful")
else:
    print("Connection successful")


def trans(Us):
    win=Toplevel()
    frame5=Frame(win,background="#a10e38",height=1500,width=900)
    frame5.pack(padx=0,pady=0)
    style = ttk.Style()
    style.theme_use("clam")  
    style.configure("Treeview", rowheight=40, font=("Proxima Nova", 12, "bold"),background="#a10e38",foreground="white",fieldbackground="#a10e38")
    style.configure("Treeview.Heading",background="#a10e38",foreground="white")
    
    tree=ttk.Treeview(frame5,columns=("date","type of transaction","amount"),show="tree headings")
    
    tree.heading("#0", text="Sr. no")
    tree.column("#0", width=100, anchor=CENTER)
    tree.heading("date", text="Date")
    tree.heading("type of transaction", text="Type of Transaction")
    tree.heading("amount", text="Amount")
    
    
    tree.column("date", width=100, anchor=CENTER)
    tree.column("type of transaction", width=150, anchor=CENTER)
    tree.column("amount", width=100, anchor=CENTER)
    tree.pack(expand=True, fill='both')

    df=pd.read_csv(Us+".csv")
    for index,row in df.iterrows():
        tree.insert("",END,text=row["Sr. no"],
            values=(
                row["Date"],
                row["Type of Transaction"],
                row["Amount"]))



