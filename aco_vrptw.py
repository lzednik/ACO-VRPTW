from aco_funs import *
from aco_ant import Ant
import sqlite3


print('run starting')

dtb='Output/Ants.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()
c.execute('DELETE FROM Solutions')


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


for iteration in range(10):
    visitedArcs=[]
    for colony in range(20):

        ants=Ant(vehicleCount=vehicleCount,dataM=dataM)
        solution=ants.calculate(dataM,distM,phiM1,depo,tour,tour_fl)
        
        #Full Solution
        if solution['visitedCount']==locCount-1:
            
            #log full sols
            c.execute('''INSERT INTO Solutions(iter,colony, vehCount,visitedCount,visited)
                         VALUES(?,?,?,?,?)''', (iteration,colony,vehicleCount,solution['visitedCount'],str(solution['visited']))) 

            #log Vehicles
            for vehicle in solution['vehicles']:
                c.execute('''INSERT INTO Vehicles(iter,colony, vehNum,tour)
                            VALUES(?,?,?,?)''', (iteration,colony,vehicle['vehNum'],str(vehicle['tour']))) 
            
            
            #for vehicle in solution['vehicles']:
            #    vehNum=vehicle['vehNum']
            #    c.execute('''INSERT INTO Summary(iter,vehNum, tour)
            #             VALUES(?,?,?)''', (iteration,vehicle['vehNum'],str(vehicle['tour'])))


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

conn.commit()
conn.close()

print('run finished')
