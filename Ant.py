from random import choice
import time,sys
from os import path
from collections import Counter

#class Ant

class Ant:
    def __init__(self,vehicleCount,dataM):
        self.vehicleCount=vehicleCount
        self.vehicles=[]
        self.visited=[]
        self.distance=0
        self.time=0
        self.solution={'vehicles':[],'visited':[],'vehicleCount':vehicleCount,'visitedCount':0,'distance':0}
        #self.locLog={0:{'start_time':0,'end_time':0}}        
        self.locLog={}

    def calculate(self,dataM,distM,phiM,feasLocIN,beta):
        #reset
        self.visited=[]
        self.distance=0
        self.time=0
        self.vehicles=[]
        
        #initial location
        ilD={}
        for loc in range(len(dataM)):
            ilD[loc]=dataM[loc]['due_time']
        ilSL=sorted(ilD.items(), key=lambda x: x[1])

        
        for veh in range(self.vehicleCount):
            self.vehicles.append({  'vehNum':veh+1,
                                    'tour':[ilSL[veh][0]],
                                    'currPos':ilSL[veh][0],
                                    'time':0})
        


        for vehicle in self.vehicles:

            flocs=True
            while flocs==True:
                #feasable locs
                feasLocs=[]
                for loc in range(len(dataM)):
                    if loc not in self.visited and vehicle['time']+distM[vehicle['currPos']][loc]+dataM[loc]['service_time']<=dataM[loc]['due_time']:
                        feasLocs.append(loc)
                
                if feasLocs:
                    #attractivness of feasable locs
                    attractL={}
                    attractL0={}
                    for feasLoc in feasLocs:
                        distanceToFeasLoc=distM[vehicle['currPos']][feasLoc]
                        feasLocReadyTime=dataM[feasLoc]['ready_time']
                        feasLocDueTime=dataM[feasLoc]['due_time']
                        delivery_time=max(vehicle['time']+distanceToFeasLoc,feasLocReadyTime)
                        delta_time=delivery_time-vehicle['time']
                        
                        attr0=1/(delta_time*(feasLocDueTime-vehicle['time']))

                        attr1=phiM[vehicle['currPos']][loc]*attr0
                        
                        attractL0[feasLoc]=attr1
                    
                    minAttr=min(attractL0.values())
                    for loc in attractL0:
                        attractL[loc]=int(attractL0[loc]/minAttr)**2
                    
                    choiceList=[]
                    for loc in attractL:
                        choiceList+=int(attractL[loc])*[loc]
                    
                    nextLoc=choice(choiceList)
                       
                    self.visited.append(nextLoc)
                   
                    start_time=max(vehicle['time']+distM[vehicle['currPos']][nextLoc],dataM[nextLoc]['ready_time'])
                    end_time=start_time+dataM[nextLoc]['service_time']
                    
                    self.locLog[nextLoc]={'start_time':start_time,
                                          'end_time':end_time
                                         }
                    feasLocIN[vehicle['currPos']][nextLoc]+=1 
                    vehicle['tour'].append(nextLoc)
                    vehicle['time']=end_time
                    vehicle['currPos']=nextLoc
                    


                else:
                    flocs=False

        #try inserting unassigned locs
        for loc in range(len(dataM)):
            if loc not in self.visited:
                for vehicle in self.vehicles:
                    if loc not in self.visited:
                        for tpos in range(len(vehicle['tour'])-1):
                            tpos1=vehicle['tour'][tpos]
                            tpos2=vehicle['tour'][tpos+1]
                            
                            try:
                                nLoc_st=max(self.locLog[tpos1]['end_time']+distM[tpos1][loc],dataM[loc]['ready_time'])
                                nLoc_et=nLoc_st+dataM[loc]['service_time']
                            except:
                                print('exception')
                                print(tpos1)
                                print(loc)
                                time.sleep(10)
                            if (self.locLog[tpos1]['end_time']+distM[tpos1][loc]+dataM[loc]['service_time']<=dataM[loc]['due_time'] and
                                    nLoc_et+distM[loc][tpos2]<=self.locLog[tpos2]['start_time']):
                                vehicle['tour'].insert(tpos+1,loc)
                                self.visited.append(loc)
                                self.locLog[loc]={'start_time':nLoc_st,
                                          'end_time':nLoc_et
                                         }
                                feasLocIN[tpos1][loc]+=1
                                feasLocIN[loc][tpos2]+=1


        #try swapping locs

