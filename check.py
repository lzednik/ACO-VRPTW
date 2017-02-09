
from funs import *
dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)


#tour=[0,92,42,15,87,57,97,0]
#tour=[0, 92, 95, 40, 53, 97, 91, 100, 0]
#tour=[0, 63, 62, 88, 18, 10, 48, 58, 0]
#tour=[0, 39, 21, 73, 22, 26, 4, 25, 0]
#tour=[0, 31, 30, 51, 9, 50, 24, 77, 0]
#tour=[0, 59, 5, 82, 19, 49, 17, 93, 0]
#tour=[0, 65, 71, 78, 34, 35, 80, 0]
#tour=[0, 36, 47, 7, 46, 1, 70, 0]
#tour=[0, 45, 83, 61, 85, 84, 96, 60, 89, 0]
#tour=[0, 28, 69, 76, 79, 3, 68, 0]
#tour=[0, 72, 23, 67, 56, 74, 0]
#tour=[0, 42, 2, 75, 41, 55, 0]
#tour=[0, 33, 29, 81, 20, 32, 0]
#tour=[0, 27, 52, 99, 6, 54, 0]
#tour=[0, 44, 38, 37, 13, 0]
#tour=[0, 98, 16, 86, 43, 0]
#tour=[0, 12, 94, 0]
#tour=[0, 14, 15, 87, 57, 0]
#tour=[0, 11, 8, 0]
#tour=[0, 64, 90, 66, 0]
tour=[0,27,69,76,79,3,54,24,80,0]

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


