from funs import *
from Ant import Ant
import time

dataM=readData('solomon_r101.txt')
distM=createDistanceMatrix(dataM)

#print(dataM[1])

phiM1=createPheromoneMatix(size=len(distM),distance=1888)
feasLocIN1=len(distM)*[0]

phiM2=createPheromoneMatix(size=len(distM),distance=1888)
feasLocIN2=len(distM)*[0]


#nnSearch(0,distM,dataM)
#print(dataM[1])

vehicleNumber=60

ant0=Ant(vehicleCount=vehicleNumber,depo=0)
bestSolution=ant0.calculate(dataM,distM,phiM1,feasLocIN1,2)

iteration=0
while iteration <300:
    #print('iteration number',antCount)
    
    ant1=Ant(vehicleCount=vehicleNumber-1,depo=0)
    solution1=ant1.calculate(dataM,distM,phiM1,feasLocIN1,2)
       
    if solution1['visitedCount']==101:
        vehicleNumber-=1
        
        phiM2=createPheromoneMatix(size=len(distM),distance=1888)
        feasLocIN2=len(distM)*[0]


        #update pheromones
        for vehicle in solution1['vehicles']:
            for index in range(0,len(vehicle['tour'])-1):
                fromLoc=vehicle['tour'][index]
                toLoc=vehicle['tour'][index+1]
                phiM1[fromLoc][toLoc]=(1-0.1)*phiM1[fromLoc][toLoc]+0.1/solution1['distance']
            
        bsChange=False
        if bestSolution['vehicleCount']>solution1['vehicleCount']:
            bestSolution=solution1
            bsChange=True
        elif bestSolution['vehicleCount']==solution1['vehicleCount'] and bestSolution['distance']>solution1['distance']:
            bestSolution=solution1
            bsChange=True
        
        if bsChange==True:

            print('**********')
            print('The best solution currently is:')
            #for index,vehicle in enumerate(solution['vehicles']):
            #    print('Vehicle',index+1,'\ttour:',vehicle['tour'])
            #    print('')
            print('Vehicle count is:',solution1['vehicleCount'])
            print('Visited count is:',solution1['visitedCount'])
            print('Distance traveled is:',solution1['distance'])
            print('')
            print('')
            #time.sleep(2)
    


    ant2=Ant(vehicleCount=vehicleNumber,depo=0)
    solution2=ant2.calculate(dataM,distM,phiM2,feasLocIN2,2)
    
    if solution2['visitedCount']==101:

        #update pheromones
        for vehicle in solution2['vehicles']:
            for index in range(0,len(vehicle['tour'])-1):
                fromLoc=vehicle['tour'][index]
                toLoc=vehicle['tour'][index+1]
                phiM2[fromLoc][toLoc]=(1-0.1)*phiM2[fromLoc][toLoc]+0.1/solution2['distance']
            
        bsChange=False
        if bestSolution['distance']>solution2['distance']:
            bestSolution=solution2
            bsChange=True
        
        if bsChange==True:
            print('**********')
            print('The best solution currently is:')
            #for index,vehicle in enumerate(solution['vehicles']):
            #    print('Vehicle',index+1,'\ttour:',vehicle['tour'])
            #    print('')
            print('Vehicle count is:',solution2['vehicleCount'])
            print('Visited count is:',solution2['visitedCount'])
            print('Distance traveled is:',solution2['distance'])
            print('')
            print('')
            #time.sleep(2)
    
    iteration+=1





'''
txtFile = open('Output.txt', 'w')
txtFile.write('Vehicle Log\n\n')
txtFile.close()

txtFile = open("Output.txt","a")
for index,vehicle in enumerate(solution['vehicles']):
    txtFile.write('Vehicle\t')
    txtFile.write(str(index+1))
    txtFile.write('\ttour:\t')
    txtFile.write(str(vehicle['tour']))
    txtFile.write('\n')
txtFile.close()
'''

