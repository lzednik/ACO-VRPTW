import sys
sys.path.append('C:/Users/Lada/Documents/ACO/ACO-VRPTW/') 

from aco_funs import *


dataM=readData('C:/Users/Lada/Documents/ACO/ACO-VRPTW/Input/solomon_r101.txt')

for rec in dataM[0]:
    print(rec)

