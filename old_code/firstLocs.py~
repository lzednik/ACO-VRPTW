from funs import *
from random import choice


dataM=readData('Input/solomon_r101.txt')
visited=[]
vehicleCount=1000

#log file
FirstLocPath=path.relpath('Output/FirstLoc.txt')
txtFile = open(FirstLocPath, 'w')
txtFile.write('First Locations\n\n')
txtFile.close()
txtFile = open(FirstLocPath,"a")

for veh in range(vehicleCount):
    #need to figure out where the starting point is going to be for each vehicle
    initAttract={}
    sumAttr=0
    for loc in range(len(dataM)):
        if loc not in visited and loc !=0:
            attr=dataM[loc]['ready_time']*dataM[loc]['due_time']
            initAttract[loc]=attr
            sumAttr+=attr
            #print('Due time is:\t',dataM[loc]['due_time'],'\tAttractivness is:\t',attr)

            

    initAttract2={}
    for loc in initAttract:
        attr2=int(sumAttr/initAttract[loc])
        initAttract2[loc]=int(attr2)
        #print('Due time is:\t',dataM[loc]['due_time'],'\tAttractivness is:\t',attr2)
            
    cutofList=[]
    for x in range(len(initAttract2)):
        #print(x+1, '\t',len(initAttract2)-x)
        cutofList+=(len(initAttract2)-x)*[x+1]
        cutoff=choice(cutofList)

    initAttract3 = sorted(initAttract2, key=initAttract2.get, reverse=True)[:cutoff]
                
    initProbList=[]
    for loc in initAttract3:
        initProbList+=int(initAttract2[loc])*[loc]
    
    firstLoc=choice(initProbList)
    print('First loc:',firstLoc,'\tDue Time:',dataM[firstLoc]['due_time'])

    txtFile.write('First loc:\t')
    txtFile.write(str(firstLoc))
    txtFile.write('\tDue Time:\t')
    txtFile.write(str(dataM[firstLoc]['due_time']))
    txtFile.write('\n')

txtFile.close()
print('all done')        
