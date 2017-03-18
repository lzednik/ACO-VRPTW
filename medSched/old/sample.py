
import itertools
import time


stuff = [1,2,3,4,5,6,7,8,9,10]

for comb in itertools.combinations(stuff, 2):
    print(comb)
    time.sleep(0.1)