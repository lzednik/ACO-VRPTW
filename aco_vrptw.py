from aco_funs import *
from aco_ant import Ant

print('run starting')

dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)

depo=0
locCount=len(dataM)

initSolution=initSolution(depo,dataM,distM)


phiM1= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]



vehicleCount=initSolution['vehicleCount']

tour=initSolution['tour']
tour_fl=initSolution['tour_fl']

for iteration in range(300):

    ants=Ant(vehicleCount=vehicleCount,dataM=dataM)
    solution=ants.calculate(dataM,distM,phiM1,depo,tour,tour_fl)
    
    #Full Solution
    if solution['visitedCount']==locCount-1:
        vehicleCount-=1
        tour=solution['tour']
        tour_fl=solution['tour_fl']
        print('iteration\t',iteration)
        print('vehicleCount\t',solution['vehicleCount'])
        print('****************\n')
#for vehicle in solution['vehicles']:
#    print(vehicle['tour'])

print('run finished')
