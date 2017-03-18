
import sqlite3
import time
import itertools
import random


dtb='data_files/medsched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('delete from combs')
c.execute('select distinct zip from mbrs')
zipdt=c.fetchall()

comb_key=10000
zip_ct=0
for rec in zipdt:
    zipcd=rec[0]
    print(zipcd)
    c.execute('''
        Select mbr_id
        from mbrs
        where substr(full_addr,1,1) in ('0','1','2','3','4','5','6','7','8','9') and
              full_addr not like '%C/O%' and
              full_addr not like '%BOX%' and
              full_addr not like '%GENERAL DELIVERY%' and
              zip = ?''',(zipcd,)) 
        
    adt=c.fetchall()
    al1=[]
    ss=10
    for a in adt:
        al1.append(a[0])
    
    if len(al1) < 10:
        ss=len(al1)
    
    al2=[al1[i] for i in random.sample(range(len(al1)), ss)]
    al3=itertools.combinations(al2, 2)
    
    for co in al3:

        c.execute('''INSERT INTO combs(comb_key,zip,mbr1,mbr2)
            VALUES(?,?,?,?)''', (comb_key,zipcd,co[0],co[1])) 
        comb_key+=1


conn.commit()
conn.close()

print('done')
