import datetime
import sqlite3

dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

svc_dt=datetime.date(2017,1,1)
end_dt=datetime.date(2017,12,31)


while svc_dt <= end_dt:
    if svc_dt.weekday() <=4:
        c.execute('''INSERT INTO cmAvlblt(svc_dt,cm_ct)
                     VALUES(?,?)''',(svc_dt,5))

    
    svc_dt+=datetime.timedelta(days=1)
conn.commit()
conn.close()
