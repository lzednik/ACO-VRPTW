from scipy.spatial import distance
from os import path

#reads txt file and saves in list by line, then in dictionary per line item
#the dictionary keys are values from the very first line
def readData(txtFile):
    data=[]
    dataM=[]
    filePath=path.relpath(txtFile)
    try: 
        for line in open(filePath):
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
            locFromDist.append(int(distance.euclidean(coordFrom,coordTo)))

        distM.append(locFromDist)
    return(distM)


#initial solution
def initSolution(depo,dataM,distM):
    visited=[]
    vehicles=[]
    totalDist=0
    time=0
    vehicle={  'vehNum':1,
               'tour':[depo],
               'currPos':depo,
               'time':0}
    tour={}
    tour_fl=[]
    while len(visited)<len(dataM)-1:
        feasLocs=[]
        for loc in range(1,len(dataM)):
            if loc not in visited and vehicle['time']+distM[vehicle['currPos']][loc]<=dataM[loc]['due_time']:
                feasLocs.append((loc,distM[vehicle['currPos']][loc]))
        if feasLocs:
            nextLoc= min(feasLocs, key = lambda t: t[1])[0]
        
            vehicle['tour'].append(nextLoc)
            vehicle['time']=max(vehicle['time']+distM[vehicle['currPos']][nextLoc],dataM[nextLoc]['ready_time'])+dataM[nextLoc]['service_time']
            totalDist+=distM[vehicle['currPos']][nextLoc]
            
            if vehicle['currPos']==depo:
                tour_fl.append(nextLoc)
            else:
                tour[vehicle['currPos']]=nextLoc
            vehicle['currPos']=nextLoc
            visited.append(nextLoc)
        else:
            vehicles.append(vehicle)
            vehicle={   'vehNum':1,
                        'tour':[depo],
                        'currPos':depo,
                        'time':0}
        
    #append last veh
    vehicles.append(vehicle)
    
    solution={}
    solution['vehicles']=vehicles
    solution['visited']=visited
    solution['tour']=tour
    solution['tour_fl']=tour_fl
    solution['visitedCount']=len(visited)
    solution['distance']=totalDist
    solution['vehicleCount']=len(vehicles)

    return solution
 


