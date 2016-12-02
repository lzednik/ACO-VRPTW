
from funs import *
dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)


#tour=[0,92,42,15,87,57,97,0]
#tour=[0,27,69,76,79,3,54,24,80,0]
#tour=[0,95,98,16,86,91,100,0]
#tour=[0,36,47,19,8,46,17,0]
#tour=[0,14,44,38,43,13,0]
#tour=[0,39,23,67,55,25,0]
#tour=[0,31,88,7,10,0]
#tour=[0,62,11,90,20,32,70,0]
#tour=[0,2,21,73,41,56,4,0]
#tour=[0,5,83,61,85,37,93,0]
#tour=[0,52,6,0]
#tour=[0,65,71,81,50,68,0]
#tour=[0,59,99,94,96,0]
#tour=[0,72,75,22,74,58,0]
#tour=[0,33,29,78,34,35,77,0]
#tour=[0,30,51,9,66,1,0]
#tour=[0,45,82,18,84,60,89,0]
#tour=[0,28,12,40,53,26,0]
tour=[0,63,64,49,48,0]
#

t=0

for pos in range(len(tour)-1):
    loc=tour[pos]
    next_loc=tour[pos+1]
    
    dnl=distM[loc][next_loc]
    start_time=max(t+dnl,dataM[next_loc]['ready_time'])
    done_time=start_time+dataM[next_loc]['service_time']
    
    check='PROBLEM'
    if start_time>=dataM[next_loc]['ready_time'] and start_time <=dataM[next_loc]['due_time']:
        check='OK'
    #print('time\t',t,'\tdist\t',dnl)    
    #print('ready\t',dataM[next_loc]['ready_time'], '\tdue\t',dataM[next_loc]['due_time'],'\tactual\t',start_time)
    print('check\t',check)
    #print('')

    t=done_time


