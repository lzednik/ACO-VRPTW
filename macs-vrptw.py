from funs import *
from ant import Ant
import time
import pickle
from os import path
import sqlite3

dataM=readData('Input/solomon_r101.txt')
locCount=len(dataM)


dtb='Output/Ants.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()
c.execute('DELETE FROM Phi')
c.execute('DELETE FROM FIN')
c.execute('DELETE FROM Vehicles')
c.execute('DELETE FROM Attr')
c.execute('DELETE FROM Summary')

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


for i in range(100):
    if i%100 == 0:
        print('Iteration:',i)

    bestSolution=ant0.calculate(dataM,distM,phiM1,feasLocIN1,1,i,c)
        
    fullSol='N'    
    #full solution:
    if locCount==bestSolution['visitedCount']:
        fullSol='Y'

        #evaporate all phis
        for px in range(len(phiM1)):
            for py in range(len(phiM1)):
                phiM1[px][py]=0.9*(phiM1[px][py])
        
        
        #update phi
        for vehicle in bestSolution['vehicles']:
            for pos in range(len(vehicle['tour'])-1):
                locFrom=vehicle['tour'][pos]
                locTo=vehicle['tour'][pos+1]
                phiM1[locFrom][locTo]=1.10*phiM1[locFrom][locTo]
        vehicleNumber-=1
        ant0=Ant(vehicleCount=vehicleNumber,dataM=dataM)   

        print('****************************************')       
        print('iterationi:\t',i)
        print('veh count:\t',vehicleNumber+1)
        print('full solution:\t',bestSolution['visitedCount'])
        print('****************************************')
        print('')

    #log phi
    for px in range(len(phiM1)):
        for py in range(len(phiM1)):
            c.execute('''INSERT INTO Phi(iter, locFrom, locTo, phi)
                         VALUES(?,?,?,?)''', (i,px, py,phiM1[px][py]))

    #log Fin
    for px in range(len(feasLocIN1)):
        for py in range(len(feasLocIN1)):
            c.execute('''INSERT INTO FIN(iter, locFrom, locTo, finval)
                         VALUES(?,?,?,?)''', (i,px, py,feasLocIN1[px][py]))


    #log vehicles
    for vehicle in bestSolution['vehicles']:
        vehNum=vehicle['vehNum']
        c.execute('''INSERT INTO Summary(iter, fullSol,vehNum, tour)
                         VALUES(?,?,?,?)''', (i,fullSol,vehicle['vehNum'],str(vehicle['tour'])))

        for pos in range(len(vehicle['tour'])):
            loc=vehicle['tour'][pos]           
            if pos<len(vehicle['tour'])-1:
                nloc=vehicle['tour'][pos+1]
            else:
                nloc=-999
            rt=dataM[loc]['ready_time']
            st=dataM[loc]['service_time']
            dt=dataM[loc]['due_time']
            if pos<len(vehicle['tour'])-1:
                dtn=distM[loc][nloc]
            else:
                dtn=0
            c.execute('''INSERT INTO Vehicles(iter, vehNum, loc, readyTime,serviceTime,dueTime,nextLoc,distToNext)
                         VALUES(?,?,?,?,?,?,?,?)''', (i,vehNum, loc,rt,st,dt,nloc,dtn))
           

#write results for checking
#txtFile=open('Output/Results.txt','w')
#for vehicle in bestSolution['vehicles']:
#    #print(vehicle['tour'])
#    txtFile.write(str(vehicle['tour']))
#    txtFile.write('\n\n')
#    
#    for pos in range(len(vehicle['tour'])):
#        loc=vehicle['tour'][pos]           
#        if pos<len(vehicle['tour'])-1:
#            nloc=vehicle['tour'][pos+1]  
#        txtFile.write('loc:\t')
#        txtFile.write(str(loc))
#        txtFile.write('\tready_time:\t')
#        txtFile.write(str(dataM[loc]['ready_time']))
#        txtFile.write('\tservice_time"\t')
#        txtFile.write(str(dataM[loc]['service_time']))
#        txtFile.write('\tdue_time"\t')
#        txtFile.write(str(dataM[loc]['due_time']))
#        if pos<len(vehicle['tour'])-1:
#            txtFile.write('\tdist to next"\t')
#            txtFile.write(str(distM[loc][nloc]))
#        txtFile.write('\n')
#
#    txtFile.write('*******************************************\n\n')
#
#txtFile.close()
           
#for vehicle in bestSolution['vehicles']:
#    print(vehicle['tour'])


conn.commit()
conn.close()

print('all done')

       

