import sqlite3
conn = sqlite3.connect('new.db')    #connects to new.db
#executes sql
# conn.execute("CREATE TABLE reminder(ID INT PRIMARY KEY ,rdate  TEXT    NOT NULL, rtime TEXT NOT NULL,notification text NOT NULL );")
#prepared query
conn.execute('insert into reminder values(?,?,?,?);',(1,'2000-3-12','12:00:00','Birthday'))
# conn.execute('insert into company values(3,"b");')
#saves changes in the db
conn.commit()
#select statment returns the values
c=conn.execute("select * from reminder")
# print c
for i in c:     #values are iterated
    print i[0] ,' ', i[1],' ',i[2],' ',i[3]#i is every object,i[0] is 1st column and i[1] 2nd
# rid=input("id:")
# conn.execute("delete from reminder")
# conn.commit()