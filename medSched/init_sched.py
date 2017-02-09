
import sqlite3


dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

cm_id=6
mbr_id=8
svc_date='2017-02-15'
svc_time=450
svc_len=80

#c.execute('Delete from schedule')

c.execute('''INSERT INTO schedule(cm_id,mbr_id,svc_date,svc_time,svc_len)
            VALUES(?,?,?,?,?)''', (cm_id,mbr_id,svc_date,svc_time,svc_len)) 



conn.commit()
conn.close()

