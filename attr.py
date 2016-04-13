from funs import *
import time

dataM=readData('solomon_r101.txt')
distM=createDistanceMatrix(dataM)


currLoc=0
currTime=0

feasable={}

for loc in range(0,len(dataM)-1):
    if currTime + distM[currLoc][loc] <dataM[loc]['due_time']:
        nextLoc=loc
        feasable[nextLoc]=0
        for loc2 in range(0,len(dataM)-1):
            if currTime+max(dataM[nextLoc]['ready_time'],distM[currLoc][nextLoc]) + distM[nextLoc][loc2] <dataM[loc2]['due_time']:
                feasable[nextLoc]+=1

print(feasable[1])
print(feasable[2])
print(feasable[3])
#print(feasable)
