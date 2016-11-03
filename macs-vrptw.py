from funs import *
from ant import Ant
import time
import pickle
from os import path

dataM=readData('Input/solomon_r101.txt')
locCount=len(dataM)

txtFile=open('Output/DataM.txt','w')
for rec in dataM:
    txtFile.write(str(rec))
    txtFile.write('\n')
txtFile.close()

distM=createDistanceMatrix(dataM)

phiM1=createPheromoneMatix(size=len(distM),distance=1888)
feasLocIN1= [[1 for i in range(locCount)] for j in range(locCount)]

vehicleNumber=35

ant0=Ant(vehicleCount=vehicleNumber,dataM=dataM)


for i in range(500):
    if i%100 == 0:
        print('Iteration:',i)

    bestSolution=ant0.calculate(dataM,distM,phiM1,feasLocIN1,1)
        
    #evaporate all phis
    #uncomment to use pheromones
    for px in range(len(phiM1)):
        for py in range(len(phiM1)):
            phiM1[px][py]=0.98*phiM1[px][py]

        
    #full solution:
    if locCount==bestSolution['visitedCount']:
        #evaporate all phis
        for px in range(len(phiM1)):
            for py in range(len(phiM1)):
                phiM1[px][py]=0.9*phiM1[px][py]

        #update phi
        for vehicle in bestSolution['vehicles']:
            for loc in range(len(vehicle['tour'])-1):
                locFrom=vehicle['tour'][loc]
                locTo=vehicle['tour'][loc+1]
                #uncomment the phiM1 below to use pheromones
                phiM1[locFrom][locTo]=1.10*phiM1[locFrom][locTo]

        vehicleNumber-=1
        ant0=Ant(vehicleCount=vehicleNumber,dataM=dataM)   

        print('****************************************')       
        print('iterationi:\t',i)
        print('veh count:\t',vehicleNumber+1)
        print('full solution:\t',bestSolution['visitedCount'])
        print('****************************************')
        print('')

#write results for checking
txtFile=open('Output/Results.txt','w')
for vehicle in bestSolution['vehicles']:
    #print(vehicle['tour'])
    txtFile.write(str(vehicle['tour']))
    txtFile.write('\n\n')
    
    for pos in range(len(vehicle['tour'])):
        loc=vehicle['tour'][pos]           
        if pos<len(vehicle['tour'])-1:
            nloc=vehicle['tour'][pos+1]  
        txtFile.write('loc:\t')
        txtFile.write(str(loc))
        txtFile.write('\tready_time:\t')
        txtFile.write(str(dataM[loc]['ready_time']))
        txtFile.write('\tservice_time"\t')
        txtFile.write(str(dataM[loc]['service_time']))
        txtFile.write('\tdue_time"\t')
        txtFile.write(str(dataM[loc]['due_time']))
        if pos<len(vehicle['tour'])-1:
            txtFile.write('\tdist to next"\t')
            txtFile.write(str(distM[loc][nloc]))
        txtFile.write('\n')

    txtFile.write('*******************************************\n\n')

txtFile.close()
           
for vehicle in bestSolution['vehicles']:
    print(vehicle['tour'])




print('all done')
#iteration=0
#while iteration <200:
    
    #solution 1 is looking for a valid solution with fewer number of vehicles
#    ant1=Ant(vehicleCount=vehicleNumber-1,dataM=dataM)
#    solution1=ant1.calculate(dataM,distM,phiM1,feasLocIN1,1)
       

