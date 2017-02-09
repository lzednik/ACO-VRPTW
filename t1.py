import sqlite3

dtb='Output/aco_dtb.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()
#c.execute('select vehCount, count(distinct idVar) FROM Solutions group by vehCount')
c.execute('select vehCount, colonySize,count(distinct idVar) as c FROM Solutions group by vehCount,colonySize')
rows = c.fetchall()

xobjs=[]
yobjs=[]
for row in rows:
    print(row)
    xobjs.append(row[0])
    yobjs.append(row[1])
conn.close()



import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
print(y_pos)
performance = [10,8,6,4,2,1]
 
plt.bar(xobjs, yobjs, align='center', alpha=0.5)

plt.xticks(xobjs)
plt.ylabel('Run Counts')
plt.xlabel('Vehicle Counts')
plt.title('ACO_VRPTW')
 
plt.show()
