import sqlite3
from statistics import mean


dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from OutZipDT')

c.execute(  '''
    select  out_key,
            zip1,
            zip2,
            dist,
            time

    from    OutZipDT0
            ''')
recs=c.fetchall()


for rec in recs:

    if rec[3][-2:] == 'mi':
        #print(rec[3][:-2])
        dist=float(rec[3][:-2])
    else:
        dist=35
    
    ts0=rec[4].split(' ')
    
    if len(ts0)==4:
        ts1=60*int(ts0[0])+int(ts0[2])
    else:
        ts1=int(ts0[0])
    
    if int(ts1)<10:
        ts1=10
        
    c.execute('''INSERT INTO outZipDT(out_key,zip1,zip2,d0,t0,dist,tme)
            VALUES(?,?,?,?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3],rec[4],dist,ts1)) 


conn.commit()
conn.close()
