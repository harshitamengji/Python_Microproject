import MySQLdb

try:

    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stationary")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="alter table statinaryproduct add company varchar(50)"
    cur.execute(query)
    print("execute query")
    mycon.commit()
    print(query+"table altered .... ")
except:
    print("table altered...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()
    print("DB connection") 