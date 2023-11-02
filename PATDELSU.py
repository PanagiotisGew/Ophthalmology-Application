import tkinter
import sqlite3
import tkinter.messagebox
conn=sqlite3.connect("MDBA.db")
#variables
rootU=None
rootD=None
rootS=None
head=None
inp_s=None
searchB=None
#display/search button

def Search_button():
    global inp_s,entry,errorS,t,i,dis1,dis2,dis3 
    global l1,l2,l3 
    c1=conn.cursor()
    inp_s=entry.get()
    p=list(c1.execute('select * from PATIENT where PATIENT_ID=?',(inp_s,)))
    if (len(p)==0):
        errorS=tkinter.Label(rootS,text="ΔΕΝ ΒΡΕΘΗΚΕ ΑΜΚΑ")
        errorS.pack()
    else:
        t=c1.execute('SELECT * FROM PATIENT where PATIENT_ID=?',(inp_s,));
        for i in t:
            l1=tkinter.Label(rootS,text="ΑΜΚΑ",fg='blue')
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="ΟΝΟΜΑΤΕPΩΝΥΜΟ ΑΣΘΕΝΗ",fg='blue')
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="ΑΣΦΑΛΕΙΑ ΑΣΘΕΝΗ",fg='blue')
            dis3=tkinter.Label(rootS,text=i[2])
            l1.pack()
            dis1.pack()
            l2.pack()
            dis2.pack()
            l3.pack()
            dis3.pack()
            conn.commit()


def RESULT_Search_button():
    global inp_s,entry,errorS,t,i,dis1,dis2,dis3,dis4,dis5
    global l1,l2,l3,l4,l5
    c1=conn.cursor()
    inp_s=entry.get()
    p=list(c1.execute('select * from appointment where PATIENT_ID=?',(inp_s,)))
    if (len(p)==0):
        errorS=tkinter.Label(rootS,text="ΔΕΝ ΒΡΕΘΗΚΕ ΑΜΚΑ")
        errorS.pack()
    else:
        t=c1.execute('SELECT * FROM appointment where PATIENT_ID=?',(inp_s,));
        for i in t:
            l1=tkinter.Label(rootS,text="ΑΜΚΑ",fg='blue')
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="ΟΝΟΜΑΤΕPΩΝΥΜΟ ΑΣΘΕΝΗ",fg='blue')
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="ΑΣΦΑΛΕΙΑ ΑΣΘΕΝΗ",fg='blue')
            dis3=tkinter.Label(rootS,text=i[2])
            l4=tkinter.Label(rootS,text="ΑΣΦΑΛΕΙΑ ΑΣΘΕΝΗ",fg='blue')
            dis4=tkinter.Label(rootS,text=i[3])
            l5=tkinter.Label(rootS,text="ΑΣΦΑΛΕΙΑ ΑΣΘΕΝΗ",fg='blue')
            dis5=tkinter.Label(rootS,text=i[4])
            l1.pack()
            dis1.pack()
            l2.pack()
            dis2.pack()
            l4.pack()
            dis4.pack()
            l5.pack()
            dis5.pack()
            conn.commit()



def Search_button2():
    global inp_s,entry,errorS,t,i,q,dis1,dis2,dis3 
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    c1=conn.cursor()
    inp_s=entry.get()
    p=list(c1.execute('select * from PATIENT where NAME=?',(inp_s,)))
    if (len(p)==0):
        errorS=tkinter.Label(rootS,text=" ΔΕΝ ΒΡΕΘΗΚΕ ΟΝΟΜΑ")
        errorS.pack()
    else:
        t=c1.execute('SELECT * FROM PATIENT where NAME=?',(inp_s,));
        for i in t:
            l1=tkinter.Label(rootS,text="ΑΜΚΑ",fg='blue')
            dis1=tkinter.Label(rootS,text=i[0])
            l2=tkinter.Label(rootS,text="ΟΝΟΜΑΤΕΠΩΝΥΜΟ ΑΣΘΕΝΗ",fg='blue')
            dis2=tkinter.Label(rootS,text=i[1])
            l3=tkinter.Label(rootS,text="ΑΣΦΑΛΕΙΑ ΑΣΘΕΝΗ",fg='blue')
            dis3=tkinter.Label(rootS,text=i[2])
            l1.pack()
            dis1.pack()
            l2.pack()
            dis2.pack()
            l3.pack()
            dis3.pack()
            conn.commit()


def eXO():
    rootS.destroy()

##search window
def P_display():
    global rootS,head,inp_s,entry,searchB
    rootS=tkinter.Tk()
    rootS.title("SEARCH WINDOW")
    head=tkinter.Label(rootS,text="ΥΠΕΒΑΛΕ ΑΜΚΑ ΓΙΑ ΑΝΑΖΗΤΗΣΗ",fg="red")
    entry=tkinter.Entry(rootS)
    searchB=tkinter.Button(rootS,text='ΑΝΑΖΗΤΗΣΗ',command=Search_button)
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="ΝΕΟ", command=P_display)
    filemenu.add_separator()
    filemenu.add_command(label="ΕΞΟΔΟΣ", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    head.pack()
    entry.pack()
    searchB.pack()
    rootS.mainloop()


def P_display_res():
    global rootS,head,inp_s,entry,searchB
    rootS=tkinter.Tk()
    rootS.title("SEARCH WINDOW")
    head=tkinter.Label(rootS,text="ΥΠΕΒΑΛΕ ΑΜΚΑ ΓΙΑ ΑΝΑΖΗΤΗΣΗ",fg="red")
    entry=tkinter.Entry(rootS)
    searchB=tkinter.Button(rootS,text='ΑΝΑΖΗΤΗΣΗ',command=RESULT_Search_button)
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_display)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    head.pack()
    entry.pack()
    searchB.pack()
    rootS.mainloop()

