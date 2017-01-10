
from aco_funs import *
from aco_vrptw import *




alpha=0.1
depo=0
input_file='Input/solomon_r101.txt'

srt=aco_setup(input_file,depo)
dataM=srt['dataM']
distM=srt['distM']
locCount=srt['locCount']
initSol=srt['initSol']

bs=aco_run(dataM,distM,depo,locCount,initSol,alpha)

