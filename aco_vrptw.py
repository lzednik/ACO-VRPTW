from aco_funs import *
from aco_ant import Ant

print('run starting')

dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)

depo=0
locCount=len(dataM)

initSolution=initSolution(depo,dataM,distM)


phiM0= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]
phiM1= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]


vehicleCount=initSolution['vehicleCount']

tour=initSolution['tour']
tour_fl=initSolution['tour_fl']

visitedArcs=[]
bestArcs=[]
bestSolution=initSolution


for iteration in range(100):
    visitedArcs=[]
    for colony in range(10):

        ants=Ant(vehicleCount=vehicleCount,dataM=dataM)
        solution=ants.calculate(dataM,distM,phiM1,depo,tour,tour_fl)
        
        #Full Solution
        if solution['visitedCount']==locCount-1:
            vehicleCount-=1
            tour=solution['tour']
            tour_fl=solution['tour_fl']
            
            for loc in tour:
                visitedArcs.append((loc,tour[loc]))
            for loc in tour_fl:
                visitedArcs.append((depo,loc))

            if bestSolution['vehicleCount']>solution['vehicleCount']:
                bestSolution=solution
                for loc in tour:
                    bestArcs.append((loc,tour[loc]))
                for loc in tour_fl:
                    bestArcs.append((depo,loc))

            print('iteration\t',iteration)
            print('colony\t\t',colony)
            print('vehicleCount\t',solution['vehicleCount'])
            print('****************\n')


    visitedArcs=list(set(visitedArcs))
    #evaporate
    alpha=0.1

    for arc in visitedArcs:
        locFrom=arc[0]
        locTo=arc[1]
        phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha*phiM0[locFrom][locTo]

    for arc in bestArcs:
        locFrom=arc[0]
        locTo=arc[1]
        phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha/bestSolution['distance']

    if iteration%50==0:
        print('*******************')
        print('iteration\t',iteration)
        print('*******************')
print('run finished')
