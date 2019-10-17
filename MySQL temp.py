# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print('Hello')
a=5
print(5-a)
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE newtemp")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='123456',
        database='newtemp')
mycursor = mydb.cursor()
mycursor.execute('create table cust (id int, name varchar(255), address varchar(255))')
mycursor.execute('show tables')
for x in mycursor:
  print(x)
mycursor.execute('alter table cust drop column id')
mycursor.execute('alter table cust add column id int auto_increment primary key')
sql = 'insert into cust (name,address) values (%s,%s)'
val = ('John','Highway 21')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, 'record inserted')
val2 = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')
        ]
mycursor.executemany(sql,val2)
mydb.commit()
print(mycursor.rowcount, 'records inserted')
mycursor.execute('select * from cust')
print(mycursor.fetchall())
mycursor.execute('select * from cust')
result = mycursor.fetchall()
for x in result:
    print(x)
mycursor.execute('select * from cust')
result2 = mycursor.fetchone()
for x in result2:
    print(x)
mycursor.execute('Select name, address from cust')
result3 = mycursor.fetchall()
for y in result3:
    print(y)
mycursor.execute('select * from cust where id > 3')
result4 = mycursor.fetchall()
for z in result4:
    print(z)
addr = ('Mountain 21',)
sql2 = 'select * from cust where address = %s'
mycursor.execute(sql2,addr)
result5 = mycursor.fetchall()
for a in result5:
    print(a)
mycursor.execute('select * from cust order by name')
result6 = mycursor.fetchall()
for b in result6:
    print(b)
mycursor.execute('show create table cust')
print(mycursor.fetchall())
sql3 = 'delete from cust where address = %s'
adr = ('Sideway 1633',)
mycursor.execute(sql3,adr)
mydb.commit()
print(mycursor.rowcount, 'record deleted')
sql4 = "update cust set address = 'Canyon 123' where address = 'Valley 345'"
mycursor.execute(sql4)
mydb.commit()
print(mycursor.rowcount, 'record(s) affected')
sql5 = "select * from cust where address like '%way%'"
mycursor.execute(sql5)
res7 = mycursor.fetchall()
for c in res7:
    print(c)
sql6 = 'select * from cust limit 5 offset 2'
mycursor.execute(sql6)
res8 = mycursor.fetchall()
for d in res8:
    print(d)
mycursor.execute('create table users (user_id int auto_increment primary key, name varchar(255), fav int)')
mycursor.execute("insert into users (name,fav) values('John',154)")
mydb.commit()
mycursor.execute('select * from users')
print(mycursor.fetchall())
mycursor.execute("insert into users (name,fav) values('Peter',154)")
mydb.commit()
mycursor.execute("insert into users (name,fav) values('Amy',155)")
mydb.commit()
mycursor.execute("insert into users (name) values('Hannah')")
mydb.commit()
mycursor.execute("insert into users (name) values('Michael')")
mydb.commit()
mycursor.execute('select * from users')
res = mycursor.fetchall()
for f in res:
    print(f)
mycursor.execute('create table products (p_id int primary key, name varchar(255))')
mycursor.execute("insert into products (p_id,name) values(154,'Chocolate')")
mydb.commit()
mycursor.execute("insert into products (p_id,name) values(155,'Lemon')")
mydb.commit()
mycursor.execute("insert into products (p_id,name) values(156,'Vanilla')")
mydb.commit()
mycursor.execute('select * from products')
print(mycursor.fetchall())
sql8 = 'Select users.name as User, products.name as Favorite from users inner join products on users.fav = products.p_id'
mycursor.execute(sql8)
res0 = mycursor.fetchall()
for p in res0:
    print(p)
sql9 = 'Select users.name as User, products.name as Favorite from users left join products on users.fav = products.p_id'
mycursor.execute(sql9)
res2 = mycursor.fetchall()
for g in res2:
    print(g)
sql10 = 'Select users.name as User, products.name as Favorite from users right join products on users.fav = products.p_id'
mycursor.execute(sql10)
res3 = mycursor.fetchall()
for h in res3:
    print(h)