def P_display2():
    global rootS,head,inp_s,entry,searchB
    rootS=tkinter.Tk()
    rootS.title("SEARCH WINDOW")
    head=tkinter.Label(rootS,text="ΥΠΕΒΑΛΕ ON/MO ΓΙΑ ΑΝΑΖΗΤΗΣΗ",fg="red")
    entry=tkinter.Entry(rootS)
    searchB=tkinter.Button(rootS,text='ΑΝΑΖΗΤΗΣΗ',command=Search_button2)
    menubar= tkinter.Menu(rootS)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_display2)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=eXO)
    menubar.add_cascade(label="File", menu=filemenu)
    rootS.config(menu=menubar)
    head.pack()
    entry.pack()
    searchB.pack()
    rootS.mainloop()

inp_d=None
entry1=None
errorD=None
disd1=None

#DELTE BUTTON
def Delete_button():
    global inp_d,entry1,errorD,disd1
    c1= conn.cursor()
    inp_d = entry1.get()
    p=list(conn.execute("select * from PATIENT where PATIENT_ID=?", (inp_d,)))
    if (len(p)==0):
        errorD = tkinter.Label(rootD, text="ΔΕΝ ΒΡΕΘΗΚΕ ΑΜΚΑ")
        errorD.pack()
    else:
        conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(inp_d,))
        disd1=tkinter.Label(rootD,text="Ο ΑΣΘΕΝΗΣ ΔΙΑΓΡΆΦΗΚΕ",fg='green')
        disd1.pack()
        conn.commit()


## DELETE SCREEN
def D_display():
    global rootD,headD,inp_d,entry1,DeleteB
    rootD=tkinter.Tk()
    rootD.title("DELETE WINDOW")
    headD=tkinter.Label(rootD,text="ΥΠΕΒΑΛΕ ΑΜΚΑ ΓΙΑ ΑΝΑΖΗΤΗΣΗ",fg="blue")
    entry1=tkinter.Entry(rootD)
    DeleteB=tkinter.Button(rootD,text="DELETE",command=Delete_button)
    headD.pack()
    entry1.pack()
    DeleteB.pack()
    rootD.mainloop()

##variables for update

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

def up1():
    global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
    conn.cursor()
    u1 = pat_ID.get()
    u2 = pat_name.get()
    u3 = pat_sex.get()

    conn = sqlite3.connect("MDBA.db")
    p = list(conn.execute("Select * from PATIENT where PATIENT_ID=?", (u1,)))
    if len(p) != 0:
        conn.execute('UPDATE PATIENT SET NAME=?,SEX=?  where PATIENT_ID=?', (u1, u2, u3 ))
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "ΤΑ ΔΕΔΟΜΕΝΑ ΕΝΗΜΕΡΟΘΗΚΑΝ")
        conn.commit()

    else:
        tkinter.messagebox.showinfo("MEDANTA DATABSE SYSTEM", "Ο ΑΣΘΕΜΗΣ ΔΕΝ ΕΧΕΙ ΕΓΓΡΑΦΕΊ")

labelu=None
bu1=None

def EXITT():
    rootU.destroy()

##-----PATIENT UPDATE SCREEN -----##
def P_UPDATE():
    global pat_address, pat_BG, pat_contact, pat_contactalt, pat_CT, pat_dob, pat_email, pat_ID, pat_name, pat_sex
    global rootU, regform, id, name, dob, sex, email, ct, addr, c1, c2, bg, SUBMIT, menubar, filemenu, p1f, p2f,HEAD
    rootU = tkinter.Tk()
    rootU.title("UPDATE WINDOW")
    menubar = tkinter.Menu(rootU)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="NEW", command=P_UPDATE)
    filemenu.add_separator()
    filemenu.add_command(label="EXIT", command=EXITT)
    rootU.config(menu=menubar)
    menubar.add_cascade(label="File", menu=filemenu)
    HEAD=tkinter.Label(rootU,text="ΠΡΟΣΘΗΚΗ ΔΕΔΟΜΕΝΩΝ ΓΙΑ ΕΠΕΞΕΡΓΑΣΙΑ",bg='black',fg='white')
    id = tkinter.Label(rootU, text="ΑΜΚΑ")
    pat_ID = tkinter.Entry(rootU)
    name = tkinter.Label(rootU, text="ΟΝΑΜΑ ΑΣΘΕΝΗ")
    pat_name = tkinter.Entry(rootU)
    sex = tkinter.Label(rootU, text="ΑΣΦΑΛΙΣΗ")
    pat_sex = tkinter.Entry(rootU)
    SUBMIT=tkinter.Button(rootU,text="ΥΠΟΒΟΛΗ",command=up1)
    HEAD.pack()
    id.pack()
    pat_ID.pack()
    name.pack()
    pat_name.pack()
    sex.pack()
    pat_sex.pack()
    SUBMIT.pack()
    rootU.mainloop()
