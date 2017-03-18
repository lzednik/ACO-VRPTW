# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 08:35:41 2017

@author: ladislav.zednik
"""

import time
import sqlite3

dtb='data_files/medica_mbrs.sqlite'
conn=sqlite3.connect(dtb)

c=conn.cursor()
c.execute('DELETE FROM mbrs')

f=open('data_files/mbr_addr.txt')
lines=f.readlines()[1:]


for line in lines:
    rec = line.split('|')
    
    if rec[3]=='':
        fa=rec[2]+' '+rec[4]+' '+rec[5]+' '+rec[6]
    else:        
        fa=rec[2]+' '+rec[3]+' '+rec[4]+' '+rec[5]+' '+rec[6]
    
    c.execute('''INSERT INTO mbrs(mbr_id,product,addr1,addr2,city,state,zip,full_addr)
            VALUES(?,?,?,?,?,?,?,?)''', (rec[0],rec[1],rec[2].upper(),rec[3].upper(),rec[4].upper(),rec[5].upper(),rec[6],fa.upper())) 


conn.commit()   
conn.close()
print('done')
