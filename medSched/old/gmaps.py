import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyCgBrIh97GTLhnLK7NMkGTSqZMbHENuMJo')

now = datetime.now()

api_key='AIzaSyCgBrIh97GTLhnLK7NMkGTSqZMbHENuMJo'


def finddist(source, destination):
    gmaps = googlemaps.Client(key=api_key)
    now = datetime.now()
    directions_result = gmaps.directions(source, destination, mode="driving",departure_time=now)
    for map1 in directions_result:
        overall_stats = map1['legs']
        for dimensions in overall_stats:
            distance = dimensions['distance']
    return distance['text']


def findtime(source, destination):
      gmaps = googlemaps.Client(key=api_key)
      now = datetime.now()
      directions_result = gmaps.directions(source, destination, mode="driving",departure_time=now)
      for map1 in directions_result:
            overall_stats = map1['legs']
            for dimensions in overall_stats:
                   duration = dimensions['duration']
                   return duration['text']

#d=fipnddist('6521 Edgewood St, Rockford, MN 55373','401 Carlson Parkway Minnetonka, MN')
dd=finddist('6521 Edgewood St Rockford MN 55373','11215 Roxbury Dr Omaha NE 68137')
dt=findtime('6521 Edgewood St Rockford MN 55373','11215 Roxbury Dr Omaha NE 68137')


print('distance is:',dd)
print('distance is:',dt)



