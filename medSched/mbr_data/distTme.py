import time
import sqlite3


dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from distTme')

#inzips
c.execute(  '''
    select  a.zip_cd,
            round(avg(a.crow_dist),5),
            round(avg(b.dist),2),
            round(avg(b.tme),2)

    from    inZipCombs4 a,
            inZipCombs3 b
    where a.zip_cd = b.zip_cd
    group by a.zip_cd
            ''')
recs1=c.fetchall()


for rec in recs1:
    c.execute('''INSERT INTO distTme(zip_cd1,zip_cd2,dist,tme,crow_dist)
            VALUES(?,?,?,?,?)''', (rec[0],rec[0],rec[1],rec[2],rec[3])) 



#outzips
c.execute(  '''
    select  zip_cd1,
            zip_cd2,
            dist,
            tme,
            crow_dist


    from    outZipCombs3
            ''')
recs2=c.fetchall()


for rec in recs2:
    c.execute('''INSERT INTO distTme(zip_cd1,zip_cd2,dist,tme,crow_dist)
            VALUES(?,?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3],rec[4])) 


conn.commit()
conn.close()

print('done')
