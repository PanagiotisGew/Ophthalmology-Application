import tkinter
import sqlite3
rootE=None
var=None


def inp():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,var
    e1=t1.get()
    e2=t2.get()
    e3=t10.get()
    e4=t3.get()
    e5=t9.get()
    e6=t4.get()
    e7=t5.get()
    e8=t6.get()
    e9=t7.get()
    e10=t9.get()
    e11=t11.get()
    e12=t12.get()
    e13=t13.get()
    e14=t14.get()
    e15=t15.get()
    e16=t16.get()
    conn = sqlite3.connect("MDBA.db")
    conn.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "EMPLOYEE DATA ADDED")

def ex():
    rootE.destroy()

def emp_screen():
    global rootE,t1,t2,r1,r2,t3,lb,t4,t5,t6,t7,var,t8,t9,t10,t11,t12,t13,t14,t15,t16
    rootE=tkinter.Tk()
    rootE.title("AΠΟΤΕΛΕΣΜΑΤΑ ΕΞΕΤΑΣΕΩΝ")
    rootE.geometry('600x720')
    var = tkinter.StringVar(master=rootE)
    H=tkinter.Label(rootE,text="AΠΟΤΕΛΕΣΜΑΤΑ ΕΞΕΤΑΣΕΩΝ",fg='grey',font="Arial 10 bold")
    H.place(x=50,y=20)
    l1=tkinter.Label(rootE,text="ΑΜΚΑ ΑΣΘΕΝΗ")
    l1.place(x="50",y="50")
    t1=tkinter.Entry(rootE)
    t1.place(x='240',y='50')
    l2 = tkinter.Label(rootE, text="ΟΝΟΜΑ ΑΣΘΕΝΗ")
    l2.place(x=50,y=80)
    t2 = tkinter.Entry(rootE)
    t2.place(x='240', y='80')
    l4 = tkinter.Label(rootE, text="Βαθμός μυωπίας δεξί μάτι")
    l4.place(x=50,y=290)
    t3=tkinter.Entry(rootE)
    t3.place(x=240,y=290)
    l6=tkinter.Label(rootE,text="βαθμός υπερμετρωπίας δεξί μάτι")
    l6.place(x=50,y=320)
    t4=tkinter.Entry(rootE)
    t4.place(x=240,y=320)
    l7 = tkinter.Label(rootE, text="βαθμός αστιγματισμού δεξί μάτι")
    l7.place(x=50,y=380)
    t5 = tkinter.Entry(rootE)
    t5.place(x=240,y=380)
    l8 = tkinter.Label(rootE, text="Πίεση δεξιού ματιού")
    l8.place(x=50,y=470)
    t6 = tkinter.Entry(rootE)
    t6.place(x=240,y=470)

    l9 = tkinter.Label(rootE, text="κόστος εξετασης")
    l9.place(x=50,y=170)
    t7=tkinter.Entry(rootE)
    t7.place(x=240,y=170)

    l12 = tkinter.Label(rootE, text="ΗΜΕΡΟΜΗΝΙΑ")
    l12.place(x=50,y=140)
    t11=tkinter.Entry(rootE)
    t11.place(x=240,y=140)
    
    
    l13 = tkinter.Label(rootE, text="Βαθμός μυωπίας αριστερό μάτι")
    l13.place(x=50,y=260)
    t12=tkinter.Entry(rootE)
    t12.place(x=240,y=260)

    
    l14 = tkinter.Label(rootE, text="βαθμός υπερμετρωπίας αριστερό μάτι")
    l14.place(x=50,y=350)
    t13=tkinter.Entry(rootE)
    t13.place(x=240,y=350)

    
    l15 = tkinter.Label(rootE, text="Βαθμος πρεσβυωπία αριστερό")
    l15.place(x=50,y=200)
    t14=tkinter.Entry(rootE)
    t14.place(x=240,y=200)

    
    l16 = tkinter.Label(rootE, text="Πίεση αριστερού ματιού")
    l16.place(x=50,y=440)
    t15=tkinter.Entry(rootE)
    t15.place(x=240,y=440)

    
    l17 = tkinter.Label(rootE, text="βαθμός αστιγματισμού αριστερό ")
    l17.place(x=50,y=410)
    t16=tkinter.Entry(rootE)
    t16.place(x=240,y=410)

    

    l10 = tkinter.Label(rootE, text="ID ΡΑΝΤΕΒΟΥ")
    l10.place(x=50,y=110)
    t9=tkinter.Entry(rootE)
    t9.place(x=240,y=110)

    l11 = tkinter.Label(rootE, text="Βαθμός πρεσβυωπία δεξί μάτι")
    l11.place(x=50,y=230)
    t10=tkinter.Entry(rootE)
    t10.place(x=240,y=230)

    b1=tkinter.Button(rootE,text="ΑΠΟΘΗΚΕΥΣΗ",command=inp)
    b1.place(x=60,y=500)
    
    b3=tkinter.Button(rootE,text="ΕΞΟΔΟΣ",command=ex)
    b3.place(x=230,y=500)
    

    dd_4 = tkinter.Label(rootE, text="Για βαθμο μυωπίας >=1,25 φακός γυαλιών 50Ε")
    dd_4.place(x=50, y=550) 

    dd_5 = tkinter.Label(rootE, text="Για βαθμο μυωπίας >=1,25 φακός γυαλιών 50Ε")
    dd_5.place(x=50, y=580) 

    dd_6 = tkinter.Label(rootE, text="Για βαθμο μυωπίας >=2 φακός γυαλιών 100Ε")
    dd_6.place(x=50, y=610) 

    dd_7 = tkinter.Label(rootE, text="Για βαθμο μυωπίας >= 10 φακός γυαλιών 150Ε")
    dd_7.place(x=50, y=640) 

    dd_8 = tkinter.Label(rootE, text="Για βαθμο μυωπίας >= 15 φακός γυαλιών 150Ε")
    dd_8.place(x=50, y=670) 

    dd_8 = tkinter.Label(rootE, text="Για βαθμο μυωπίας = 20 φακός γυαλιών 200Ε  ")
    dd_8.place(x=50, y=700) 

    rootE.mainloop()

 
rootDE=None


