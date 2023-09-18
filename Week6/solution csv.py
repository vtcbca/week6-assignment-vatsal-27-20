import sqlite3 as sq
conn=sqlite3.connect("c://sqlite//result.db")
q="create table result 
(sid int primary key, sname text,marks1 int,marks2 int,marks3 int,marks4 int,marks5 int)"
cur=conn.cursor()
cur.execute(q)
conn.commit()

# insert record into table 

q1= "insert into result values(1,'hardik',67,45,58,90,45),(2,'nikhil',56,34,56,78,45),(3,'bitu',67,76,83,50,54),(4,'prince',50,67,78,89,45),(5,'yuvraj',45,67,78,50,78),(6,'ankit',60,65,64,50,43),(7,'rohan',56,45,44,78,36),(8,'smit',56,67,45,49,50),(9,'rachit',46,62,43,39,57),(10,'anay',67,64,54,56,78)"
cur1=conn.cursor()
cur1.execute(q1)
conn.commit()

# dump result table to result.csv

.header on
.mode csv
.output result.csv
select * from result
.quit

#Read result.csv file and Print Total Marks and Grade of each student. 
 Also Append Total Marks and Grade column into result.csv file.

import csv 
with open("c://sqlite//result.csv","r") as f:
    data=csv.reader(f)
    list1=[]
    header=next(data)
    header.append["Totalmarks","Grade"]
    list1.append(header)
    for i in data:
        sid,sname,*marks=i
        total=sum(int,marks)
        if total>=400:
            Grade='A'
        elif total>=300:
            Grade='B'
        elif total>=200:
            Grade='C'
        elif total>=150:
            Grade='D'
        elif total>=100:
            Grade='E'
        else:
            Grade="fail"
        i.append([total,Grade])
        l.append(i)
with open("c://sqlite//result.csv","w") as f1:
    data1=csv.writer(f1)
    data.writerows(l)

#List out Top 3 Student id and name with its percentage.

import csv
with open("c://sqlite//result.csv",'r') as f:
    data=csv.reader(f)
    per=[]
    for i in data:
        percentage=(int(total_marks)/5)
        per.append(percentage)
print("sid\t","sname\t","percentage\t")
for i in range(3):
    print("{}\t,{}\t,{}\t".format(i[0],i[1],i[2]))
    


        
    
    

