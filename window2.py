import tkinter
import sqlite3
import tkinter.messagebox
from PATDELSU import P_display
from PATDELSU import P_display2
from PATDELSU import D_display
from PATDELSU import P_UPDATE
from RooMT import Room_all
from BILLING import BILLING
from employee_reg import emp_screen
from appointment import appo

conn=sqlite3.connect("MDBA.db")
print("DATABASE CONNECTION SUCCESSFUL")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None


#EXIT for MENU
def ex():
    global root1
    root1.destroy()

#MENU BUTTONS
def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    root1.geometry("280x350")
    root1.title("ΚΥΡΙΟ ΙΑΤΡΟΥ")
    m=tkinter.Label(root1,text="ΜΕΝΟΥ",fg='black',font='Times 16 bold italic',bg='green')
    button1=tkinter.Button(root1,text="1.ΕΓΓΡΑΦΗ ΑΣΘΕΝΗ",command=PAT,bg='light blue',fg='black')
    button2 = tkinter.Button(root1, text="2.ΦΑΡΜΑΚΕΥΤΙΚΗ ΑΓΩΓΗ",bg='light green',fg='black',command=Room_all)
    button3 = tkinter.Button(root1, text="3.ΠΡΟΣΘΗΚΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ",bg='light blue',fg='black',command=emp_screen)
    button4 = tkinter.Button(root1, text="4.ΠΡΟΣΘΗΚΗ ΡΑΝΤΕΒΟΥ",bg='light green',fg='black',command=appo)
    button5 = tkinter.Button(root1, text="5.ΑΠΟΤΕΛΕΣΜΑΤΑ",bg='light blue',fg='black',command=BILLING)
    button6 = tkinter.Button(root1, text="6.ΕΞΟΔΟΣ",command=ex,bg='light green',fg='black')
    m.place(x=75,y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80,y=50)
    button2.pack(side=tkinter.TOP)
    button2.place(x=80,y=100)
    button3.pack(side=tkinter.TOP)
    button3.place(x=80,y=150)
    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=200)
    button5.pack(side=tkinter.TOP)
    button5.place(x=80,y=250)
    button6.pack(side=tkinter.TOP)
    button6.place(x=80,y=300)
    root1.mainloop()

def menu2():
    global root1,button7,button10,n,button12
    root1=tkinter.Tk()
    root1.geometry("280x350")
    root1.title("ΚΥΡΙΟ ΥΠΑΛΗΛΟΥ")
    n=tkinter.Label(root1,text="ΜΕΝΟΥ",fg='black',font='Times 16 bold italic',bg='WHITE')
    button7=tkinter.Button(root1,text="1.ΕΓΓΡΑΦΗ ΑΣΘΕΝΗ",command=PAT,bg='light blue',fg='black')
    button10 = tkinter.Button(root1, text="2.ΠΡΟΣΘΗΚΗ ΡΑΝΤΕΒΟΥ",bg='light green',fg='black',command=appo)
    button12 = tkinter.Button(root1, text="3.ΕΞΟΔΟΣ",command=ex,bg='light green',fg='black')
    n.place(x=75,y=5)
    button7.pack(side=tkinter.TOP)
    button7.place(x=80,y=50)
    button10.pack(side=tkinter.TOP)
    button10.place(x=80, y=100)
    button12.pack(side=tkinter.TOP)
    button12.place(x=80,y=150)
    root1.mainloop()

p=None
#input patient form
def IN_PAT():
    global pp1, pp2, pp3,conn
    conn=sqlite3.connect("MDBA.db")
    conn.cursor()
    pp1=pat_ID.get()
    pp2=pat_name.get()
    pp3=pat_sex.get()
    conn.execute('INSERT INTO PATIENT VALUES(?,?,?)',(pp1,pp2,pp3,))
    
    tkinter.messagebox.showinfo("ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ","ΕΠΙΤΥΧΗΣ ΕΓΓΡΑΦΗ ΑΣΘΕΝΗ")
    conn.commit()


#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
def nothing():
    print("CONTACT DATABASE HEAD :921 ")

def nothing1():
    print("MADE BY BHAVIYA BATRA")

#PATIENT FORM
 
SEARCH=None
DELETE=None
UPDATE=None

def PAT():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootp,regform,id,name,dob,sex,email,ct,addr,c1,c2,bg,SUBMIT,menubar,filemenu, SEARCH,DELETE,UPDATE
    rootp=tkinter.Tk()
    rootp.title("MEDANTA PATIENT FORM")
    menubar=tkinter.Menu(rootp)
    filemenu=tkinter.Menu(menubar,tearoff=0)
    filemenu.add_command(label="NEW",command=PAT)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXO)
    helpmenu=tkinter.Menu(menubar,tearoff=0)
    helpmenu.add_command(label="HELP",command=nothing)
    helpmenu.add_command(label="ABOUT",command=nothing1)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    rootp.config(menu=menubar)
    regform=tkinter.Label(rootp,text="Εγγραφή ασθενών",font="Arial 16 bold")
    id=tkinter.Label(rootp,text="ΑΜΚΑ")
    pat_ID=tkinter.Entry(rootp)
    name=tkinter.Label(rootp,text="Ονοματεπώνυμο")
    pat_name = tkinter.Entry(rootp)
    sex=tkinter.Label(rootp,text="Ασφάλιση")
    pat_sex=tkinter.Entry(rootp)
     
    SEARCH=tkinter.Button(rootp,text="  ΑΝΑΖΉΤΗΣΗ ΑΜΚΑ >>  ",command=P_display)
    SEARCH2=tkinter.Button(rootp,text="  ΑΝΑΖΉΤΗΣΗ ΟΝΟΜ/ΝΥΜΟ >>  ",command=P_display2)
    DELETE=tkinter.Button(rootp,text="  ΔΙΑΓΡΑΦΗ  ",command=D_display)
    UPDATE=tkinter.Button(rootp,text="  ΕΠΕΞΕΡΓΑΣΙΑ  ",command=P_UPDATE)
    SUBMIT=tkinter.Button(rootp,text="  ΥΠΟΒΟΛΗ  ",command=IN_PAT,)
    regform.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    SUBMIT.pack()
   
    UPDATE.pack(side=tkinter.LEFT)
    DELETE.pack(side=tkinter.LEFT)
    SEARCH.pack(side=tkinter.LEFT)
    SEARCH2.pack(side=tkinter.LEFT)
    rootp.mainloop()

