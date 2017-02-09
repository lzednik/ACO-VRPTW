import time
import random
mbrs=[]

f=open('data_files\mbr_addr.txt','r')
lines=f.readlines()[1:]
for line in lines:
    fields=line.split('|')
    mbrs.append(fields)
f.close()


zips = [rec[6] for rec in mbrs]

zips=set(zips)
zips=list(zips)
sample=[]


for zipcode in zips:
    g1=[rec for rec in mbrs if rec[6] == zipcode]
   
    ss=10
    if len(g1) < 10:
        ss=len(g1)
    
    s1=[g1[i] for i in random.sample(range(len(g1)), ss)]
    
    for rec in s1:
        sample.append([rec[0],rec[6],rec[2]+' '+rec[3]+' '+rec[4]+' '+rec[5]+' '+rec[6]])



sof=open('data_files\sample.txt','w')

for rec in sample:
    sof.write(rec[0])
    sof.write('|')
    sof.write(rec[1])
    sof.write('|')
    sof.write(rec[2])
    sof.write('|')
    sof.write('\n')

sof.close()







#a1=[rec for rec in mbrs if rec[4] == 'BROOKLYN PK']
#for rec in a1:
#    print(rec)
