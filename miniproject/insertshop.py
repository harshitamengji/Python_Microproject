import MySQLdb

try:
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="bookstore")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="insert into books_info values('1','javaBook','200') "
    query="insert into books_info values('2','C_programming Book','220') "
    query="insert into books_info values('3','python Book','200') "
    query="insert into books_info values('4','Data_structure Book','200') "
    query="insert into books_info values('5','operating_system Book','210') "




    



    
    cur.execute(query)
    print("execute query")
    mycon.commit()
    print(query+"sucessfully inserted values in table.... ")
except:
    print("values inserted...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection")