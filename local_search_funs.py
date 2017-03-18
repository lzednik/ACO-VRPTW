import time
import copy

def move_loc(vehicles,visited,dataM,distM):
    if len(visited)==len(dataM)-1:
        
        Swap=False
        for veh in vehicles:
            for pos in range(1,len(veh['tour'])-1):
                loc=veh['tour'][pos]
                curr_dist=calc_dist(vehicles,distM)
                bestNewDist={'dist':curr_dist,'vehNum1':-1,'vehNum2':-1}
                
                vehi0=copy.deepcopy(vehicles)

                for veh0 in vehi0:
                    if veh0['vehNum']==veh['vehNum']:
                        del veh0['tour'][pos]

                for veh0 in vehi0:
                    for pos1 in range(1,len(veh0['tour'])-1):
                        veh0['tour'].insert(pos1,loc)
                        if check_tour_feas(veh0['tour'],dataM,distM):
                            curr_dist=calc_dist(vehi0,distM)
                            if curr_dist<bestNewDist['dist']:
                                Swap=True
                                bestNewDist['dist']=curr_dist
                                bestNewDist['vehNum']=veh0['vehNum']
                                bestNewDist['pos']=pos1

                        del veh0['tour'][pos1]
                
                if Swap:
                    break
            if Swap:
                break

        if Swap:
            vehicles=[veh for veh in vehi0]

    return vehicles


def move_loc2(vehicles,visited,dataM,distM):
    if len(visited)==len(dataM)-1:
        for veh in vehicles:
            for pos in range(1,len(veh['tour'])-1):
                print(pos,veh['tour'][pos])
                loc=veh['tour'][pos]
                curr_dist=calc_dist(vehicles,distM)
                bestNewDist={'dist':curr_dist,'vehNum1':-1,'vehNum2':-1}
                
                vehi0=copy.deepcopy(vehicles)

                for veh0 in vehi0:
                    if veh0['vehNum']==veh['vehNum']:
                        del veh0['tour'][pos]

                Swap=False
                for veh0 in vehi0:
                    for pos1 in range(1,len(veh0['tour'])-1):
                        veh0['tour'].insert(pos1,loc)
                        if check_tour_feas(veh0['tour'],dataM,distM):
                            curr_dist=calc_dist(vehi0,distM)
                            if curr_dist<bestNewDist['dist']:
                                Swap=True
                                bestNewDist['dist']=curr_dist
                                bestNewDist['vehNum']=veh0['vehNum']
                                bestNewDist['pos']=pos1

                        del veh0['tour'][pos1]
        
                if Swap==True:
                    del veh['tour'][pos]
                    for vehx in vehicles:
                        if vehx['vehNum']==bestNewDist['vehNum']:
                            vehx['tour'].insert(bestNewDist['pos'],loc)

            
    return vehicles

def swap_locsSLOW(vehicles,visited,dataM,distM):
    if len(visited)==len(dataM)-1:
        Swap=False
        for veh1 in vehicles:
            for pos1 in range(1,len(veh1['tour'])-1):
                loc1=veh1['tour'][pos1]

                curr_dist=calc_dist(vehicles,distM) 
                bestNewDist={'dist':curr_dist}
                for veh2 in vehicles:
                    if veh1['vehNum']<=veh2['vehNum']:
                        for pos2 in range(1,len(veh2['tour'])-1):
                            if veh1['vehNum'] == veh2['vehNum'] and pos1==pos2:
                                pass
                            else:
                                loc2=veh2['tour'][pos2]
                                vehi0=copy.deepcopy(vehicles)
                                
                                tour_feas=0
                                for veh0 in vehi0:
                                    if veh0['vehNum']==veh1['vehNum']:
                                        veh0['tour'][pos1]=loc2
                                        if check_tour_feas(veh0['tour'],dataM,distM):
                                            tour_feas+=1
                                    if veh0['vehNum']==veh2['vehNum']:
                                        veh0['tour'][pos2]=loc1
                                        if check_tour_feas(veh0['tour'],dataM,distM):
                                            tour_feas+=1
                                
                                if tour_feas==2:
                                    newDist=calc_dist(vehi0,distM)
                                    if newDist<bestNewDist['dist']:
                                        Swap=True
                                        bestNewDist['dist']=newDist
                                        bestNewDist['vehicles']=copy.deepcopy(vehi0)
                            
                if Swap:
                    break
            if Swap:
                break

        if Swap:
            vehicles=copy.deepcopy(bestNewDist['vehicles'])
#            for vehx1 in vehicles:
#                for vehx2 in bestNewDist['vehicles']:
#                    if vehx1['vehNum']==vehx2['vehNum']:
#                        vehx1['tour']=[locx for locx in vehx2['tour']]
    return vehicles

