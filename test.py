from funs import *
from random import choice

dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)


curr_time=10
curr_pos=59
phi=0.00053


il1={}

for loc in range(1,len(dataM)):
    il1[loc]=dataM[loc]['ready_time']+dataM[loc]['service_time']

il2=sorted(il1.items(), key=lambda x: x[1])[0:10]


multiplier=len(il2)
iltc=[]
for item in il2:
    iltc+=multiplier*[item[0]]
    multiplier-=1

print('len il2',len(il2))

for item in il2:
    print(item)

print('*************')
print(iltc)

nl=choice(iltc)
print(nl)
