import time
import random
import csv
import sqlite3
import re

#import mbr_data
dtb='data_files/simPop.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('delete from mbrs')


c.execute(  '''
            select  loc_id,
                    full_addr,
                    zip_cd
            from locations
            '''
         )

locs=c.fetchall()

#import census first names
fnames=[]
freq_sum_fn=0

#female
with open('C:/Users/Lada/Documents/ACO\ACO-VRPTW/medSched/mbr_data/census/names/dist.female.first') as file: 
    data = file.readlines() 
    
    for line in data:
        fname=line[:15].strip()
        fname_freq=float(line[15:20])
        fnames.append((fname,(freq_sum_fn,freq_sum_fn+fname_freq)))
        freq_sum_fn+=fname_freq

#male
with open('C:/Users/Lada/Documents/ACO\ACO-VRPTW/medSched/mbr_data/census/names/dist.male.first') as file: 
    data = file.readlines() 
    
    for line in data:
        fname=line[:15].strip()
        fname_freq=float(line[15:20])
        fnames.append((fname,(freq_sum_fn,freq_sum_fn+fname_freq)))
        freq_sum_fn+=fname_freq


#import last names census
with open('C:/Users/Lada/Documents/ACO\ACO-VRPTW/medSched/mbr_data/census/names/Names_2010Census.csv', 'r') as f:
    reader = csv.reader(f)
    lnames0 = list(reader)[1:]

freq_sum_ln=0
lnames=[]
for lname in lnames0:
    if lname[0]!='ALL OTHER NAMES':
        lname_freq=int(lname[2])
        lnames.append((lname[0],(freq_sum_ln,freq_sum_ln+lname_freq)))
        freq_sum_ln+=lname_freq

#loop over our mbr_data records, generate names and fix stuff
mbr_id=1
for loc in locs:
    #pick fname 
    fname_prob=random.uniform(0,freq_sum_fn)

    #find the picked fname
    for fname in fnames:
        if fname_prob >fname[1][0] and fname_prob <=fname[1][1]:
            first_name=fname[0]

    #pick lname 
    lname_prob=random.uniform(0,freq_sum_ln)

    #find the picked fname
    for lname in lnames:
        if lname_prob >lname[1][0] and lname_prob <=lname[1][1]:
            last_name=lname[0]

    full_name=str(first_name+' '+last_name).title()
    loc_id=loc[0]
    
    addr_fix_m=re.findall('\d+-',loc[1])
    if len(addr_fix_m)>0:
        full_addr= re.sub('\d+-\d+', addr_fix_m[0][:-1], loc[1])
    else:
        full_addr=loc[1]

    full_addr=full_addr.replace(', USA','')
    zip_cd=loc[2]
    
    c.execute('''INSERT INTO mbrs(loc_id,mbr_id,full_name,full_addr,zip_cd)
            VALUES(?,?,?,?,?)''', (loc_id,mbr_id,full_name,full_addr,zip_cd)) 
    print(mbr_id,full_name,full_addr,zip_cd)
    mbr_id+=1
    conn.commit()
conn.close()
