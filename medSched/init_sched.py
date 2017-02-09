
import sqlite3


dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()



cm_id=3
mbr_id=11
svc_dt='2017-02-16'
svc_tm_from=50
svc_tm_to=125
svc_len=80

#c.execute('Delete from schedule')

c.execute('''INSERT INTO schedule(cm_id,mbr_id,svc_dt,svc_tm_from,svc_tm_to,svc_len)
            VALUES(?,?,?,?,?,?)''', (cm_id,mbr_id,svc_dt,svc_tm_from,svc_tm_to,svc_len)) 



conn.commit()
conn.close()

