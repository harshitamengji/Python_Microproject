import MySQLdb

try:
    query="create table statinaryproduct(name varchar(100),price int(50))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stationary")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="update statinaryproduct set company='Yuva'where name='Stickynotes'"
    query="update statinaryproduct set company='Classmate'where name='Notebook'"
    query="update statinaryproduct set company='NARGO'where name='Studytable'"
    query="update statinaryproduct set company='apsara'where name='Eraser'"
    query="update statinaryproduct set company='navneet'where name='Craftpaper'"
    query="update statinaryproduct set company='Reynolds'where name='Pens'"
    query="update statinaryproduct set company='Camlin'where name='Pencils'"
    query="update statinaryproduct set company='Camel'where name='Compassbox'"
    query="update statinaryproduct set company='Camel'where name='Colourbox'"
    cur.execute(query)
    print("excecute excecute")
    mycon.commit()
    print(query+"sucessfully fired.....")
except:
    print("table not created...")
finally:
    cur.close()
    print("cursor connection close...")
    mycon.close()
    print("DB connection close...")

