from aco_funs import *
from aco_ant import Ant
import sqlite3


print('run starting')

dtb='Output/aco_tuner.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()
#c.execute('DELETE FROM Solutions')
c.execute('DELETE FROM RunSum')


dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)
depo=0
locCount=len(dataM)

initSolution=initSolution(depo,dataM,distM)



phiFrc=0.1

while phiFrc<=0.9:

    for run in range(100):
        alpha=0.1
        

        phiM0= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]
        phiM1= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]
        phiM2= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]


        vehicleCount1=initSolution['vehicleCount']
        vehicleCount2=initSolution['vehicleCount']

        tour1=initSolution['tour']
        tour2=initSolution['tour']
        tour_fl1=initSolution['tour_fl']
        tour_fl2=initSolution['tour_fl']

        bestArcs1=[]
        bestArcs2=[]
        bestSolution=initSolution

        bsiter1=0
        bsiter2=0
        
        for iteration in range(50):
            visitedArcs1=[]
            visitedArcs2=[]

            for colony in range(20):

                colony1=Ant(vehicleCount=vehicleCount1,dataM=dataM)
                colony2=Ant(vehicleCount=vehicleCount2,dataM=dataM)
                solution1=colony1.calculate(dataM,distM,phiM1,depo,tour1,tour_fl1)
                solution2=colony2.calculate(dataM,distM,phiM2,depo,tour2,tour_fl2)
                
                #Full Solution 1
                if solution1['visitedCount']==locCount-1:
                    
                    #log full sols
                    #c.execute('''INSERT INTO Solutions(iter,colony, vehCount,visitedCount,visited)
                    #             VALUES(?,?,?,?,?)''', (iteration,colony,vehicleCount,solution['visitedCount'],str(solution['visited']))) 

                    #log Vehicles
                    #for vehicle in solution['vehicles']:
                    #    c.execute('''INSERT INTO Vehicles(iter,colony, vehNum,tour)
                    #                VALUES(?,?,?,?)''', (iteration,colony,vehicle['vehNum'],str(vehicle['tour']))) 
                    
                    
                    vehicleCount1-=1
                    tour1=solution1['tour']
                    tour_fl1=solution1['tour_fl']
                    

                    if bestSolution['vehicleCount']>solution1['vehicleCount']:
                        bestSolution=solution1
                        bsiter1=iteration
                        bestArcs1=[]
                        vehicleCount2=solution1['vehicleCount']
                        for loc in tour1:
                            bestArcs1.append((loc,tour1[loc]))
                        for loc in tour_fl1:
                            bestArcs1.append((depo,loc))
                    
                        print('colony 1')
                        print('phiFrc\t',phiFrc)
                        print('run\t',run)
                        print('iteration\t',iteration)
                        print('colony\t\t',colony)
                        print('vehicleCount\t',solution1['vehicleCount'])
                        print('distance\t',solution1['distance'])
                        print('****************\n')

                #Full Solution 2
                if solution2['visitedCount']==locCount-1:
                    
                    #log full sols
                    #c.execute('''INSERT INTO Solutions(iter,colony, vehCount,visitedCount,visited)
                    #             VALUES(?,?,?,?,?)''', (iteration,colony,vehicleCount,solution['visitedCount'],str(solution['visited']))) 

                    #log Vehicles
                    #for vehicle in solution['vehicles']:
                    #    c.execute('''INSERT INTO Vehicles(iter,colony, vehNum,tour)
                    #                VALUES(?,?,?,?)''', (iteration,colony,vehicle['vehNum'],str(vehicle['tour']))) 
                    
                    
                    tour2=solution2['tour']
                    tour_fl2=solution2['tour_fl']
                    
                    if bestSolution['distance']>solution2['distance']:
                        bestSolution=solution2
                        bsiter2=iteration
                        bestArcs2=[]
                        for loc in tour2:
                            bestArcs2.append((loc,tour2[loc]))
                        for loc in tour_fl2:
                            bestArcs2.append((depo,loc))
                        
                        print('colony 2')
                        print('phiFrc\t',phiFrc)
                        print('run\t',run)
                        print('iteration\t',iteration)
                        print('colony\t\t',colony)
                        print('vehicleCount\t',solution2['vehicleCount'])
                        print('distance\t',solution2['distance'])
                        print('****************\n')

                #evaporation
                for loc in solution1['tour']:
                    locFrom=loc
                    locTo=solution1['tour'][loc]
                    phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha*phiM0[locFrom][locTo]
               
                for loc in solution2['tour']:
                    locFrom=loc
                    locTo=solution2['tour'][loc]
                    phiM2[locFrom][locTo]=(1-alpha)*phiM2[locFrom][locTo]+alpha*phiM0[locFrom][locTo]
               
                

            #phi updates

            for arc in bestArcs1:
                locFrom=arc[0]
                locTo=arc[1]
                phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha/(initSolution['distance']*phiFrc)

            for arc in bestArcs2:
                locFrom=arc[0]
                locTo=arc[1]
                phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha/bestSolution['distance']

        
            #if iteration%50==0:
            #    print('*******************')
            #    print('iteration\t',iteration)
            #    print('*******************')
        
        
        #log run
        c.execute('''INSERT INTO RunSum(run,bsiter1,bsiter2,phiFrc,vehCount, distance)
                     VALUES(?,?,?,?,?,?)''', (run,bsiter1,bsiter2,phiFrc,bestSolution['vehicleCount'],bestSolution['distance'])) 
    phiFrc+=0.1
    phiFrc=round(phiFrc,1)        
conn.commit()
conn.close()

print('run finished')
