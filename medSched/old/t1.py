import sqlite3


dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

#c.execute('Delete from distTme')


custList=[1,345,678,7666,7777,44444,27]


distM=[]
for cust1 in custList:
    d0M=[]
    for cust2 in custList:
        c.execute(  '''
            select  c.tme
            from    mbrs a,
                    mbrs b,
                    distTme c
            where   a.mbr_id = ? and
                    b.mbr_id = ? and
                    (
                    (a.zip = c.zip1 and
                    b.zip = c.zip2)
                    or
                    (a.zip = c.zip2 and
                    b.zip = c.zip1)
                    )

                    ''',(cust1,cust2,))
        recs=c.fetchall()
        
        d0M.append(recs[0])
    distM.append(d0M)

for d in distM:
    print(d)

conn.close

