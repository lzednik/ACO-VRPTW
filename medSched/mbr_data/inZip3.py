import sqlite3
import time


dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('delete from inZipCombs3')

c.execute(  '''
            select  comb_id,
                    zip_cd,
                    gdist,
                    gtime
            from inZipCombs2
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
        ts1=10
    
    c.execute('''INSERT INTO inZipCombs3(comb_id,zip_cd,gdist,gtime,dist,tme)
            VALUES(?,?,?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3],dist,ts1)) 


conn.commit()
conn.close()
