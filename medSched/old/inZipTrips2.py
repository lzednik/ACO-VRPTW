import time


trips=[]
f=open('data_files\inZipTrips.txt','r')
lines=f.readlines()
for line in lines:
    fields=line.split('|')
    trips.append(fields[:-1])
f.close()


mis=[trip for trip in trips if trip[7] == '0']


s=mis[0][3]

print(s)

s2=s.split(' ', 3)
print(s2)




for trip in mis:
    print(trip[3])
    print(trip[6])
    print('**************')
    time.sleep(1)
