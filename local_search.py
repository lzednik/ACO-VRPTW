from aco_funs import *
from local_search_funs import *
import copy

with open('Output/vehicles.txt') as f:
    lines = f.readlines()


vehicles=[]

ct=1
for line in lines:
    vehi={}
    vehi['vehNum']=ct
    tour=[int(loc.replace('\n','')) for loc in line.split(',')]
    vehi['tour']=tour
    vehicles.append(vehi)
    ct+=1


#remove one to test insert
for veh in vehicles:
    if veh['vehNum']==3:
        del veh['tour'][3]
    if veh['vehNum']==10:
        del veh['tour'][4]

input_file='Input/solomon_r101.txt'
dataM=readData(input_file)
distM=createDistanceMatrix(dataM)

visited=[]
for veh in vehicles:
    for loc in veh['tour']:
        if loc !=0:
            visited.append(loc)
visited_count=len(visited)

ls_st=time.time()
ls_change=True
while ls_change==True:
    ls_dist1=calc_dist(vehicles,distM)

#    print('visited count orig',visited_count)
#    print('distance orig',calc_dist(vehicles,distM))
#    print('**********************************')

    #insertion:
    after_insert=insert_locs(vehicles,visited,dataM,distM)
    visited=after_insert['visited']
    vehicles=after_insert['vehicles']
    print('visted count insert',len(visited))
    print('distance insert',calc_dist(vehicles,distM))
    print('**********************************')
    
    #swap two locs
    vehicles=swap_locs(vehicles,visited,dataM,distM)
    print('visted count swap',len(visited))
    print('distance swap',calc_dist(vehicles,distM))
    print('**********************************')

    
    #move loc
    vehicles=move_loc(vehicles,visited,dataM,distM)
    print('visted count move',len(visited))
    print('distance move',calc_dist(vehicles,distM))
    print('**********************************')
    
    ls_dist2=calc_dist(vehicles,distM)
    
    ls_change=False
    if ls_dist2!=ls_dist1:
        ls_change=True

run_tme=time.time()-ls_st
print('ls runtime',run_tme)

for veh in vehicles:
    t=0
    for pos in range(0,len(veh['tour'])-1):
        loc1=veh['tour'][pos]
        loc2=veh['tour'][pos+1]

        t=max(t+distM[loc1][loc2],dataM[loc2]['ready_time'])
        if t>dataM[loc2]['due_time']:
            print('Houston, we have a problem')
        t+=dataM[loc2]['service_time']

