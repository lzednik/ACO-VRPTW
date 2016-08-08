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
feasLocIN1=len(distM)*[0]

vehicleNumber=58

ant0=Ant(vehicleCount=vehicleNumber,dataM=dataM)


for i in range(1000):
    bestSolution=ant0.calculate(dataM,distM,phiM1,feasLocIN1,1)
    
    #full solution:
    if locCount==bestSolution['visitedCount']:
        #update phi for all tours in full solution
        for vehicle in bestSolution['vehicles']:
            for loc in range(len(vehicle['tour'])-1):
                locFrom=vehicle['tour'][loc]
                locTo=vehicle['tour'][loc+1]
                phiM1[locFrom][locTo]=1.1*phiM1[locFrom][locTo]

        #evaporate all phis
        for px in range(len(phiM1)):
            for py in range(len(phiM1)):
                phiM1[px][py]=0.9*phiM1[px][py]

        vehicleNumber-=1
        ant0=Ant(vehicleCount=vehicleNumber,dataM=dataM)   

        print('iterationi:\t',i)
        print('veh count:\t',vehicleNumber+1)
        print('full solution:\t',bestSolution['visitedCount'])
        print('')

print('all done')
#iteration=0
#while iteration <200:
    
    #solution 1 is looking for a valid solution with fewer number of vehicles
#    ant1=Ant(vehicleCount=vehicleNumber-1,dataM=dataM)
#    solution1=ant1.calculate(dataM,distM,phiM1,feasLocIN1,1)
       

