import time
import sqlite3
from scipy.spatial import distance

dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from inZipCombs4')

c.execute(  '''
    select  a.comb_id,
            a.zip_cd,
            a.loc_from,
            a.loc_to,
            b.lat,
            b.lon,
            c.lat,
            c.lon

    from    inZipCombs1 a,
            locations b,
            locations c
    where   a.loc_from = b.loc_id and
            a.loc_to = c.loc_id
            ''')
recs=c.fetchall()

for rec in recs:
    coord_from=(rec[5],rec[4])
    coord_to=(rec[7],rec[6])

    crow_dist=round(distance.euclidean(coord_from,coord_to),5)
    
    c.execute('''INSERT INTO inZipCombs4(comb_id,zip_cd,loc_from,loc_to,crow_dist)
            VALUES(?,?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3],crow_dist)) 


conn.commit()
conn.close()
