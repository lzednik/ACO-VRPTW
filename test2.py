from funs import *
from random import choice

dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)

vehicle_count=20

d1={}
for loc in range(len(dataM)):
    if loc !=0:
        d1[loc]=dataM[loc]['ready_time']+dataM[loc]['service_time']

d2=sorted(d1.items(), key=lambda x: x[1])[0:vehicle_count]


for item in d2:
    print(item)


d3=choice(d2)

print('choice is:\t',d3)
d2.remove(d3)

for item in d2:
    print(item)

print('final choice is:\t',d3[0])

