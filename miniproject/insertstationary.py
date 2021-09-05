import MySQLdb

try:
    query="create table statinaryproduct(name varchar(100),price int(50))"
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="stationary")
    print("mycon excecute")
    cur=mycon.cursor()
    print("cursor excecute")
    query="insert into statinaryproduct values('Stickynotes','50') "
    query="insert into statinaryproduct values('Notebook','75') "
    query="insert into statinaryproduct values('Studytable','800') "
    query="insert into statinaryproduct values('Eraser','10') "
    query="insert into statinaryproduct values('Craftpaper','30') "
    query="insert into statinaryproduct values('Pens','10') "
    query="insert into statinaryproduct values('Pencils','5') "
    query="insert into statinaryproduct values('Diaries','200') "
    query="insert into statinaryproduct values('Compassbox','150') "
    query="insert into statinaryproduct values('Colourbox','300') "
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