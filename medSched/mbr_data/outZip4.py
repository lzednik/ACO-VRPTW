import time
import sqlite3
from scipy.spatial import distance

dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from OutZipCombs3')

c.execute(  '''
    select  a.comb_id,
            a.zip_cd1,
            a.zip_cd2,
            a.dist,
            a.tme,
            b.lat,
            b.lon,
            c.lat,
            c.lon

    from    OutZipCombs2 a,
            zipCenters b,
            zipCenters c
    where   a.zip_cd1 = b.zip_cd and
            a.zip_cd2 = c.zip_cd
            ''')
recs=c.fetchall()


for rec in recs:
    coord_from=(rec[6],rec[5])
    coord_to=(rec[8],rec[7])

    crow_dist=round(distance.euclidean(coord_from,coord_to),5)
    
    #print(rec[1],rec[2],crow_dist)
    c.execute('''INSERT INTO OutZipCombs3(comb_id,zip_cd1,zip_cd2,dist,tme,crow_dist)
            VALUES(?,?,?,?,?,?)''', (rec[0],rec[1],rec[2],rec[3],rec[4],crow_dist)) 


conn.commit()
conn.close()
