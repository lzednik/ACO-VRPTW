from funs import *

dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)



il1={}
for loc in range(1,len(dataM)):
    il1[loc]=dataM[loc]['ready_time']+dataM[loc]['service_time']

mil=max(il1.values()) 

il1=sorted(il1.items(), key=lambda x: x[1])

ilPrime0=il1[0:30]
ilBackup0=il1[30:len(dataM)]

ilPrime=[]
for x in ilPrime0:
    ilPrime+=(int(mil/x[1])**2)*[x[0]]

ilBackup=[]
for x in ilBackup0:
    ilBackup+=(int(mil/x[1])**2)*[x[0]]

ilPrime[:] = [x for x in ilPrime if x != 59]


counter=1
for x in il1:
    print(counter,'\t',x)
    counter+=1


#for x in il1:
#    x0=x[0]
#    x1=x[1]
#    print(x0,'\t',x1,'\t',mil/x1,'\t',68/x1)


