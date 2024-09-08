import random
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd='mysql',database='realproject')
if mycon.is_connected()==False:
    print('Error connecting to MySQL database')
cursor=mycon.cursor()

def pin__check(a):
         cursor.execute("select account_type from bankdetails where account_no= {}".format(a))
         data=cursor.fetchall()

         if data==[]:
             print('Account does not Exist!')
             f='access denied'
             return f
         
         if data==[('locked',)]:
             print('Please Contact BANK Since Account is Locked!')
             f='access denied'
             return f
         else:
            for d in range(3):
              b=int(input('Enter pin no :  '))
              cursor.execute("select pin from bankdetails where account_no= {}".format(a))
              data=cursor.fetchall()
              
              if [(b,)]==data:
                    f='access granted'
                    return f                  
                    break
              else:
                    print('INCORRECT PIN')
            else:       
              cursor.execute("update bankdetails set account_type = 'locked' where account_no = {}".format(a))
              mycon.commit()
              print('Account has been Locked')
              f='access denied'
              return f
    

def withdraw(a):
    try :
        
         print('Select 1 for Withdraw')
         print('Select 2 for Deposit')
         s=input('Enter value :  ')
         if s=='1':
            b=int(input('Enter amount to Withdraw :  '))
            cursor.execute("select amount from bankdetails where account_no = {}".format(a))
            d=cursor.fetchone()
            d=d[0]
            if d<b:
                print('INSUFFICIENT BALANCE!')
            else:
                cursor.execute("update bankdetails set amount = amount-{} where account_no = {}".format(b,a))
                mycon.commit()
            
                search(a)
         elif s=='2':
            b=int(input('Enter amount to deposit :  '))
            cursor.execute("update bankdetails set amount = amount+{} where account_no = {}".format(b,a))
            mycon.commit()
            
            search(a)   
         else:
             print('Wrong Choice')
               
    except ValueError:
        print('Numeric Values only')
        