def insert_locs(vehicles,visited,dataM,distM):
    if len(visited)<len(dataM)-1:
        for loc_to_insert in range(1,len(dataM)):
            if loc_to_insert not in visited:
                bestNewDist={'dist':1000000,'vehNum':-1}
                
                
                for veh in vehicles:
                    for pos_to_insert in range(1,len(veh['tour'])-1):
                        veh_tour=[loc for loc in veh['tour']]
                        veh_tour.insert(pos_to_insert,loc_to_insert)
                        if check_tour_feas(veh_tour,dataM,distM):
                            #print('insert is possible')
                            vehNum=veh['vehNum']
                            newDist=0
                            for veh0 in vehicles:
                                if veh0['vehNum']==vehNum:
                                    for p in range(0,len(veh_tour)-1):
                                        newDist+=distM[veh_tour[p]][veh_tour[p+1]]
                                else:
                                    for p in range(0,len(veh0['tour'])-1):
                                        newDist+=distM[veh0['tour'][p]][veh0['tour'][p+1]]

                            if bestNewDist['dist']>newDist:
                                bestNewDist['dist']=newDist
                                bestNewDist['vehNum']=vehNum
                                bestNewDist['pos']=pos_to_insert
                                bestNewDist['loc']=loc_to_insert

                if bestNewDist['vehNum']!=-1:
                    for veh in vehicles:
                        if veh['vehNum']==bestNewDist['vehNum']:
                            veh['tour'].insert(bestNewDist['pos'],bestNewDist['loc'])                                    
                            visited.append(bestNewDist['loc'])
    retvar={}
    retvar['vehicles']=vehicles
    retvar['visited']=visited

    return retvar



def check_tour_feas(veh_tour,dataM,distM):
    t=0
    route_feasable=True
    for pos in range(0,len(veh_tour)-1):
        loc1=veh_tour[pos]
        loc2=veh_tour[pos+1]
        
        t=max(t+distM[loc1][loc2],dataM[loc2]['ready_time'])
        if t>dataM[loc2]['due_time']:
            route_feasable=False

        t+=dataM[loc2]['service_time']

    return route_feasable


def calc_dist(vehicles,distM):
    dist=0
    for veh in vehicles:
        for pos in range(0,len(veh['tour'])-1):
            dist+=distM[veh['tour'][pos]][veh['tour'][pos+1]]
    return round(dist,2)


def swap_locs(vehicles,visited,dataM,distM):
    if len(visited)==len(dataM)-1:
        for veh1 in vehicles:
            for pos1 in range(1,len(veh1['tour'])-1):
                loc1=veh1['tour'][pos1]

                Swap=False
                curr_dist=calc_dist(vehicles,distM) 
                bestNewDist={'dist':curr_dist,'vehNum1':-1,'vehNum2':-1}
                for veh2 in vehicles:
                    if veh1['vehNum']<veh2['vehNum']:
                        for pos2 in range(1,len(veh2['tour'])-1):
                            loc2=veh2['tour'][pos2]
                            
                            l1_tour=[x for x in veh1['tour']]
                            l2_tour=[x for x in veh2['tour']]
        
                            l1_tour[pos1]=loc2
                            l2_tour[pos2]=loc1
                            if check_tour_feas(l1_tour,dataM,distM) and check_tour_feas(l2_tour,dataM,distM):
                                #compute dist
                                newDist=0
                                for veh0 in vehicles:
                                    if veh0['vehNum']==veh1['vehNum']:
                                        for p in range(0,len(l1_tour)-1):
                                            newDist+=distM[l1_tour[p]][l1_tour[p+1]]
                                    elif veh0['vehNum']==veh2['vehNum']:
                                        for p in range(0,len(l2_tour)-1):
                                            newDist+=distM[l2_tour[p]][l2_tour[p+1]]
                                    else:
                                        for p in range(0,len(veh0['tour'])-1):
                                            newDist+=distM[veh0['tour'][p]][veh0['tour'][p+1]]

                                if newDist<bestNewDist['dist']:
                                    Swap=True
                                    bestNewDist['dist']=newDist
                                    bestNewDist['vehNum1']=veh1['vehNum']
                                    bestNewDist['tour1']=l1_tour
                                    bestNewDist['vehNum2']=veh2['vehNum']
                                    bestNewDist['tour2']=l2_tour
                                    #print('old tour 1',veh1['tour'])
                                    #print('new tour 1',l1_tour)
                                    #print('old tour 2',veh2['tour'])
                                    #print('new tour 2',l2_tour)
                                    #print('****************************')
                                    #time.sleep(10)
                            
                if Swap==True:
                    for veh0 in vehicles:
                        if veh0['vehNum']==bestNewDist['vehNum1']:
                            veh0['tour']=bestNewDist['tour1']
                        if veh0['vehNum']==bestNewDist['vehNum2']:
                            veh0['tour']=bestNewDist['tour2']
    return vehicles
