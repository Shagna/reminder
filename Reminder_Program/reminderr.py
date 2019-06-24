import time
import sqlite3
conn = sqlite3.connect('new.db')                                          #database connection
c=1

while c:
    choice=input("1.Add reminder\n2.Edit reminder\n3.View Memo\n4.Delete")
    print "-------------------------------------------------------------------------------------------------------------"

    if choice==1:
        print "Add Reminder:\n"                                          # creating memo with date time and memo

        date_entry = raw_input("Enter the date (YYYY-MM-DD):")
        time_entry = raw_input("Enter the time (HH-MM-SS):")
        notification = raw_input("Enter memo:")
        p=''
        v=conn.execute("select max(id) from reminder")                  #autoincrement table id (unique field)
        for i in v:
           p= int(i[0])
        p+=1
        conn.execute('insert into reminder values (?,?,?,?);',(p,date_entry,time_entry,notification))
        conn.commit()
        a = raw_input("Do you want to continue (Y/N)?")
        if a == "Y":
            c = 1
        else:
            c = 0
        # choice = input("1.Add reminder\n2.Edit reminder\n3.View Notifications\n4.Exit")
        print "---------------------------------------------------------------------------------------------------------"
    elif choice==2:
        print "Edit Reminder:"                                              #update reminders

        rid = input("Choose your reminder id:")
        r_date=raw_input("Enter date:")
        r_time=raw_input("Enter time:")
        r_notifivation=raw_input("Enter memo:")
        conn.execute("update reminder set rdate=?,rtime=?,notification=? where id=?", (r_date,r_time,r_notifivation,rid))
        conn.commit()
        a = raw_input("Do you want to continue (Y/N)?")
        if a == "Y":
            c = 1
        else:
            c = 0
        print "---------------------------------------------------------------------------------------------------------"
    elif choice==3:
        print "View Memo:"                                              #view all reminders

        c = conn.execute("select * from reminder")
        for i in c:  # values are iterated
            print str(i[0]), '   ', i[1], '   ', i[2], '   ', i[3]
        a = raw_input("Do you want to continue (Y/N)?")
        if a == "Y":
            c = 1
        else:
            c = 0
        print "---------------------------------------------------------------------------------------------------------"
    elif choice == 4:
        print "Remove Reminder:"                                        #removing reminders

        rid = raw_input("Choose your reminder:")
        int(rid)
        conn.execute("delete from reminder where id=?", (rid))
        print "Removed.."
        a = raw_input("Do you want to continue (Y/N)?")
        if a == "Y":
            c = 1
        else:
            c = 0
        print "---------------------------------------------------------------------------------------------------------"
    else:
         print "Exiting.."
         break                                                          #exit from while
        
 # here we can write the code for realtime notification


