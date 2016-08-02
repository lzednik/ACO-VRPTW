from random import choice
from collections import Counter
locs={  '0':10,
        '1': 3,
        '2':15,
        '3':2,
        '4':7,
        '5':8,
        '6':31,
        '7':3,
        '8':12,
        '9':1}


s=sum(locs.values())

weights={}
probs=[]
for loc in locs:
    weights[loc]=int(s/locs[loc])
    probs+=weights[loc]*[loc]



x=0
flist=[]
while x<100:
    x+=1
    flist.append(choice(probs))

ct=Counter(flist)

for item in ct:
    print(item,ct[item])

