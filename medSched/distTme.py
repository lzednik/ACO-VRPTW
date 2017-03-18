import sqlite3


dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from distTme')

#outzips
c.execute(  '''
    select  zip1,
            zip2,
            dist,
            tme
    from    OutZipDT
            ''')
recs=c.fetchall()

for rec in recs:
    c.execute('''INSERT INTO distTme(zip1,zip2,dist,tme)
            VALUES(?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3])) 



#inzips available
c.execute(  '''
    select  zip,
            dist,
            tme
    from    inZipDT
            ''')
recs=c.fetchall()

for rec in recs:
    c.execute('''INSERT INTO distTme(zip1,zip2,dist,tme)
            VALUES(?,?,?,?)''', (rec[0],rec[0],rec[1],rec[2])) 


#inzips without pop set to inzip avg dist=4.6, tme=8.3
c.execute(  '''
    select  distinct zip
            
    from    mbrs
    where zip not in (select distinct zip from inZipDT)
            ''')
recs=c.fetchall()

for rec in recs:
    c.execute('''INSERT INTO distTme(zip1,zip2,dist,tme)
            VALUES(?,?,?,?)''', (rec[0],rec[0],4.6,8.3)) 

conn.commit()
conn.close()
