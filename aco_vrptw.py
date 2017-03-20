from aco_funs import *
from aco_ant import Ant
import sqlite3
import time

def aco_setup(input_file,depo):
    dataM=readData(input_file)
    distM=createDistanceMatrix(dataM)
    locCount=len(dataM)

    initSol=initSolution(depo,dataM,distM)
    
    rt={    'dataM':dataM,
            'distM':distM,
            'locCount':locCount,
            'initSol':initSol}
    return(rt)    

def aco_run(dataM,distM,depo,locCount,initSolution,alpha,BRCP,iterCount,colSize):
    phi01=float(1)/(len(dataM)*initSolution['vehicleCount'])
    phi02=float(1)/(len(dataM)*initSolution['distance'])

    phiM1= [[float(1)/initSolution['vehicleCount'] for i in range(locCount)] for j in range(locCount)]
    phiM2= [[float(1)/initSolution['distance'] for i in range(locCount)] for j in range(locCount)]


    vehicleCount1=initSolution['vehicleCount']-1
    vehicleCount2=initSolution['vehicleCount']

    tour1=initSolution['tour']
    tour2=initSolution['tour']

    bestArcs1=[]
    bestArcs2=[]
    bestSolution=initSolution


    for iteration in range(iterCount):
        #visitedArcs1=[]
        #visitedArcs2=[]
        for colony in range(colSize):
            colony1=Ant(vehicleCount=vehicleCount1,dataM=dataM)
            solution1=colony1.calculate(dataM,distM,phiM1,depo,bestSolution['tour'],BRCP,'sol1')

            
            solution1['iteration']=iteration
            solution1['colony']=colony
            solution1['alpha']=alpha
            solution1['BRCP']=BRCP

            
            sol1_found=False
            #Full Solution 1
            if solution1['visitedCount']==locCount-1:
                vehicleCount1-=1
                tour1=solution1['tour']
                

                if bestSolution['vehicleCount']>solution1['vehicleCount']:
                    sol1_found=True
                    bestSolution=solution1
                    bestArcs1=[]
                    vehicleCount2=solution1['vehicleCount']
                    for loc in tour1:
                        bestArcs1.append(loc)
                
                    print('colony 1')
                    print('alpha\t',alpha)
                    print('iteration\t',iteration)
                    print('colony\t\t',colony)
                    print('vehicleCount\t',solution1['vehicleCount'])
                    print('distance\t',solution1['distance'])
                    print('****************\n')

            if sol1_found==False:
                colony2=Ant(vehicleCount=vehicleCount2,dataM=dataM)
                solution2=colony2.calculate(dataM,distM,phiM2,depo,bestSolution['tour'],BRCP,'sol2')

                solution2['iteration']=iteration
                solution2['colony']=colony
                solution2['alpha']=alpha
                solution2['BRCP']=BRCP
                
                #Full Solution 2
                if solution2['visitedCount']==locCount-1:
                    tour2=solution2['tour']
                    if bestSolution['distance']>solution2['distance']:
                        bestSolution=solution2
                        bestArcs2=[]
                        for loc in tour2:
                            bestArcs2.append(loc)
                        
                        print('colony 2')
                        print('alpha\t',alpha)
                        print('iteration\t',iteration)
                        print('colony\t\t',colony)
                        print('vehicleCount\t',solution2['vehicleCount'])
                        print('distance\t',solution2['distance'])
                        print('****************\n')
            

            #evaporation
            for loc in solution1['tour']:
                locFrom=loc[0]
                locTo=loc[1]
                #phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha*phiM01[locFrom][locTo]
                phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha*phi01
           
            if sol1_found==False:
                for loc in solution2['tour']:
                    locFrom=loc[0]
                    locTo=loc[1]
                    #phiM2[locFrom][locTo]=(1-alpha)*phiM2[locFrom][locTo]+alpha*phiM02[locFrom][locTo]
                    phiM2[locFrom][locTo]=(1-alpha)*phiM2[locFrom][locTo]+alpha*phi02
           
        #phi updates

        for arc in bestArcs1:
            locFrom=arc[0]
            locTo=arc[1]
            phiM1[locFrom][locTo]=(1-alpha)*phiM1[locFrom][locTo]+alpha/((bestSolution['vehicleCount']))

        for arc in bestArcs2:
            locFrom=arc[0]
            locTo=arc[1]
            phiM2[locFrom][locTo]=(1-alpha)*phiM2[locFrom][locTo]+alpha/bestSolution['distance']

        
    return bestSolution        
