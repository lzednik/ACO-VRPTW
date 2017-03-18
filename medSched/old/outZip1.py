import sqlite3
import time
import itertools
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


dtb='data_files/medica_mbrs.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from outZipDT')

c.execute('select distinct zip from mbrs')
zipdt=c.fetchall()

zips=[z[0] for z in zipdt]

trips=itertools.combinations(zips, 2)

out_key=200000
for trip in trips:
    try:
        gdt=gDistTime(trip[0],trip[1])
        gdist=gdt[0]['text']
        gtime=gdt[1]['text']

    except:
        gdist=0
        dtime=0
    
    print(out_key,trip[0],trip[1],gdist,gtime)
    c.execute('''INSERT INTO outZipDT(out_key,zip1,zip2,dist,time)
            VALUES(?,?,?,?,?)''', (out_key,trip[0],trip[1],gdist,gtime)) 

    out_key+=1
    time.sleep(0.1)

    conn.commit()
conn.close()
