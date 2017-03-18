

import sqlite3


dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()



svc_dt='2017-02-16'
cm_ct=20

#c.execute('Delete from schedule')

c.execute('''INSERT INTO cmAvlblt(svc_dt,cm_ct)
            VALUES(?,?)''', (svc_dt,cm_ct)) 



conn.commit()
conn.close()

