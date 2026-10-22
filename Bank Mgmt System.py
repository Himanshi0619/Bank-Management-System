#------------------------BANK MANAGEMENT SYSTEM------------------------

import mysql.connector as a
con=a.connect(host="localhost",user="root",password="237081f",database="atm")


#FOR OPENING A NEW ACCOUNT

def openAccount():
    n=input("Enter Name : ")
    ac=input("Enter Account Number : ")
    db=input("Enter D.O.B. [YYYY/MM/DD] : ")
    ob=int(input("Enter Opening Balance : "))
    data1=(n,ac,db,ob)
    data2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("\n","-"*30,"DATA ENTERED SUCCESSFULLY!","-"*30)
    main()


#FOR DEPOSTING AMOUNT

def depositAmt():
    am=int(input("Enter Amount to Deposit : "))
    ac=input("Enter Account Number : ")
    a="select currentBalance from amount where accountNo=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set currentBalance=%s where accountNo=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("\n","-"*30,"AMOUNT DEPOSITED SUCCESSFULLY!!","-"*30)
    main()

#FOR WITHDRAWING AMOUNT

def withdrawAmt():
    am=int(input("Enter Amount : "))
    ac=input("Enter Account Number : ")
    a="select currentBalance from amount where accountNo=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql="update amount set currentBalance=%s where accountNo=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("\n","-"*30,"AMOUNT WITHDRAWN SUCCESSFULLY!!","-"*30)
    main()


#FOR CHECKING THE BALANCE IN ACCOUNT

def balance():
    ac=input("Enter Account Number : ")
    a="select currentBalance from amount where accountNo=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("balance for account:",ac,"is",myresult[0])
    main()


#FOR DISPLAYING ACCOUNT HOLDER'S INFORMATION

def displayAccount():
    ac=input("Enter Account Number : ")
    a="select * from account where accountNo=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("\nNAME, ACCOUNT NUMBER, DATE OF BIRTH, OPENING BALANCE")
    for i in myresult:
        print(i,end=" ")
    main()

#FOR CLOSING/DELETING AN ACCOUNT

def closeAccount():
    ac=input("Enter Account Number : ")
    sql1="delete from account where accountNo=%s"
    sql2="delete from amount where accountNo=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    print("\n","-"*30,"ACCOUNT CLOSED!!","-"*30)
    main()


#MAIN SCREEN

def main():
    print("\n","-" * 30,"BANK MANAGEMENT SYSTEM","-" * 30)
    print("\nENTER 1 TO OPEN NEW ACCOUNT")
    print("\nENTER 2 TO DEPOSIT AMOUNT")
    print("\nENTER 3 TO WITHDRAW AMOUNT")
    print("\nENTER 4 FOR BALANCE ENQUIRY")
    print("\nENTER 5 TO DISPLAY CUSTOMER DETAILS")
    print("\nENTER 6 TO CLOSE AN ACCOUNT")
    print("\nENTER ANY NO TO EXIT")

    choice=input("\nENTER TASK NUMBER : ")

    if (choice=='1'):
        openAccount()
    elif (choice=='2'):
        depositAmt()
    elif (choice=='3'):
        withdrawAmt()
    elif (choice=='4'):
        balance()
    elif (choice=='5'):
        displayAccount()
    elif (choice=='6'):
        closeAccount()
    else:
        print("\nTHANK YOU")
        print("\nHAVE A GOOD DAY")

main()
