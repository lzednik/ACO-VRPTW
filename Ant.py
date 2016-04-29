from random import choice
import time,sys
from os import path

#class Ant

class Ant:
    def __init__(self,vehicleCount,dataM):
        self.vehicleCount=vehicleCount
        self.vehicles=[]
        self.visited=[]
        self.distance=0
        self.time=0
        self.solution={'vehicles':[],'vehicleCount':vehicleCount,'visitedCount':0,'distance':0}
        for veh in range(vehicleCount):
            #need to figure out where the starting point is going to be for each vehicle
            initAttract={}
            sumAttr=0
            for loc in range(len(dataM)):
                if loc not in self.visited and loc !=0:
                    attr=dataM[loc]['ready_time']*dataM[loc]['due_time']
                    initAttract[loc]=attr
                    sumAttr+=attr
            

            initAttract2={}
            for loc in initAttract:
                attr2=sumAttr/initAttract[loc]
                initAttract2[loc]=int(attr2)

            cutofList=[]
            for x in range(len(initAttract2)):
                cutofList+=(len(initAttract2)-x)*[x+1]
                cutoff=choice(cutofList)

            initAttract3 = sorted(initAttract2, key=initAttract2.get, reverse=True)[:cutoff]
                
            initProbList=[]
            for loc in initAttract3:
                initProbList+=int(initAttract2[loc])*[loc]
            
            firstLoc=choice(initProbList)

            #print out probabilities
            PI_Path=path.relpath('Output/ProbsInit.txt')
            pifile=open(PI_Path,'a')
            pifile.write('vehicle\t')
            pifile.write(str(veh))
            pifile.write('\n')
            for loc in initAttract2:
                pifile.write(str(loc))
                pifile.write('\t')
                pifile.write(str(initAttract2[loc]))
                pifile.write('\n')
            pifile.write('\n\n\n')
            pifile.close()
            
            #print('Our first stop is going to be',firstLoc)
            #time.sleep(10)
            self.vehicles.append({'tour':[firstLoc],
                                  'currPos':firstLoc,
                                  'time':dataM[firstLoc]['ready_time']+dataM[firstLoc]['service_time']})
            
            self.visited.append(firstLoc)
            #for veh in self.vehicles:
            #    print(veh)
            #    time.sleep(1)
            #print('')
            #print('this is all vehs')
            #time.sleep(5)
    #calculates trips for all vehicles for one ant
    def calculate(self,dataM,distM,phiM,feasLocIN,beta): 
        prevVisitedCount=-1
        while self.solution['visitedCount']<100 and prevVisitedCount != self.solution['visitedCount']:
            #print('visited count is',self.solution['visitedCount'])
            prevVisitedCount=self.solution['visitedCount']

            iterationReturn=self.iterate(dataM,distM,phiM,feasLocIN,beta)
            
            visitedCount=iterationReturn[0]
            distanceTraveled=iterationReturn[1]
            #update best solution
            if visitedCount>self.solution['visitedCount']:
                self.solution['visitedCount']=visitedCount
                self.solution['distance']=distanceTraveled
                self.solution['vehicles']=iterationReturn[2]
        
        return(self.solution)

       
    #calculates trip for all vehicles for one ant
    def iterate(self,dataM,distM,phiM,feasLocIN,beta):
        for vehicle in self.vehicles:
            if self.time<=vehicle['time']:
                #figure out what is feasable first
                feasable=[]
                for dataItem in range(len(dataM)):
                    if vehicle['time']+distM[vehicle['currPos']][dataItem]<=dataM[dataItem]['due_time']-dataM[dataItem]['service_time'] \
                        and dataItem not in self.visited:
                            feasable.append(dataItem)
                #need to continue only if something is feasable
                if len(feasable)>0:
                    #compute attractiveness
                    attractivness={}
                    
                    #attractivness based on feasable locations count - does not work all that great
                    #for nextLoc in feasable:
                    #    attractivness[nextLoc]=1
                    #    for loc2 in range(0,len(dataM)-1):
                    #        if vehicle['time']+max(dataM[nextLoc]['ready_time'],distM[vehicle['currPos']][nextLoc]) +dataM[nextLoc]['service_time'] \
                    #                    + distM[nextLoc][loc2]+ dataM[loc2]['service_time'] < dataM[loc2]['due_time'] and loc2 not in self.visited:
                    #            attractivness[nextLoc]+=1
 

                    
                    #attractivnes as in the paper
                    for feasableLoc in feasable:
                        distanceToFeasLoc=distM[vehicle['currPos']][feasableLoc]
                        feasLocReadyTime=dataM[feasableLoc]['ready_time']
                        feasLocDueTime=dataM[feasableLoc]['due_time']

                        delivery_time=max(vehicle['time']+distanceToFeasLoc,feasLocReadyTime)
                        delta_time=delivery_time-vehicle['time']
                        distance=delta_time*(feasLocDueTime-vehicle['time'])
                        distance2=max(1,distance+feasLocIN[feasableLoc])
                        eta=1/distance2
                        attractivness[feasableLoc]=eta
                        
                        #if eta>0.9:
                        #    print('eta is:\t',eta)
                        #    
                        #    txtFile = open("Output2.txt","a")
                        #    txtFile.write('eta is\t')
                        #    txtFile.write(str(eta))
                        #    txtFile.write('\nIN\t')
                        #    txtFile.write(str(feasLocIN[feasableLoc]))
                        #    txtFile.write('\ndistance\t')
                        #    txtFile.write(str(distance))

                        #    
                        #    txtFile.close()
                        #    time.sleep(5)
                        #    sys.exit()


                    bottomSum=0
                    for attr in attractivness:
                        bottomSum+=(phiM[vehicle['currPos']][attr]*(attractivness[attr]**beta)) 

                    probs={}
                    minProb=1
                    for attr in attractivness:
                        probs[attr]=(phiM[vehicle['currPos']][attr]*(attractivness[attr]**beta))/bottomSum
                        if probs[attr]<minProb:
                            minProb=probs[attr]
                    
                    #probabilities of selection based on attractivness
                    probList=[]
                    for prob in probs:
                        try:
                            probList+=int(probs[prob]/minProb)*[prob]
                        except:
                            print('prob exception')
                            print('loc is \t',prob)
                            print('prob count is \t',int(probs[prob]/minProb))
                            print('')

                            txtFile = open('Output.txt', 'w')
                            txtFile.write('prob exception at:\t')
                            txtFile.close()
                            
                            txtFile = open("Output.txt","a")
                            probs2=probs
                            txtFile.write(str(prob))
                            txtFile.write('\n\n')
                            for prob2 in probs2:
                                txtFile.write('probability:\t')
                                txtFile.write(str(probs2[prob2]))
                                txtFile.write('\tloc:\t')
                                txtFile.write(str(prob2))
                                txtFile.write('\n')
                            txtFile.close()
                            time.sleep(5)
                    nextLoc=choice(probList)
                   
                    '''
                    #print out probabilities
                    P_Path=path.relpath('Output/Probs.txt')
                    pfile=open(P_Path,'a')
                    for prob in probs:
                        pfile.write(str(prob))
                        pfile.write('\t')
                        pfile.write(str(probs[prob]))
                        pfile.write('\n')
                    pfile.write('\n\n\n')
                    pfile.close()
                    '''

                    #need to update vehicle and log the visit
                    vehicle['tour'].append(nextLoc)
                    if nextLoc != 0:
                        self.visited.append(nextLoc)
                    self.distance+=distM[vehicle['currPos']][nextLoc]
                    vehicle['time']=vehicle['time']+max(distM[vehicle['currPos']][nextLoc],dataM[nextLoc]['ready_time'])+dataM[dataItem]['service_time']
                    feasLocIN[nextLoc]+=1
                    vehicle['currPos']=nextLoc
                    
                    #update time
                    minTime=1000000
                    for vehicle in self. vehicles:
                        if vehicle['time']<minTime:
                            minTime=vehicle['time']
                    self.time=minTime

        #print the tour for all vehicles
        #for index,vehicle in enumerate(self.vehicles):
        #    print('Vehicle',index+1,'\ttour:',vehicle['tour'])
        #print('')
        return(len(self.visited),self.distance,self.vehicles)
