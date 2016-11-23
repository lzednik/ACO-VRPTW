from funs import *
import random

dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)


curr_time=0
curr_pos=0
phi=0.00053


feasable=[]
for loc in range(len(dataM)):
    if curr_time+distM[curr_pos][loc]<=dataM[loc]['due_time'] and loc != curr_pos:
        feasable.append(loc)


txtFile=open('Output/attr_test.txt','w')
txtFile.write('loc')
txtFile.write('\t')
txtFile.write('attr0')
txtFile.write('\t')
txtFile.write('attr1')
txtFile.write('\n')    

attractL0={}
attractL1={}
attr0Sum=0
choiceList=[]
for feasLoc in feasable:
    distanceToFeasLoc=distM[curr_pos][feasLoc]
    feasLocReadyTime=dataM[feasLoc]['ready_time']
    feasLocDueTime=dataM[feasLoc]['due_time']
    delivery_time=max(curr_time+distanceToFeasLoc,feasLocReadyTime)
    delta_time=delivery_time-curr_time
    attr0=delta_time*(feasLocDueTime-curr_time)
    attractL0[feasLoc]=attr0
 
for loc in attractL0:
    attr0Sum+=(phi)*(attractL0[loc])**2
                    
for loc in attractL0:
    attractL1[loc]=int(attr0Sum/((phi)*(attractL0[loc])**2))

for loc in attractL1:
    choiceList+=attractL1[loc]*[loc]

choice=random.choice(choiceList)
print(choice)

for loc in attractL1:
    txtFile.write(str(loc))
    txtFile.write('\t')
    txtFile.write(str(attractL0[loc]))
    txtFile.write('\t')
    txtFile.write(str(attractL1[loc]))
    txtFile.write('\n')

txtFile.close()


