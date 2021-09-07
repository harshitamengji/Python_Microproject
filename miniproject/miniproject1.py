import MySQLdb
def exit1():
    print("============THANK YOU..! VISIT AGAIN...!\U0001f607============")

    exit()

def menu():
    print("\t\t---------------------------")
    print("\t\t||P-code|Product   ||Rate||")
    print("\t\t---------------------------")
    print("\t\t||111   |Java      ||  200||")
    print("\t\t||222   |C-lang    ||  220||")
    print("\t\t||333   |Python    ||  200||")
    print("\t\t||444   |Data&Algo ||  200||")
    print("\t\t||555   |OPSY      ||  210||")
    print("\t\t---------------------------")
menu()
def database():
    print("")
    print("**Welcome to the BOOKSHOP*")
    try:
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="bookstore")
            query="SELECT * FROM books_info"
            cur=mycon.cursor()
            cur.execute(query)
            tdata=cur.fetchall()
            print(" \n Types of Books are: ")
            print("Id: ","\tRate: ","\t\tName : ")
            for row in tdata:
                print(row[0],"","\t",row[2],"\t  ",row[1])
            print("--------------------------------------------")  
            print("--------------------------------------------")    
  

    except:
            print("Error")

    finally:
            mycon.commit()
            cur.close()

    ch=int(input("\nEnter your choice "))
    print("")
    print("----------------------------------------------------")

    if ch==11:
        print("------------EXIT-------------")


    while (ch!=11):

        if ch==1:
            menu()

            x1 = 200
            print("\nYou have selected JavaBook")
            print("Price is ",x1)
            a1 = int(input("Enter number of books:"))
            print("Total Amount: ",a1 * x1)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                
                exit1()
            break


        if ch==2:
            menu()

            x2 = 220
            print("\nYou have selected C_programming Book")
            print("Price is ",x2)
            a2 = int(input("Enter number of books:"))
            print("Total Amount: ",a2 * x2)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==3:
            menu()

            x3 = 200
            print("\nYou have selected python Book ")
            print("Price is ",x3)
            a3 = int(input("Enter number of books:"))
            print("Total Amount: ",a3 * x3)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==4:
            menu()
            x4 = 200
            print("\nYou have selected Data_structure Book")
            print("Price is ",x4)
            a4 = int(input("Enter number of books:"))
            print("Total Amount: ",a4 * x4)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                exit1()
            break

        if ch==5:
            menu()

            x5 = 210
            print("\nYou have selected operating_system Book")
            print("Price is ",x5)
            a5 = int(input("Enter number of books:"))
            print("Total Amount: ",a5 * x5)
            b1 = int(input("Press 1 to continue \nPress 2 to exit: "))
            if(b1 == 1):
                database()
            if(b1 == 2):
                
                exit1()       
            break
        print("============THANK YOU..! VISIT AGAIN...!============")

        

database()


exit1()