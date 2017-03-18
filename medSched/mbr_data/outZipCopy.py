
import sqlite3
import time


dtb1='C:/Users/Lada/Documents/ACO/ACO-VRPTW/medSched/data_files/medSched.sqlite'
dtb2='data_files/simPop.sqlite'

conn1=sqlite3.connect(dtb1)
c1=conn1.cursor()

conn2=sqlite3.connect(dtb2)
c2=conn2.cursor()

c1.execute(  '''
            select  zip1,
                    zip2,
                    dist,
                    tme
            from outZipDT
            '''
         )

recs=c1.fetchall()

for rec in recs:
    c2.execute('''INSERT INTO distTme(zip_cd1,zip_cd2,dist,tme)
            VALUES(?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3])) 
    
    c2.execute('''INSERT INTO distTme(zip_cd1,zip_cd2,dist,tme)
            VALUES(?,?,?,?)''', (rec[1],rec[0],rec[2],rec[3])) 


conn2.commit()
conn1.close()
conn2.close()
