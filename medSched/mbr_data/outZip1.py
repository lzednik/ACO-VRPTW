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


dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from outZipCombs1')

c.execute('select distinct zip_cd from mbrs')
zipdt=c.fetchall()

zips=[z[0] for z in zipdt]

trips=[]
ct=0
for zip_cd1 in zips:
    for zip_cd2 in zips:
        if zip_cd1 != zip_cd2:
            trips.append((zip_cd1,zip_cd2))
            ct+=1


comb_key=1
for trip in trips:
    try:
        gdt=gDistTime(trip[0],trip[1])
        gdist=gdt[0]['text']
        gtime=gdt[1]['text']

    except:
        gdist=0
        dtime=0
    
    print(comb_key,trip[0],trip[1],gdist,gtime)
    c.execute('''INSERT INTO outZipCombs1(comb_id,zip_cd1,zip_cd2,gdist,gtime)
            VALUES(?,?,?,?,?)''', (comb_key,trip[0],trip[1],gdist,gtime)) 

    comb_key+=1
    time.sleep(0.1)

    conn.commit()
conn.close()
