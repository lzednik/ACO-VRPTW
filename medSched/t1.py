


import sqlite3

dtb='data_files/medSched.sqlite'

conn=sqlite3.connect(dtb)
c=conn.cursor()

svc_dt='2017-03-15'

c.execute('''select mbr_id, 
                    svc_tm_from,
                    svc_tm_to,
                    svc_len
            from    schedule
            where   svc_dt =?''',(svc_dt,))

recs=c.fetchall()

for rec in recs:
    print(rec)
