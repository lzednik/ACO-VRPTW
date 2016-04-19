from funs import *
import time

dataM=readData('solomon_r101.txt')
distM=createDistanceMatrix(dataM)


currLoc=0
currTime=0

attractivness={}

for loc in range(0,len(dataM)-1):
    if currTime + distM[currLoc][loc] <dataM[loc]['due_time']:
        nextLoc=loc
        attractivness[nextLoc]=0
        for loc2 in range(0,len(dataM)-1):
            if currTime+max(dataM[nextLoc]['ready_time'],distM[currLoc][nextLoc]) + distM[nextLoc][loc2] <dataM[loc2]['due_time']:
                attractivness[nextLoc]+=1

print(attractivness[1])
print(attractivness[2])
print(attractivness[3])
#print(feasable)
