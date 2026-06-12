from tkinter import *
from tkinter import ttk
import tkinter.font as f
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector as ms
try:
    con=ms.connect(host="localhost",user="root",database="bankmgt")
except:
    print("Error: connection is unsuccessful")
else:
    print("Connection successful")
win= Tk()
win.state("zoomed")

#FIRST WINDOW

frame=Frame(win,height=1000,width=2000,bd=10,background="#a10e38")
frame.pack(padx=40,pady=40)

f1=f.Font(family="Proxima Nova",size=18,weight="bold")
f2=f.Font(family="Aerial",size=17,weight="bold")
f3=f.Font(family="Aerial",size=30,weight="bold")
f4=f.Font(family="Aerial",size=10)

label=Label(frame,text="Username",font=f1)
label.place(x=100,y=260)

Name=StringVar()
name=Entry(frame,textvariable=Name,width=50)
name.place(x=300,y=260)

label1=Label(frame,text="Password",font=f1)
label1.place(x=100,y=350)

Pass=StringVar()
pas=Entry(frame,textvariable=Pass,width=50)
pas.place(x=300,y=350)

label2=Label(frame,text="LOGIN WINDOW",font=f3)
label2.place(x=220,y=100)


image=PhotoImage(file="C:/Users/DELL/Downloads/pnb.png")
label=Label(frame,image=image,bg="#a10e38")
label.place(x=750,y=220)

#lOGIN WINDOW

def clicked():
    pass

def submit():
    pass

def depo():
    pass

def withdraww():
    pass

def trans():
    pass

def statement():
    pass

def logout():
    win.destroy()
    pass


top=None
tree=None

def withdraw():
    withdraw=Toplevel()
    frame4=Frame(withdraw,height=500,width=500,bd=10,background="#a10e38")
    frame4.pack(padx=60,pady=10)

    title=Label(frame4,text="WITHDRAW",font=f2)
    title.place(x=180,y=30)

    label11=Label(frame4,text="Current Balance",font=f2)
    label11.place(x=20,y=150)

    Cb=StringVar()
    cb=Entry(frame4,textvariable=Cb,width=38)
    cb.place(x=240,y=155)

    label12=Label(frame4,text="Amount",font=f2)
    label12.place(x=20,y=220)

    Am=StringVar()
    am=Entry(frame4,textvariable=Am,width=38)
    am.place(x=240,y=225)

    label13=Label(frame4,text="Updated Balance",font=f2)
    label13.place(x=20,y=280)

    label14=Label(frame4,width=32,height=1)
    label14.place(x=240,y=287)

    submit_bt=Button(frame4,text="Submit",command=submit,font=f2,width=32,relief="groove")
    submit_bt.place(x=20,y=350)

    withdraw_bt=Button(frame4,text="Withdraw",command=withdraww,font=f2,width=32,relief="groove")
    withdraw_bt.place(x=20,y=410)

    image=PhotoImage(file="bank-removebg-preview.png")
    labell=Label(frame4,image=image,bg="#a10e38")
    labell.image=image
    labell.place(x=15,y=12)

    imagee=PhotoImage(file="bank-removebg-preview.png")
    labell=Label(frame4,image=imagee,bg="#a10e38")
    labell.image=imagee
    labell.place(x=330,y=12)
    
def deposit():
    depositt=Toplevel(win)
    frame3=Frame(depositt,height=500,width=500,bd=10,background="#a10e38")
    frame3.pack(padx=60,pady=10)

    title=Label(frame3,text="DEPOSIT",font=f2)
    title.place(x=180,y=30)

    label11=Label(frame3,text="Current Balance",font=f2)
    label11.place(x=20,y=150)

    Cb=StringVar()
    cb=Entry(frame3,textvariable=Cb,width=38)
    cb.place(x=240,y=155)

    label12=Label(frame3,text="Amount",font=f2)
    label12.place(x=20,y=220)

    Am=StringVar()
    am=Entry(frame3,textvariable=Am,width=38)
    am.place(x=240,y=225)

    label13=Label(frame3,text="Updated Balance",font=f2)
    label13.place(x=20,y=280)

    label14=Label(frame3,width=32,height=1)
    label14.place(x=240,y=287)

    submit_bt=Button(frame3,text="Submit",command=submit,font=f2,width=32,relief="groove")
    submit_bt.place(x=20,y=350)

    deposit_bt=Button(frame3,text="Deposit",command=depo,font=f2,width=32,relief="groove")
    deposit_bt.place(x=20,y=410)

    image=PhotoImage(file="bank-removebg-preview.png")
    labell=Label(frame3,image=image,bg="#a10e38")
    labell.image=image
    labell.place(x=15,y=12)

    imagee=PhotoImage(file="bank-removebg-preview.png")
    labell=Label(frame3,image=imagee,bg="#a10e38")
    labell.image=imagee
    labell.place(x=330,y=12)


