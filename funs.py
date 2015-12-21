from scipy.spatial import distance

#reads txt file and saves in list by line, then in dictionary per line item
#the dictionary keys are values from the very first line
def readData(txtFile):
    data=[]
    dataM=[]
    try: 
        for line in open(txtFile):
            data.append(line)

        keys=data[0].split()
        data.pop(0)

        for line in data:
            items=line.split()
            itemDict={}
            for index,item in enumerate(items):
                #print('the index is ',keys[index],'and the item is',item)
                if index==0:
                    itemDict[keys[index]]=int(item)
                else:
                    itemDict[keys[index]]=float(item)
                    
            dataM.append(itemDict)
    except FileNotFoundError as e:
        print('File was not found')
        print(e)
        exit()
    return(dataM)


#computes distance matrix based on dataM
def createDistanceMatrix(dataM):
    distM=[]
    for locFrom in dataM:
        coordFrom=(locFrom['xcoord'],locFrom['ycoord'])

        locFromDist=[]
        for locTo in dataM:
            coordTo=(locTo['xcoord'],locTo['ycoord'])
            locFromDist.append(distance.euclidean(coordFrom,coordTo))

        distM.append(locFromDist)
    return(distM)

#creates the pheromones matrix
def createPheromoneMatix(size,distance):
    phi=1/(size*distance)
    phiLine=size*[phi]
    phiMatrix=size*[phiLine]
    return phiMatrix

#nearest neighbor algorithm
def nnSearch(depo,distM,dataM):
    currLoc=depo
    visited=[]
    visited.append(currLoc)
    locCount=len(distM[currLoc])
    distanceTraveled=0
    vehList=[]
    time=0
    vehicle=[]
    vehicle.append(currLoc)

    while len(visited)<locCount:
        placesToGo=sorted([(index,item) for index,item in enumerate(distM[currLoc])],key=lambda x: x[1])
        position=0

        while position<locCount and placesToGo[position][0] in visited:
            position+=1

        #print('Going from',currLoc,'to',placesToGo[position][0],'distance',placesToGo[position][1])
        

        newServiceStartTime=max((time+placesToGo[position][1]),dataM[placesToGo[position][0]]['ready_time'])
        newServiceTime=dataM[placesToGo[position][0]]['service_time']
        newDueTime=dataM[placesToGo[position][0]]['due_time']

        if newServiceStartTime+newServiceTime<=newDueTime:
            #add to same vehicle
            vehicle.append(placesToGo[position][0])
            time+=(newServiceStartTime+newServiceTime)
        else:
            vehList.append(vehicle)
            vehicle=[]
            time=0
            currLoc=depo
            vehicle.append(currLoc)
            
            placesToGo=sorted([(index,item) for index,item in enumerate(distM[currLoc])],key=lambda x: x[1])
            while position<locCount and placesToGo[position][0] in visited:
                position+=1

            newServiceStartTime=max((time+placesToGo[position][1]),dataM[placesToGo[position][0]]['ready_time'])
            newServiceTime=dataM[placesToGo[position][0]]['service_time']
            newDueTime=dataM[placesToGo[position][0]]['due_time']

            vehicle.append(placesToGo[position][0])
            time+=(newServiceStartTime+newServiceTime)
            
            #start new vehicle
        '''
        if max((time+placesToGo[position][1]),dataM[placesToGo[position][0]]['ready_time'])+dataM[placesToGo[position][0]]['service_time'] <=dataM[placesToGo[position][0]]['due_time']:
            vehicle.append(placesToGo[position][0])
            time+=(max((time+placesToGo[position][1]),dataM[placesToGo[position][0]]['ready_time'])+dataM[placesToGo[position][0]]['service_time'])
        else:
            vehList.append(vehicle)
            time=max(distM[depo][placesToGo[position][0]],dataM[placesToGo[position][0]]['ready_time'])+dataM[placesToGo[position][0]]['service_time']
            vehicle=[]
            vehicle.append(placesToGo[position][0])
        '''     
        visited.append(placesToGo[position][0])
        distanceTraveled+=placesToGo[position][1]
        currLoc=placesToGo[position][0]

    print('')
    for veh in vehList:
        print(veh)
    print('')
    print('number of vehicles',len(vehList))
    print('')
    print('distance traveled',distanceTraveled)

