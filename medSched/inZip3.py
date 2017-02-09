
import sqlite3
import time
import googlemaps
from datetime import datetime

now=datetime.now()

#free code
#api_key='AIzaSyCgBrIh97GTLhnLK7NMkGTSqZMbHENuMJo'

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




dtb='data_files/medSched.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from inZipDT')

c.execute('''select a.comb_key,
                    a.zip, 
                    a.mbr1,
                    b.full_addr,
                    a.mbr2,
                    c.full_addr
           from combs a, mbrs b, mbrs c
           where    a.mbr1 = b.mbr_id and
                    a.mbr2 =c.mbr_id
           ''')


trips=c.fetchall()

for trip in trips:
    try:
        gdt=gDistTime(trip[3],trip[5])
        gdist=gdt[0]['text']
        gtime=gdt[1]['text']

    except:
        gdist=0
        dtime=0
    
    print(trip[0],gdist,gtime)
    c.execute('''INSERT INTO inZipDT(comb_key,zip,dist,time)
            VALUES(?,?,?,?)''', (trip[0],trip[1],gdist,gtime)) 

    time.sleep(0.1)
conn.commit()
conn.close()
