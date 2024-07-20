import mysql.connector as a
con = a.connect(host='localhost',user='root', password='mysql@123', database='podar1')
def ast():
    n=input("Student Name: ")
    c=input("Class Name: ")
    r=input("Roll No: ")
    a=input("Adress: ")
    p=input("Phone: ")
    data=(n,c,r,a,p)
    sql='insert into students values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data entered successfully")
    print(">-----------------------------------------<")
    main()

def rst():
    c=input("Class Name: ")
    r=input("Roll No: ")
    data=(c,r)
    sql='DELETE FROM students WHERE Classname=%s and Rollno=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------<")
    main()
    
def addt():
    n= input("Teacher: ")
    p= input("Post: ")
    s= input("Salary: ")
    a= input("Address: ")
    ph= input("Phone: ")
    ac=input("Account: ")
    data=(n,p,s,a,ph,ac)
    sql='insert into teachers values (%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print ("Data entered Successfully")
    print(">-----------------------------------------<")
    main()

def remt():
    n=input("Teacher : ")
    ac=input("Account : ")
    data=(n,ac)
    sql='DELETE FROM teachers WHERE Teacher=%s and Account=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print ("Data Updated")
    print(">-----------------------------------------<")
    main()

def abclass():
    d=input("Date: ")
    cl= input("Class: ")
    ab= input("Names of Absent Students: ")
    data=(d,cl,ab)
    sql='insert into Cattendance values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------<")
    main()

def acteacher():
    d=input("Date :")
    ab=input("Names of Absent Teacher: ")
    data=(d,ab)
    sql='insert into Tattendance values (%s, %s)'
    c=con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------<")
    main()

def submitf():
    n=input("Student Name: ")
    c=input("Class Name: ")
    x=input("Roll No: ")
    m=input("Month: ")
    y=input("Year: ")
    f=input("Fees: ")
    d=input("Date: ")
    data=(n,c,x,m,y,f,d)
    sql='insert into Fees values (%s,%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered successfully")
    print(">-----------------------------------------<")
    main()

def pays():
    n=input("Teacher Name: ")
    m=input("Month: ")
    p=input("Yes/No: ")
    data=(n,m,p)
    sql='insert into Salary values (%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print ("Data Entered Successfully")
    print(">-----------------------------------------<")
    main()
    
def dclass():
    sql='select*from Students'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print ("Name:",i[0])
        print ("Class: ",i[1])
        print("Roll: ",i[2])
        print("Address: ",i[3])
        print("Phone: ",i[4])
        print(">-----------------------------------------<")
    print(">-----------------------------------------<")    
    main()

def dteacher():
    sql='select*from Teachers'
    c=con.cursor()
    c.execute (sql)
    d=c.fetchall ()
    for i in d:
        print("Name:",i[0])
        print("post:",i[1])
        print("salary:",i[2])
        print("Address : ",i[3])
        print("Phone: " ,i[4])
        print("AccountNo: ",i[5])
        print(">-----------------------------------------<")
    print(">-----------------------------------------<")    
    main()

def main():
    print("""                        Podar International School


                        1. ADD STUDENT             2. REMOVE STUDENT
                        3. ADD TEACHER             4. REMOVE TEACHER
                        5. CLASS ATTENDANCE        6. TEACHER ATTENDANCE
                        7. SUBMIT FEES             8. PAY SALARY
                        9. DISPLAY CLASS           10. TEACHER LIST
""")
    choice=input("Enter Task No: ")
    print(">---------------------<")
    if (choice=='1') :
        ast()
    elif (choice=='2') :
        rst()
    elif (choice=='3') :
        addt()
    elif (choice== '4') :
        remt()
    elif (choice=='5') :
        abclass()
    elif (choice=='6') :
        acteacher()
    elif (choice=='7') :
        submitf()
    elif (choice=='8') :
        pays()
    elif (choice =='9') :
        dclass()
    elif (choice=='10') :
        dteacher()
    else:
        print("Wrong Choice")
        main()

def pswd():
    p=input("Password : ")
    if p=="root":
        main()
    else:
        print ("Wrong Password")
        pswd()
pswd()




















    
