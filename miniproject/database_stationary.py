import MySQLdb

try:
    query="CREATE DATABASE STATIONARY "
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")

    cur.execute(query)
    print("execute query")
    mycon.commit()
    print(query+"table created .... ")
except:
    print("table not created...")
finally:
    cur.close()
    print("cursor connection close....")
    mycon.close()