import mysql.connector as a
con = a.connect(host='localhost',user='root', password='mysql@123', database='podar')
def ast():
    n=input("Student Name:")
    c=input("Class Name:")
    r=input("Roll No:")
    a=input("Adress:")
    p=input("Phone:")
    data=(n,c,r,a,p)
    sql='insert into students values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data entered successfully")
    print(">-----------------------------------------<")
    main()

def stop():
    exit()
    main()

def main():
    print("""
1.ADD STUDENT
0.STOP PROGRAM
""")
    choice=input("Enter Task No: ")
    print(">---------------------<")
    if (choice=='1') :
        ast()
    elif (choice=='0') :
        print("STOP")
        stop()
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
        



