import sqlite3
import time
import googlemaps

#free code
#api_key='AIzaSyCgBrIh97GTLhnLK7NMkGTSqZMbHENuMJo'

#paid code
api_key='AIzaSyBZG6yfPokTPWdIt3MijWJiyT91v-9rt5M'
gmaps = googlemaps.Client(key=api_key)


dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('Delete from locations')

c.execute(  '''
            select  loc_id,
                    zip_cd0,
                    lat,
                    lon 
            from locations0
            ''')
locs=c.fetchall()

ct=0
for loc in locs:
    lat=loc[2]
    lon=loc[3]
    
    res=gmaps.reverse_geocode((lat, lon))
    time.sleep(0.1)
    
    #get address
    addr=''
    addr=res[0]['formatted_address']
    addr_comp=res[0]['address_components']
    
    #get zip
    zip_cd='00000'
    for addr_type in addr_comp:
        if addr_type['types']==['postal_code']:
            zip_cd=addr_type['short_name']

    
    c.execute('''INSERT INTO locations(loc_id,zip_cd0,lat,lon,full_addr,zip_cd)
            VALUES(?,?,?,?,?,?)''', (loc[0],loc[1],lat,lon,addr,zip_cd)) 

    conn.commit()
    print('counter',ct)
    ct+=1
    

conn.close()

