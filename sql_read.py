import sqlite3

dtb='Output/Ants.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

#stuff=c.execute('''SELECT Iteration, locFrom, locTo, Phi,Attr FROM Attraction WHERE locFrom=?''', (57,))

stuff=c.execute('''SELECT * FROM Vehicles WHERE Iteration=1''')




for x in stuff:
    print(x)