#        minTL=1000
#        maxTL=0
#        for vehicle in self.vehicles:
#            if len(vehicle['tour'])>maxTL:
#                maxTL=len(vehicle['tour'])
#            if len(vehicle['tour'])<minTL:
#                minTL=len(vehicle['tour'])
#        
#        for tl in range(minTL,maxTL-1):
#            for vehicle1 in self.vehicles:
#                toRem=[]
#                if len(vehicle1['tour'])==tl and tl>0:
#                    for pos1 in range(1,len(vehicle1['tour'])):
#                        loc1=vehicle1['tour'][pos1]
#                        for vehicle2 in self.vehicles:
#                            if len(vehicle['tour'])>tl:
#                                for tpos in range(len(vehicle2['tour'])-1):
#                                    if loc1 not in toRem:
#                                        tpos1=vehicle2['tour'][tpos]
#                                        tpos2=vehicle2['tour'][tpos+1]
#                            
#                                        nLoc_st=max(self.locLog[tpos1]['end_time']+distM[tpos1][loc1],dataM[loc1]['ready_time'])
#                                        nLoc_et=nLoc_st+dataM[loc1]['service_time']
#
#                                        if (self.locLog[tpos1]['end_time']+distM[tpos1][loc1]+dataM[loc]['service_time']<=dataM[loc1]['due_time'] and
#                                            nLoc_et+distM[loc1][tpos2]<=self.locLog[tpos2]['start_time']):
#                                
#                                            vehicle2['tour'].insert(tpos+1,loc1)
#                                            toRem.append(loc1)
#                                            
#                                            #print('swapping',loc1)
#                                            self.locLog[loc1]={ 'start_time':nLoc_st,
#                                                                'end_time':nLoc_et
#                                                                }
#
#                for locr in toRem:
#                    vehicle1['tour'].remove(locr)                    
#

       
       #create solution

        self.solution['vehicles']=self.vehicles
        self.solution['visited']=self.visited
        self.solution['visitedCount']=len(self.visited)

        txtFile=open('Output/locLog.txt','w')
        for loc in self.locLog:
            txtFile.write('loc:\t')
            txtFile.write(str(loc))
            txtFile.write('\tstart_time:\t')
            txtFile.write(str(self.locLog[loc]['start_time']))
            txtFile.write('\tend_time\t')
            txtFile.write(str(self.locLog[loc]['end_time']))
            txtFile.write('\n')
        txtFile.close()

        return self.solution
    
    #            txtFile=open('Output/Attract.txt','w')
    #            for rec in attractL:
    #                txtFile.write(str(rec))
    #                txtFile.write('\t')
    #                txtFile.write(str(attractL[rec]))
    #                txtFile.write('\n')
    #            txtFile.write(str(minAttr))
    #            txtFile.close()
    #
           
               #print('feasloc:\t',feasLoc,'attr:\t',attr,'attr2:\t',attr2)
                        #eta=1/distance2
                        #attractivness[feasableLoc]=eta
                        








    # 'time':dataM[firstLoc]['ready_time']+dataM[firstLoc]['service_time']})
        
#    def calculate2(self,dataM,distM,phiM,feasLocIN,beta):
#        for veh in range(self.vehicleCount):
#            #initial location for all vehicles:
#            initLocAtt={}
#            for custData in dataM:
#                if custData['cust_no']-1 not in self.visited:
#                    initLocAtt[custData['cust_no']-1]=custData['due_time']
#            ilaS=sum(initLocAtt.values())
#
#            weights={}
#            weightsList=[]
#            for loc in initLocAtt:
#                weights[loc]=int(ilaS/initLocAtt[loc])
#                weightsList+=weights[loc]*[loc]
#            
#            firstLoc=choice(weightsList)
#            self.visited.append(firstLoc)
#            #end initial location for all vehicles
            


#            txtFile=open('Output/Solution.txt','w')
#            for veh in self.vehicles:
#                txtFile.write(str(veh))
#                txtFile.write('\n')
#            txtFile.close()
        

        



    #calculates trips for all vehicles for one ant
    def calculate2(self,dataM,distM,phiM,feasLocIN,beta): 
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
                        


                    bottomSum=0
                    for loc in attractivness:
                        bottomSum+=(phiM[vehicle['currPos']][loc]*(attractivness[loc]**beta)) 

                    probs={}
                    minProb=1
                    for attr in attractivness:
                        probs[attr]=(phiM[vehicle['currPos']][attr]*(attractivness[attr]**beta))/bottomSum
                        #print('phi:\t',phiM[vehicle['currPos']][attr],'attr',attractivness[attr])
                        if probs[attr]<minProb:
                            minProb=probs[attr]

                    #time.sleep(3)
                   
                    #here
                    cutofList=[]
                    for x in range(len(attractivness)):
                        cutofList+=(len(attractivness)-x)*[x+1]
                    cutoff=choice(cutofList)

                    probs2 = sorted(probs, key=probs.get, reverse=True)[:cutoff]
                    

                    #probabilities of selection based on attractivness
                    probList=[]
                    for prob in probs2:
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
