from aco_funs import *
from aco_ls_funs import *
import time
import random


class Ant:
    def __init__(self,vehicleCount,dataM):
        self.vehicleCount=vehicleCount 
        self.locLog={}
        self.test=5
    def calculate(self,dataM,distM,phiM,depo,tour,Theta,sol_type):
        #reset
        self.visited=[]
        self.tour=[]
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
                    if choiceRand<Theta:
                        pos_next_locs=[]
                        for arch in tour:
                            if arch[0]==vehicle['currPos']:
                                pos_next_locs.append(arch[1])

                        if len(pos_next_locs) >0:
                            pos_next_loc=random.choice(pos_next_locs)
                        else:
                            pos_next_loc=99999999
                        
                        if pos_next_loc in feasLocs:
                            nextLoc=pos_next_loc
                            nlcr=True
                    
                    if nlcr==False:              
                        attractL0={}
                        attr0Sum=0
                        attractL1={}
                        attractL2={}
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
                            
                        attr0Sum=0
                        for loc in attractL0:
                            attr0Sum+=(phiM[vehicle['currPos']][loc])*(1./((attractL0[loc])**2))
                    
                        for loc in attractL0:
                            attractL1[loc]=attr0Sum/(phiM[vehicle['currPos']][loc]*(1./(attractL0[loc])**2))
                        
                        mv_al1=max(attractL1.values())
                        for loc in attractL1:
                            attractL2[loc]=int(mv_al1/float(attractL1[loc]))
                        
                        mv_al2_red=True
                        while mv_al2_red:
                            mv_al2=max(attractL2.values())
                            if mv_al2<10000:
                                mv_al2_red=False
                            else:
                                for loc in attractL2:
                                    attractL2[loc]=int(attractL2[loc]/10)
                        
                        for loc in attractL2:
                                choiceList+=attractL2[loc]*[loc]
                            #if sol_type=='sol2':
                            #    print(loc,attractL1[loc],distM[vehicle['currPos']][loc])
                            #    time.sleep(3)

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
        
        #local search
        #ls_st=time.time()
        ls_change=True
        while ls_change==True:
            ls_dist1=calc_dist(self.vehicles,distM)
            
            #insert
            after_insert=insert_locs(self.vehicles,self.visited,dataM,distM)
            self.visited=after_insert['visited']
            self.vehicles=after_insert['vehicles']
            
            #swap
            self.vehicles=swap_locs(self.vehicles,self.visited,dataM,distM)
            
            #move
            self.vehicles=move_loc(self.vehicles,self.visited,dataM,distM)
        
            ls_dist2=calc_dist(self.vehicles,distM)
    
            ls_change=False
            if ls_dist2!=ls_dist1:
                ls_change=True
        #run_tme=time.time()-ls_st
        #print('ls runtim',run_tme)

        #calculate distance and tours
        self.distance=0
        self.tour=[]
        for vehicle in self.vehicles:
            for pos in range(len(vehicle['tour'])-1):
                self.distance+=distM[vehicle['tour'][pos]][vehicle['tour'][pos+1]]
                self.tour.append((vehicle['tour'][pos],vehicle['tour'][pos+1]))

        solution={}
        solution['vehicles']=self.vehicles
        solution['visited']=self.visited
        solution['tour']=self.tour

        solution['visitedCount']=len(self.visited)
        solution['vehicleCount']=self.vehicleCount
        solution['distance']=round(self.distance,2)
        
        return solution


