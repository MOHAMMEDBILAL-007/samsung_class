import pymysql
def connectdb():
    try:
        connection = pymysql.connect(host="localhost",user ="root",password="Bilal1234#",database="samsung",port=3306,charset="utf8")
        print("database connected")
    except:
        print("database couldn't connect")
    return connection
def disconnetdb(connection):
    try:
        connection.close
        print("data base disconnected")
    except:
        print("disconnection failed")
def createdb():
    query = 'create data base if not exist samsung'
    connection =connectdb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("data base created")
        cursor.close()
        disconnetdb(connection)
    except:
        print("database creation failed")
def create_tabl():
    query = 'create table executive(exe_id varchar(5) primary key,exe_name varchar(20),position varchar(10),salary int)'
    connection = connectdb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnetdb(connection)
    except:
        print('Table creation failed')
def read_all_employees():
    query = 'select * from executive'
    connection = connectdb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('All rows retrived')
        cursor.close()
        disconnetdb(connection)
    except:
        print('Rows retrival failed')
def read_input():
    exe_id =input("enter your id:")
    exe_name=input("enter your name:")
    position = input("enter your position in the company:")
    salary =int(input("enter your salary:"))
    return (exe_id,exe_name,position,salary)
def insert():
    employee = read_input()
    quary = "insert into executive(exe_id,exe_name,position,salary) value(%s,%s,%s,%s)"
    try:
        connection=connectdb()
        cursor=connection.cursor()
        value = cursor.execute(quary,employee)
        connection.commit()
        cursor.close()
        disconnetdb(connection)
        if value == 1:
            print("row inserted")
        else:
            print("row insertion failed")
    except:
        print("insertion failed")

connection=connectdb()
insert()
read_all_employees()
disconnetdb(connection)