import time
import itertools
import googlemaps
from datetime import datetime


now = datetime.now()
#free code
#api_key='AIzaSyCgBrIh97GTLhnLK7NMkGTSqZMbHENuMJo'

#paid code
api_key='AIzaSyBZG6yfPokTPWdIt3MijWJiyT91v-9rt5M'


def finddisttime(source, destination):
    gmaps = googlemaps.Client(key=api_key)
    now = datetime.now()
    directions_result = gmaps.directions(source, destination, mode="driving",departure_time=now)
    for map1 in directions_result:
        overall_stats = map1['legs']
        for dimensions in overall_stats:
            distance = dimensions['distance']
            duration = dimensions['duration']
    return (distance,duration)


mbrs=[]
f=open('data_files\sample.txt','r')
lines=f.readlines()
for line in lines:
    fields=line.split('|')
    mbrs.append(fields[:-1])
f.close()

zips = [rec[1] for rec in mbrs]


zips=set(zips)
zips=list(zips)

trips=[]
for zipcode in zips:
    #g1=[rec for rec in mbrs if rec[1] == zipcode]
    g1=[rec[0] for rec in mbrs if rec[1] == zipcode]

    for comb in itertools.combinations(g1, 2):



        p1=[c for c in mbrs if c[0]==comb[0]][0]
        p2=[c for c in mbrs if c[0]==comb[1]][0]

        trip=[]
        trip.append(p1[0])
        trip.append(p1[1])
        trip.append(p1[2])

        trip.append(p2[0])
        trip.append(p2[1])
        trip.append(p2[2])
        trips.append(trip)
        

sof=open('data_files\inZipTrips.txt','w')


rec_count=1
for trip in trips:
    try:
        gdt=finddisttime(trip[2],trip[5])
        gdist=gdt[0]['text']
        gtime=gdt[1]['text']
    except:
        gdist=0
        gtime=0

    print(rec_count,trip[0],trip[1],trip[3],trip[4],gdist,gtime)

    sof.write(str(rec_count))
    sof.write('|')
    sof.write(trip[0])
    sof.write('|')
    sof.write(trip[1])
    sof.write('|')
    sof.write(trip[2])
    sof.write('|')
    sof.write(trip[3])
    sof.write('|')
    sof.write(trip[4])
    sof.write('|')
    sof.write(trip[5])
    sof.write('|')
    sof.write(str(gdist))
    sof.write('|')
    sof.write(str(gtime))
    sof.write('|')

    sof.write('\n')
    rec_count+=1
    time.sleep(0.1)

sof.close()

print('done')
