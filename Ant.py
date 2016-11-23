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

    def calculate(self,dataM,distM,phiM,feasLocIN,beta,iteration,c,lag):
        #reset
        self.visited=[]
        self.distance=0
        self.time=0
        self.vehicles=[]
        
        #initial location
        il1={}
        for loc in range(1,len(dataM)):
            il1[loc]=dataM[loc]['ready_time']+dataM[loc]['service_time']
        
        mil=max(il1.values())
        il1=sorted(il1.items(), key=lambda x: x[1])
        ilPrime0=il1[0:self.vehicleCount]
        ilBackup0=il1[self.vehicleCount:len(dataM)]
        
        ilPrime=[]
        for x in ilPrime0:
            ilPrime+=(int(mil/x[1])**2)*[x[0]]
        ilBackup=[]
        for x in ilBackup0:
            ilBackup+=(int(mil/x[1])**2)*[x[0]]
        
        
        for veh in range(self.vehicleCount):
            if ilPrime:
                ilChoice=choice(ilPrime)
                ilPrime[:] = [x for x in ilPrime if x != ilChoice]
            else:
                ilChoice=choice(ilBackup)  
                ilBackup[:] = [x for x in ilBackup if x != ilChoice]
            init_pos=ilChoice
            
            self.vehicles.append({  'vehNum':veh+1,
                                    'tour':[init_pos],
                                    'currPos':init_pos,
                                    'time':dataM[init_pos]['ready_time']+dataM[init_pos]['service_time']})
            self.visited.append(init_pos)
            self.locLog[init_pos]={'start_time':dataM[init_pos]['ready_time'],
                              'end_time':dataM[init_pos]['ready_time']+dataM[init_pos]['service_time']}
            

        for vehicle in self.vehicles:
            #init pos

            flocs=True
            while flocs==True:
                #feasable locs
                feasLocs=[]
                for loc in range(1,len(dataM)):
                    #if loc not in self.visited and vehicle['time']+distM[vehicle['currPos']][loc]+dataM[loc]['service_time']<=dataM[loc]['due_time']:
                    if loc not in self.visited and vehicle['time']+distM[vehicle['currPos']][loc]<=dataM[loc]['due_time']:
                        feasLocs.append(loc)
                
                if feasLocs:
                    
                    attractL0={}
                    attractL1={}
                    choiceList=[]
                    attIN0 ={}
                    #attractivness of feasable locs
                    
                    for feasLoc in feasLocs:
                        distanceToFeasLoc=distM[vehicle['currPos']][feasLoc]
                        feasLocReadyTime=dataM[feasLoc]['ready_time']
                        feasLocDueTime=dataM[feasLoc]['due_time']
                        delivery_time=max(vehicle['time']+distanceToFeasLoc,feasLocReadyTime)
                        delta_time=delivery_time-vehicle['time']
                        
                        attr0=delta_time*(feasLocDueTime-vehicle['time'])
                        
                        #attract0
                        #attractL0[feasLoc]=attr0*(1+0.1*feasLocIN[vehicle['currPos']][feasLoc]*(1+lag))
                        attractL0[feasLoc]=attr0
                        attIN0[feasLoc]=feasLocIN[vehicle['currPos']][feasLoc]
                    
                    

                    maxAttr0=max(attractL0.values())
                    maxIN0=max(attIN0.values())
                    
                   
                                        
                    for loc in attractL0:
                        #attractL1[loc]=((1+phiM[vehicle['currPos']][loc])*float(maxAttr0/attractL0[loc])**2)*(maxIN0/attIN0[loc])
                        attractL1[loc]=(1+phiM[vehicle['currPos']][loc])*float(maxAttr0/attractL0[loc])**2

                    
                    for loc in attractL1:
                        choiceList+=int(attractL1[loc])*[loc]
                        c.execute('''INSERT INTO Attr(iter,vehNum, currLoc, nextLoc, attr0, attr1)
                                   VALUES(?,?,?,?,?,?)''', (iteration,vehicle['vehNum'],vehicle['currPos'],loc,attractL0[loc],attractL1[loc]))

                    
                    nextLoc=choice(choiceList)
                       
                    self.visited.append(nextLoc)
                   
                    start_time=max(vehicle['time']+distM[vehicle['currPos']][nextLoc],dataM[nextLoc]['ready_time'])gt
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
        for loc in range(1,len(dataM)):
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
                                print(vehicle['tour'])
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
                                feasLocIN[tpos1][tpos2]-=1


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


        return self.solution
  
