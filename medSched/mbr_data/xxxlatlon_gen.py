import random

mfact=1000

lats=[]
lat=44.68*mfact
while lat<=45.24*mfact:
    lats.append(lat)
    lat+=1


lons=[]
lon=-93.85*mfact
while lon<=-92.81*mfact:
    lons.append(lon)
    lon+=1


lats_lons=[]

for lat in lats:
    for lon in lons:
        lats_lons.append((lat/mfact,lon/mfact))
        

#disp
lats_lons_sample=random.sample(lats_lons,10)

for ll in lats_lons_sample:
    print(ll)