def new_account():
            print('Fill these details to register your account ')
            name=input("Enter your name        :")		           
            s=input("Enter your address     :")
            p=input("Enter your phone number:") 
            t=input("Enter account type     :")
            
            pin=random.randint(1000,9999)
            try:
                amt=int(input("Enter amount           :")

                while True:
                    
                        cursor.execute("select account_no from bankdetails")
                        data=cursor.fetchall()
                        ano=random.randint(100000,999999)
                        
                        if (ano,) not in data:
                            
                            print('\nACCOUNT NO is ',ano)
                            print('\nPIN is ',pin)
                            cursor.execute("insert into bankdetails values({},'{}',{},{})".format(ano,t,amt,pin))
                            mycon.commit()
                            cursor.execute("insert into cust values({},'{}','{}','{}')".format(ano,name,s,p))
                            mycon.commit()
                            print("\n\nNEW ACCOUNT is opened SUCCESSFULLY")
                            search(ano)
                            break
                        
            except ValueError:
                print('Numeric Vales Only!')

def reset(a):
    
         cursor.execute("select account_type from bankdetails where account_no= {}".format(a))
         data=cursor.fetchall()
         cursor.execute("select account_no from bankdetails where account_no= {}".format(a))
         d=cursor.fetchall()
         
         if data==[('locked',)]:
             print('Please Contact Bank Since Account is Locked')
             
         elif d!=[]:
             name=input('Enter full name    : ')
             address=input('Enter Address      : ')
             phone=input('Enter Phone Number : ')
             cursor.execute("select cname,phone,address from cust where account_no= {}".format(a))   
             data=cursor.fetchall()
             
             if data[0][0].upper()==name.upper() and data[0][1]==phone and data[0][2].upper()==address.upper():
                 print('RESET ACTIVATED')
                 pin=random.randint(1000,9999)
                 print('NEW PIN IS:   ',pin,'\n\n\n')
                 cursor.execute("update bankdetails set pin = {} where account_no = {}".format(pin,a))
                 mycon.commit()
                 search(a)
             else:
                 print('wrong details entered'.upper())
         else:
             print('ACCOUNT NUMBER does not EXIST!')

def display(p):
    if p=='101920':
        cursor.execute("select * from cust,bankdetails where cust.account_no=bankdetails.account_no")
        row=cursor.fetchall()
        count=cursor.rowcount
        print("The number of rows retrieved from resultset:",count)
        for line in row :
            print(line,'\n')
    else:
         print("Wrong Password")
       

def update(a):
    print("1.to update NAME")
    print("2.to update ADDRESS")
    print("3.to update PHONE NO.")
    print("4.to update ALL OF THE ABOVE")
    n=input("Choose your option:")
    
    if n=='1':
            m=input("Enter NEW NAME:")
            
            cursor.execute("update cust set  cname='%s' where account_no='%s'"%(m,a))
            mycon.commit()
            print("Update is Successful\n\n")
            search(a)
    elif n=='2':
            d=input("Enter NEW ADDRESS:")
            
            cursor.execute("update cust set address='%s' where account_no='%s'"%(d,a))
            mycon.commit()
            print("Update is Successful\n\n")
            search(a)
    elif n=='3':
            p=input("Enter NEW PHONE NO:")
            
            cursor.execute("update cust set phone='%s'where account_no='%s'"%(p,a))
            mycon.commit()
            print("Update is Successful\n\n")
            search(a)
   
    elif n == '4':
       
       nme=input("Enter NEW NAME     :")
       add=input("Enter NEW ADDRESS  :")
       phn=input("Enter NEW PHONE NO :")
       cursor.execute("update cust set cname='%s',address='%s',phone='%s' where account_no='%s'"%(nme,add,phn,a))
       mycon.commit()
       print("Update is Successful\n\n")
       search(a)

    else:
            print("Wrong Choice")


def transfer(x):
    try: 
        amt=int(input("Amount to be transferred: "))
        y=int(input("Account no of person     : "))
        cursor.execute("select account_no from bankdetails where account_no= {}".format(y))   
        data=cursor.fetchall()
        cursor.execute("select amount from bankdetails where account_no= {}".format(x))
        d=cursor.fetchone()
        d=d[0]
        if d<amt:
            print('INSUFFICIENT BALANCE')
        else:
                    
                if data!=[]:
                  
                        cursor.execute("UPDATE bankdetails SET AMOUNT=AMOUNT-'%s' WHERE ACCOUNT_NO='%s' " %(amt, x))
                        cursor.execute("UPDATE bankdetails SET AMOUNT=AMOUNT+'%s' WHERE ACCOUNT_NO='%s' " %(amt, y))
                        cursor.execute("SELECT NOW()")
                        m=cursor.fetchall()
                        d=m[0][0]
                        mycon.commit()
                        y=str(y)
                        print("You have successfully transferred", amt, "rupees to", y[0] + 'x'*(len(y)-2) +y[-1], "on", d) 
                        
                        print("Transaction successful".upper(),'\n\n\n')
                        search(x)
                
                else: 
                    print('ACCOUNT NUMBER does not EXIST')         
    except ValueError:
            print("Enter Numeric Values only")

def search(a):
    
             cursor.execute("select * from cust, bankdetails WHERE bankdetails.account_no='%s' and bankdetails.account_no=cust.account_no" %(a,))
             profile=cursor.fetchone()
             print('BANK DETAILS ARE:   \n')
             print('Customer name is         :',profile[1])
             print('Customer address is      :',profile[2])
             print('Customer Phone number is :',profile[3])
             print('Customer ID is           :',profile[0])
             print('Account type is          :',profile[5])
             print('Amount in account is     :',profile[6],'Rs')

def delete(a):
        cursor.execute("delete from cust where account_no='%s'"%(a,))
        cursor.execute("delete from bankdetails where account_no='%s'"%(a,))
        mycon.commit()
        print('ACCOUNT DELETED')
   
while True:
  print('\n\n\n')
  print('               $$Welcome to SILVER COIN$$  \n')
  
  print('________________________________________________________')
  print('|                                                       |')
  print('|......................MAIN MENU........................|\n|                                                       |\n|                                                       |\n|                                                       |')
  print('|    1 for Customer Menu                                |')
  print('|    2 for Forgot PIN                                   |')
  print('|    3 for Employee Options                             |')
  print('|    4 for Opening New Account                          |')
  print('|    5 to EXIT                                          |')
  print('|_______________________________________________________|')
  print('\n\n\n')
  ch=input('Enter your Choice    :  ')
  
  if ch=='1':
     a=input('Enter account number :   ')
     if pin__check(a)=='access granted':
         while True:           
             print('\n\n\n')                                                    
             print('_________________________________________________________')
             print('|                                                        |')
             print('|....................CUSTOMER MENU.......................|\n|                                                        |\n|                                                        |\n|                                                        |')
         
             print('|    1 to WITHDRAW or DEPOSIT money                      |')
             
             print('|    2 to VIEW bank details                              |')
             print('|    3 to TRANSFER money                                 |')
             print('|    4 to UPDATE customer details                        |')
             print('|    5 to DELETE Account                                 |')
             print('|    6 to GO BACK to MAIN MENU                           |')
             print('|________________________________________________________|')
             ch=input('Enter your Choice :   ')
             if ch=='1':
                 withdraw(a)

             elif ch=='2':
                    search(a)
             elif ch=='3':
                    transfer(a)
             elif ch=='4':
                    update(a) 
             elif ch=='5':
                 ch=input('Are you sure you want to DELETE ACCOUNT? <y/n>')
                 if ch.upper()=='Y':
                     
                     delete(a)
                     break
             elif ch=='6':
                    break
             else:
                    print('Wrong Choice')
  elif ch=='2':
      try:
          a=int(input('Enter Account Number :  '))
          reset(a)
      except ValueError:
          print('Enter Numeric Values Only!')
          
  elif ch=='3':
        ef=input('Do you want to view all files <y/n> :   ')
        if ef=='y':
            p=input('Enter the password                  :  ')
            display(p)
        gh=input('Do you want to search with CUSTOMER ID? <y/n> :')
        if gh =='y':
            b=input('Enter Account no :  ')
            search(b)
  elif ch=='4':
      new_account()
          
  elif ch=='5':
      break
  else:
      print('Wrong Choice')
