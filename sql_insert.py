import sqlite3

dtb='Ants.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

#c.execute('''INSERT INTO Attraction(Iteration, locFrom, locTo, Phi,Attr)
#                  VALUES(?,?,?,?,?)''', (1,92, 57,0.075,267))


#c.execute('''INSERT INTO Attraction(Iteration, locFrom, locTo, Phi,Attr)
#                  VALUES(?,?,?,?,?)''', (2,57, 68,0.00021,4556))


#c.execute('''INSERT INTO Attraction(Iteration, locFrom, locTo, Phi,Attr)
#                  VALUES(?,?,?,?,?)''', (3,57, 88,0.00021,4556))

c.execute('DELETE FROM Attraction')

conn.commit()
conn.close()

print('done')
