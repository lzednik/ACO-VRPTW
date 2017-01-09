import time
import random


class Ant:
    def __init__(self,vehicleCount,dataM):
        self.vehicleCount=vehicleCount 
        self.locLog={}

    def calculate(self,dataM,distM,phiM,depo,tour,tour_fl):
        #reset
        self.visited=[]
        self.tour={}
        self.tour_fl=[]
        self.distance=0
        self.vehicles=[]
        self.solution={'vehicles':[],'visited':[],'vehicleCount':self.vehicleCount,'visitedCount':0,'distance':0}


        for veh in range(self.vehicleCount):
            self.vehicles.append({  'vehNum':veh+1,
                                    'tour':[depo],
                                    'currPos':depo,
                                    'time':0})

        for vehicle in self.vehicles:
            flocs=True
            while flocs==True:
                feasLocs=[]
                for loc in range(1,len(dataM)):
                    if loc not in self.visited and vehicle['time']+distM[vehicle['currPos']][loc]<=dataM[loc]['due_time']:
                        feasLocs.append(loc)
                if feasLocs:

                    choiceRand=random.uniform(0,1)
                    nlcr=False
                    if choiceRand<0.6:
                        if vehicle['currPos']==depo:
                            feasLocsDepo=[]
                            for loc in tour_fl:
                                if loc in feasLocs:
                                    feasLocsDepo.append(loc)
                            if feasLocsDepo:
                                    nextLoc=random.choice(feasLocsDepo)
                                    nlcr=True
                        else:
                            if vehicle['currPos'] in tour.keys():
                                if tour[vehicle['currPos']] in feasLocs:
                                    nextLoc=tour[vehicle['currPos']]
                                    nlcr=True
                    
                    if nlcr==False:              
                        attractL0={}
                        attr0Sum=0
                        attractL1={}
                        choiceList=[]
                        
                        #remove tour loc from feaslocs
#                        if vehicle['currPos']==depo:
#                            for loc in tour_fl:
#                                if loc in feasLocs:
#                                    feasLocs.remove(loc)
#                        else:
#                            if vehicle['currPos'] in tour.keys():
#                                if tour[vehicle['currPos']] in feasLocs:
#                                    feasLocs.remove(tour[vehicle['currPos']])
                        
                        #attractivness of feasable locs
                    
                        for feasLoc in feasLocs:
                            distanceToFeasLoc=distM[vehicle['currPos']][feasLoc]
                            feasLocReadyTime=dataM[feasLoc]['ready_time']
                            feasLocDueTime=dataM[feasLoc]['due_time']
                            delivery_time=max(vehicle['time']+distanceToFeasLoc,feasLocReadyTime)
                            delta_time=delivery_time-vehicle['time']
                            attr0=delta_time*(feasLocDueTime-vehicle['time'])
                            attractL0[feasLoc]=attr0
 
                        for loc in attractL0:
                            attr0Sum+=(phiM[vehicle['currPos']][loc])*(attractL0[loc])**2
                    
                        for loc in attractL0:
                            attractL1[loc]=int(attr0Sum/((phiM[vehicle['currPos']][loc])*(attractL0[loc])**2))
                        
                        mv_al1=max(attractL1.values())
                        if mv_al1>10000:
                            for loc in attractL1:
                                attractL1[loc]=int(10000*float(attractL1[loc])/mv_al1)

                        for loc in attractL1:
                            choiceList+=attractL1[loc]*[loc]
                    
                        nextLoc=random.choice(choiceList)
                    
                                       
                    
                    #if vehicle['currPos'] == depo:
                    #    start_time =dataM[nextLoc]['ready_time']
                    #else:
                    #    start_time=max(vehicle['time']+distM[vehicle['currPos']][nextLoc],dataM[nextLoc]['ready_time'])
                    start_time=max(vehicle['time']+distM[vehicle['currPos']][nextLoc],dataM[nextLoc]['ready_time'])

                    
                    end_time=start_time+dataM[nextLoc]['service_time']
                    
                    vehicle['tour'].append(nextLoc)
                    vehicle['time']=end_time
                    vehicle['currPos']=nextLoc
                    self.visited.append(nextLoc)
 


                else:
                    flocs=False
        
        #return to depo
        for vehicle in self.vehicles:
            vehicle['tour'].append(depo)

        #calculate distance and tours
        for vehicle in self.vehicles:
            for pos in range(len(vehicle['tour'])-1):
                self.distance+=distM[vehicle['tour'][pos]][vehicle['tour'][pos+1]]
                
                if vehicle['tour'][pos]==depo:
                    self.tour_fl.append(vehicle['tour'][pos+1])
                else:            
                    self.tour[vehicle['tour'][pos]]=vehicle['tour'][pos+1]
        solution={}
        solution['vehicles']=self.vehicles
        solution['visited']=self.visited
        solution['tour']=self.tour
        solution['tour_fl']=self.tour_fl
        solution['visitedCount']=len(self.visited)
        solution['vehicleCount']=self.vehicleCount
        solution['distance']=self.distance

        return solution
    






