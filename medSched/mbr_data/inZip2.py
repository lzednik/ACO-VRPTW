
import googlemaps
from datetime import datetime
import sqlite3
import time


#paid code
api_key='AIzaSyBZG6yfPokTPWdIt3MijWJiyT91v-9rt5M'


def gDistTime(source, destination):
    gmaps = googlemaps.Client(key=api_key)
    now = datetime.now()
    directions_result = gmaps.directions(source, destination, mode="driving",departure_time=now)
    for map1 in directions_result:
        overall_stats = map1['legs']
        for dimensions in overall_stats:
            distance = dimensions['distance']
            duration = dimensions['duration']
    return (distance,duration)



dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('delete from inZipCombs2')

c.execute('''
            select  a.comb_id, 
                    a.zip_cd,
                    a.loc_from,
                    a.loc_to,
                    b.lat,
                    b.lon,
                    c.lat,
                    c.lon

                    from    inZipCombs1 a,
                            locations b,
                            locations c
                    where   a.loc_from = b.loc_id and
                            a.loc_to = c.loc_id
            ''')
trips=c.fetchall()


for trip in trips:
    print(trip[0])
    trip_from=str(trip[4])+' '+str(trip[5])
    trip_to=str(trip[6])+' '+str(trip[7])
    try:
        gdt=gDistTime(trip_from,trip_to)
        time.sleep(0.1)
        gdist=gdt[0]['text']
        gtime=gdt[1]['text']

    except:
        gdist=0
        dtime=0
    c.execute('''INSERT INTO inZipCombs2(comb_id,zip_cd,gdist,gtime)
                VALUES(?,?,?,?)''', (trip[0],trip[1],gdist,gtime)) 
    conn.commit()

conn.close()

print('done')

