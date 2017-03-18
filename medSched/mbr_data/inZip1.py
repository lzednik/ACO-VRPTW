
import sqlite3
import time
import random


dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()


c.execute('delete from inZipCombs1')
c.execute('select distinct zip_cd from locations')
zipdt=c.fetchall()

comb_id=1
for rec in zipdt:
    zip_cd=rec[0]
    print(zip_cd)
    c.execute('''
        Select loc_id
        from locations
        where zip_cd = ?''',(zip_cd,)) 

    locs=c.fetchall()
    if len(locs) >1:
        ss=min(100,len(locs))
        sample_from=random.sample(locs,ss)
        for sp1 in sample_from:
            locs2=[x for x in locs]
            locs2.remove(sp1)
            sp2=random.choice(locs2)
            c.execute('''INSERT INTO inZipCombs1(comb_id,zip_cd,loc_from,loc_to)
                VALUES(?,?,?,?)''', (comb_id,zip_cd,sp1[0],sp2[0])) 
            comb_id+=1

conn.commit()
conn.close()

print('done')

