import googlemaps
from datetime import datetime

now=datetime.now()

#free code
#api_key='AIzaSyCgBrIh97GTLhnLK7NMkGTSqZMbHENuMJo'

#paid code
api_key='AIzaSyBZG6yfPokTPWdIt3MijWJiyT91v-9rt5M'
gmaps = googlemaps.Client(key=api_key)

#lat=45.094396
#lon=-93.734923

lat=45.140371
lon=-93.808851

res=gmaps.reverse_geocode((lat, lon))


addr=res[0]['formatted_address']
addr_comp=res[0]['address_components']

zip_cd='0'
for addr_type in addr_comp:
    if addr_type['types']==['postal_code']:
        zip_cd=addr_type['short_name']



print('address is',addr)
print('zip is',zip_cd)

