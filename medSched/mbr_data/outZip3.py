import sqlite3
import googlemaps
import time

dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

#paid code
api_key='AIzaSyBZG6yfPokTPWdIt3MijWJiyT91v-9rt5M'
gmaps = googlemaps.Client(key=api_key)


c.execute('Delete from zipCenters')

c.execute(  '''
    select  distinct 
            zip_cd1

    from    OutZipCombs2
            ''')
recs=c.fetchall()

for rec in recs:
    zip_cd=rec[0]

    coords=gmaps.geocode(zip_cd)
    lat=coords[0]['geometry']['location']['lat']
    lon=coords[0]['geometry']['location']['lng']
    
    time.sleep(0.1)
    c.execute('''INSERT INTO zipCenters(zip_cd,lat,lon)
            VALUES(?,?,?)''', (zip_cd,lat,lon)) 

    print(zip_cd,lat,lon)

conn.commit()
conn.close()
