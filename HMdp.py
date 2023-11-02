import sqlite3
conn=sqlite3.connect("MDBA.db")
print("DATABASE CONNECTION SUCCESSFUL")


conn.execute("Drop table if EXISTS PATIENT")
conn.execute("Drop table if EXISTS CONTACT_NO")
conn.execute("Drop table if EXISTS ROOM")
conn.execute("Drop table if EXISTS TREATMENT")
conn.execute("Drop table if EXISTS MEDICINE")
conn.execute("Drop table if EXISTS employee")

conn.execute("""CREATE table PATIENT
           (PATIENT_ID int(10) primary key,
           NAME VARCHAR(20) not null,
          SEX varchar(10) not null
             )""")
print("TABLE CREATED SUCCESSFULLY")

 

conn.execute("""CREATE table ROOM
            (PATIENT_ID int(10)not NULL ,
             ROOM_NO varchar(20) PRIMARY KEY ,
             farmaka varchar(10) not null,
             disease varchar(20) not null,
             DATE_ADMITTED date,
             outcome varchar(40) NULL,
             FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
             );
            """)
print("TABLE CREATED")

conn.execute("""CREATE TABLE TREATMENT
            (PATIENT_ID int(10) primary key,
             TREATMENT varchar(100) not null,
             TREATMENT_CODE varchar(30) not null,
             T_COST int(20) not null,
            FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
             """)
print("TREATMENT CREATED")

conn.execute("""CREATE TABLE MEDICINE
            (PATIENT_ID int(10) primary key,
             MEDICINE_NAME varchar(100) not null,
             M_COST int(20) not null,
             M_QTY int(10) not null,
             FOREIGN KEY(PATIENT_ID) REFERENCES PATIENT(PATIENT_ID));
             """)
#print("MEDICINE CREATED")

conn.execute("""CREATE table employee
            (PATIENT_ID varchar(10) not null,
             EMP_NAME  DECIMAL(10,3) not null,
             SEX DECIMAL(10,3) not null,
             AGE DECIMAL(10,3) not null,
             DESIG DECIMAL(10,3) not null,
             SAL DECIMAL(10,3) not null,
             EXP DECIMAL(10,3) not null,
             EMAIL DECIMAL(10,3) not null,
             PHONE DECIMAL(10,3) not null,
             idapo DECIMAL(10,3) not null,
             MERA DATE not null,
             muoar DECIMAL(10,3) not null,
             uperari  DECIMAL(10,3) not null,
             presvar DECIMAL(10,3) not null,
             piesiar DECIMAL(10,3) not null,
             astar DECIMAL(10,3) not null,
            FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
)""")
print ("EMPLOYEE CREATED")

conn.execute("DROP TABLE if EXISTS appointment")
conn.execute("""CREATE table appointment
            (
             PATIENT_ID int(20) not null,
             AP_NO varchar(10) ,
             AP_TIME time,
             AP_DATE date,
             description varchar(100),
             foreign key(PATIENT_ID) references patient(PATIENT_ID)
            );""")

print("APPOINTMENT CREATED")