
import sqlite3


dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

        
c.execute('''INSERT INTO mbrs(loc_id,mbr_id,full_name,full_addr,zip_cd)
            VALUES(?,?,?,?,?)''', (0,0,'depo','401 Carlson Pkwy Minnetonka, MN 55305','55305'))
conn.commit()
conn.close()
