# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 08:26:10 2017

@author: ladislav.zednik
"""

import sqlite3

dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

#c.execute('DROP TABLE inZipDT')
#c.execute('DROP TABLE schedule')


#c.execute('''
#    CREATE TABLE cmAvlblt(  svc_dt REAL,
#                            cm_ct INTEGER
#                      )
#''')

#c.execute('''
#    CREATE TABLE schedule(  cm_id INTEGER,
#                            mbr_id INTEGER,
#                            svc_dt REAL,
#                            svc_tm_from INTEGER,
#                            svc_tm_to INTEGER,
#                            svc_tm_actual INTEGER,
#                            svc_len INTEGER
#                      )
#''')

#c.execute('''
#    CREATE TABLE mbrs(mbr_id INTEGER,
#                      product TEXT,
#                      addr1 TEXT,
#                      addr2 TEXT,
#                      city TEXT,
#                      state TEXT,
#                      zip TEXT,
#                      full_addr TEXT
#                      )
#''')

#c.execute('''
#    CREATE TABLE combs(comb_key INTEGER,
#                      zip TEXT,
#                      mbr1 INTEGER,
#                      mbr2 INTEGER
#                      )
#''')

#c.execute('''
#    CREATE TABLE inZipDT(   zip TEXT,
#                            dist INT,
#                            tme INT
#                      )
#''')


#c.execute('''
#    CREATE TABLE inZipDT1(  comb_key INTEGER,
#                            zip TEXT,
#                            d0 TEXT,
#                            t0 TEXT,
#                            dist INT,
#                            tme INT
#                      )
#''')

#c.execute('''
#    CREATE TABLE outZipDT(  out_key INTEGER,
#                            zip1 TEXT,
#                            zip2 TEXT,
#                            dist TEXT,
#                            time TEXT
#                      )
#''')



#c.execute('''
#    CREATE TABLE outZipDT(  out_key INTEGER,
#                            zip1 TEXT,
#                            zip2 TEXT,
#                            d0 TEXT,
#                            t0 TEXT,
#                            dist INT,
#                            tme INT
#                      )
#''')


c.execute('''
    CREATE TABLE distTme(   zip1 TEXT,
                            zip2 TEXT,
                            dist INT,
                            tme INT
                      )
''')



conn.close()

print('done')
