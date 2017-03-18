
import sqlite3
from statistics import mean


dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from inZipDT1')
c.execute('Delete from inZipDT')

c.execute(  '''
    select  comb_key,
            zip,
            dist,
            time

    from    inZipDT0
            ''')
recs=c.fetchall()




for rec in recs:
    if rec[2][-2:] == 'mi':
        dist=float(rec[2][:-2])
    else:
        dist=1

    ts0=rec[3].split(' ')
    
    if len(ts0)==4:
        ts1=60*int(ts0[0])+int(ts0[2])

    else:
        ts1=int(ts0[0])
    
    if int(ts1)<1:
        ts1=1

    
    c.execute('''INSERT INTO inZipDT1(comb_key,zip,d0,t0,dist,tme)
            VALUES(?,?,?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3],dist,ts1)) 


c.execute(  '''
    select  zip,
            round(avg(dist),1),
            round(avg(tme),1)
    from    inZipDT1
    group by zip
            ''')
recs=c.fetchall()



for rec in recs:
    c.execute('''INSERT INTO inZipDT(zip,dist,tme)
            VALUES(?,?,?)''', (rec[0],rec[1],rec[2])) 

conn.commit()
conn.close()
