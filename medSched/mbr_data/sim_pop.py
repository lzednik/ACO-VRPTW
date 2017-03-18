import xml.etree.ElementTree as ET
import csv
import time
import random
import sqlite3


#check interstion of two lines given coordicates
def inter_check(c1,c2,p):
    x1=c1[0]
    x2=c2[0]
    y1=c1[1]
    y2=c2[1]
    inter=False

    #check y coordinates
    ydif1=y1 -p[1]
    ydif2=y2-p[1]

    if min(ydif1,ydif2)<=0 and max(ydif1,ydif2)>=0 and min(ydif1,ydif2)!=max(ydif1,ydif2):
        if x1==x2:
            if x1>=p[0]:
                inter=True
        else:
            slope=(y1-y2)/(x1-x2)
            x0=(p[1]-y1+slope*x1)/slope
            if x0>= p[0]:
                inter=True

    if min(ydif1,ydif2)==0 and max(ydif1,ydif2)==0:
        if max(x1,x2)>=p[0]:
            inter=True
    return inter


c1=(2.34,1.25)
c2=(5.6,7.1)
p1=(2.77,1.25)
intcheck=inter_check(c1,c2,p1)
#print(intcheck)

#read zip boundaries
with open('census/zip_bounds.csv', 'r') as f:
  reader = csv.reader(f)
  csv_zip_bounds = list(reader)[1:]

#read county zip xwalk
with open('census/county_zip_xwalk.csv', 'r') as f:
  reader = csv.reader(f)
  csv_zip_cnty_xwalk = list(reader)[1:]

#read pop per zip
with open('census/zip_pop.csv', 'r') as f:
  reader = csv.reader(f)
  csv_zip_pop = list(reader)[1:]

#list zip codes we care about:
mn_counties=['ANOKA','CARVER','CHISAGO','DAKOTA','HENNEPIN','RAMSEY','SCOTT','SHERBURNE','ISANTI','WASHINGTON','WRIGHT']
wi_counties=['ST. CROIX','PIERCE']
cov_area_zips=[]

for line in csv_zip_cnty_xwalk:
    if (line[3]=='MN' and line[4].upper() in mn_counties) or (line[3]=='WI' and line[4].upper() in wi_counties ):
        cov_area_zips.append(line[0])
        
#process zip boundaries
zip_bounds={}
for line in csv_zip_bounds:
    zip_cd=line[3]
    
    if len(line[11])>0 and zip_cd in cov_area_zips:
        xml = ET.fromstring(line[11])
        coor_all=[]
        for coord in xml.getiterator('coordinates'):
            coords1=coord.text.split(' ')
            cl2=[]
            for coord1 in coords1:
                coord2=coord1.split(',')
                cl2.append((float(coord2[0]),float(coord2[1])))
                
            coor_all.append(cl2)

        zip_bounds[zip_cd]=coor_all

#remove zip codes that dont have a boundary 
#these are post office/business/etc zip codes

cov_area_zips=[]
pop={}
for line in csv_zip_pop:
    if line[1] in zip_bounds.keys():
        if int(line[3])>0:
            pop[line[1]]=int(line[3])
            cov_area_zips.append(line[1])


total_pop=sum(pop.values())
for zip_cd in pop:
    zpop=pop[zip_cd]
    spop=int(100000*zpop/total_pop)
    pop[zip_cd]=(zpop,spop)


#create a giant rectangle and generate lat lons in it

lats=[]
lat=44.41
while lat<=45.87:
    lats.append(lat)
    lat+=0.0005
    lat=round(lat,4)

lons=[]
lon=-94.47
while lon<=-91.91:
    lons.append(lon)
    lon+=0.0005
    lon=round(lon,4)


lats_lons={}
for zip_cd in cov_area_zips:
    lats_lons[zip_cd]=[] 
for lat in lats:
    print(lat)
    for lon in lons:
        p2c=(lon,lat)

        #check each zipcode for check
        for zip_cd in cov_area_zips:
            zipconf=False
            confirmed_zip='None'
            for geom in  zip_bounds[zip_cd]:
                inter_ct=0
                for pos in range(len(geom)-1):
                    if inter_check(geom[pos],geom[pos+1],p2c):
                        inter_ct+=1
                if inter_ct%2!=0:
                    zipconf=True
                    confirmed_zip=zip_cd
                if confirmed_zip!='None':
                    lats_lons[confirmed_zip].append((lat,lon))

        
dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('delete from locations')
loc_id=1
for zip_cd in cov_area_zips:
    sample_size=min(pop[zip_cd][1],len(lats_lons[zip_cd]))
    coord_sample=random.sample(lats_lons[zip_cd],sample_size)
    for coord in coord_sample:
        lat=coord[0]
        lon=coord[1]
        c.execute('''INSERT INTO locations(loc_id,zip_cd0,lat,lon)
                                     VALUES(?,?,?,?)''',(loc_id,zip_cd,lat,lon)) 
        loc_id+=1
conn.commit() 
conn.close() 


print('all done')
