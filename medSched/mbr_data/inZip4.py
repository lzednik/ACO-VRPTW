

import sqlite3
import time


dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute(  '''
            select  zip_cd,
                    round(avg(dist),2),
                    round(avg(tme),2)
            from inZipCombs3
            group by zip_cd
            '''
         )

recs=c.fetchall()

for rec in recs:
    c.execute('''INSERT INTO distTme(zip_cd1,zip_cd2,dist,tme)
            VALUES(?,?,?,?)''', (rec[0],rec[0],rec[1],rec[2])) 


conn.commit()
conn.close()
