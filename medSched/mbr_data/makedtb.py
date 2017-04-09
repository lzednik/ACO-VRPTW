import sqlite3

dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()


#c.execute('DROP TABLE distTme')


#c.execute('''
#    CREATE TABLE inZipCombs4(   comb_id INT,
#                                zip_cd TEXT,
#                                loc_from INT,
#                                loc_to INT,
#                                crow_dist REAL
#                      )
#''')

#c.execute('''
#    CREATE TABLE zipCenters(    zip_cd TEXT,
#                                lat REAL,
#                                lon REAL
#                      )
#''')

#c.execute('''
#    CREATE TABLE outZipCombs3(  comb_id INT,
#                                zip_cd1 TEXT,
#                                zip_cd2 TEXT,
#                                dist REAL,
#                                tme REAL,
#                                crow_dist REAL
#                      )
#''')
#
#c.execute('''
#    CREATE TABLE outZipCombs2(  comb_id INT,
#                                zip_cd1 TEXT,
#                                zip_cd2 TEXT,
#                                gdist TEXT,
#                                gtime TEXT,
#                                dist REAL,
#                                tme REAL
#                      )
#''')

#c.execute('''
#    CREATE TABLE outZipCombs1(  comb_id INT,
#                                zip_cd1 TEXT,
#                                zip_cd2 TEXT,
#                                gdist TEXT,
#                                gtime TEXT
#                      )
#''')
#

#c.execute('''
#    CREATE TABLE locations( loc_id INT,
#                            zip_cd0 TEXT,
#                            lat DECIMAL,
#                            lon DECIMAL,
#                            full_addr TEXT,
#                            zip_cd TEXT
#                      )
#''')

#c.execute('''
#    CREATE TABLE mbrs(  loc_id INT,
#                        mbr_id INT,
#                        full_name TEXT,
#                        full_addr TEXT,
#                        zip_cd TEXT
#                      )
#''')


#c.execute('''
#    CREATE TABLE inZipCombs1(    comb_id INT,
#                                zip_cd,
#                                loc_from INT,
#                                loc_to INT
#                      )
#''')


#c.execute('''
#    CREATE TABLE inZipCombs2(   comb_id INT,
#                                zip_cd,
#                                gdist TEXT,
#                                gtime TEXT
#                      )
#''')


#c.execute('''
#    CREATE TABLE inZipCombs3(   comb_id INT,
#                                zip_cd,
#                                gdist TEXT,
#                                gtime TEXT,
#                                dist INT,
#                                tme INT)
#''')


#c.execute('''
#    CREATE TABLE distTme(   zip_cd1 TEXT,
#                            zip_cd2 TEXT,
#                            dist INT,
#                            tme INT,
#                            crow_dist)
#''')
conn.commit()
conn.close()