def clicked():
    n="p"
    p="a"
    namee=Name.get()
    passs=Pass.get()
    if(namee==n and passs==p):
        dashboard=Toplevel()
        dashboard.state("zoomed")
    else:
        messagebox.showerror("error", "Wrong Username or Password \n Try again")

    frame1=Frame(dashboard,height=3000,width=2000,bd=10,background="#a10e38")
    frame1.pack(padx=40,pady=40)

    wel=Label(frame1,text="WELCOME, ADMIN!",font=f1)
    wel.pack(fill=X)

    na=Label(frame1,text="Name:",font=f1,bg="#a10e38",fg="white")
    na.place(x=100,y=100)

    pa=Label(frame1,text="  Palakpreet Kaur    ",font=f1,bg="#a10e38",fg="white")
    pa.place(x=350,y=100)


    ac=Label(frame1,text="Account Number:",font=f1,bg="#a10e38",fg="white")
    ac.place(x=100,y=150)

    no=Label(frame1,text="242520",font=f1,bg="#a10e38",fg="white")
    no.place(x=360,y=150)

    bal=Label(frame1,text="Balance:",font=f1,bg="#a10e38",fg="white")
    bal.place(x=100,y=200)

    balance=Label(frame1,text="0",font=f1,bg="#a10e38",fg="white")
    balance.place(x=360,y=200)


    depo_bt_img=PhotoImage(file="C:/Users/DELL/Documents/Palak Work py/depo-removebg-preview.png")
    depo_bt=Button(frame1,image=depo_bt_img,text="DEPOSIT",relief="groove",compound= 'left',command=deposit,font=f2)
    depo_bt.image=depo_bt_img
    depo_bt.place(x=70,y=350,width=220,height=160)  

    with_bt_img=PhotoImage(file="withdraw-removebg-preview.png")
    with_bt=Button(frame1,image=with_bt_img,text="WITHDRAW",relief="groove",command=withdraw,font=f2,compound= 'left')
    with_bt.image=with_bt_img
    with_bt.place(x=340,y=350,width=240,height=160)

    trans_bt_img=PhotoImage(file="trans-removebg-preview.png")
    trans_bt=Button(frame1,image=trans_bt_img,text="TRANSACTIONS",relief="groove",command=trans,font=f2,compound= 'left')    
    trans_bt.image=trans_bt_img
    trans_bt.place(x=630,y=350,width=290,height=160)

    state_bt_img=PhotoImage(file="C:/Users/DELL/Documents/Palak Work py/statement-removebg-preview.png")
    state_bt=Button(frame1,image=state_bt_img,text="STATEMENT",relief="groove",command=statement,font=f2,compound= 'left')
    state_bt.image=state_bt_img
    state_bt.place(x=970,y=350,width=250,height=160)

    frame1.pack_propagate(False)

    logout_bt=Button(frame1,text="Logout",command=logout,font=f2,width=10,relief="groove")
    logout_bt.place(x=1100,y=46)


#CREATE WINDOW

    
frame2=None
def clear():
    pass    

def quit():
    pass

def check():
    pass

def generate():
    pass

def create():
    createe=Toplevel(win)
    createe.state("zoomed")
    global frame2
    frame2=Frame(createe,height=1000,width=2000,bd=10,background="#a10e38")
    frame2.pack(padx=40,pady=40)

    frame2.pack_propagate(False)

    cre=Label(frame2,text="CREATE ACCOUNT",font=f1)
    cre.pack(fill=X)

    label3=Label(frame2,text="Account Number",font=f2)
    label3.place(x=50,y=100)

    Acc=StringVar()
    acc=Entry(frame2,textvariable=Name,width=50)
    acc.place(x=300,y=105)

    label4=Label(frame2,text="Account Number",font=f2)
    label4.place(x=50,y=100)

    Acc=StringVar()
    acc=Entry(frame2,textvariable=Acc,width=50)
    acc.place(x=300,y=105)

    label5=Label(frame2,text="Name",font=f2)
    label5.place(x=50,y=162)

    Nam=StringVar()
    nam=Entry(frame2,textvariable=Nam,width=50)
    nam.place(x=300,y=162)

    label6=Label(frame2,text="Account Type",font=f2)
    label6.place(x=50,y=220)

    
    typee=ttk.Combobox(frame2,width=47,state="readonly")
    typee.set("Select Account Type")
    typee['values']=("Savings account",
                   "Current account"
                   )
    typee.place(x=300,y=220)

    label7=Label(frame2,text="Initial Amount",font=f2)
    label7.place(x=50,y=280)

    Amt=StringVar()
    amt=Entry(frame2,textvariable=Amt,width=50)
    amt.place(x=300,y=280)

    label8=Label(frame2,text="Phone Number",font=f2)
    label8.place(x=50,y=340)

    Phn=StringVar()
    phn=Entry(frame2,textvariable=Phn,width=50)
    phn.place(x=300,y=340)

    label9=Label(frame2,text="Gender",font=f2)
    label9.place(x=50,y=400)

    
    gen=ttk.Combobox(frame2,width=47,state="readonly")
    gen["values"]=("Female",
                   "Male",
                   "Transgender"
                   )
    gen.set("Select Gender")
    gen.place(x=300,y=400)

    label9=Label(frame2,text="Date of Birth",font=f2)
    label9.place(x=50,y=460)

    cal=DateEntry(frame2,selectmode="day",state="readonly",date_pattern="yyyy-mm-dd")
    cal.place(x=300,y=460)
    

    label10=Label(frame2,text="Email",font=f2)
    label10.place(x=750,y=200)

    generate_bt=Button(frame2,text="Generate Account Number",font=f2,bg="white",command=generate,relief="groove")
    generate_bt.place(x=750,y=100)
     
    Email=StringVar()
    email=Entry(frame2,textvariable=Email,width=50)
    email.place(x=860,y=205)

    clear_bt=Button(frame2,text="Submit",font=f2,bg="white",command=clear,relief="groove")
    clear_bt.place(x=750,y=300)

    quit_bt=Button(frame2,text="Quit",font=f2,bg="white",command=quit,relief="groove")
    quit_bt.place(x=890,y=300)    

    checkbox = Checkbutton(frame2,bg="#9e163c",fg="white",font=f4,text="I hereby declare all these details are correct and all the documents have been submitted.")
    checkbox.place(x=730,y=390)


bt=Button(frame,text="Create an account",font=f2,bg="#9e163c",command=create,fg="white",relief='flat')
bt.place(x=270,y=550)    

        
login_bt=Button(frame,text="Login",command=clicked,font=f2,width=10)
login_bt.place(x=370,y=450)




 
     
    
  
