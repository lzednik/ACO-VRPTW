import sqlite3

dtb='Output/Ants.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

#phi
#c.execute('''
#    CREATE TABLE Phi(Iteration INTEGER, locFrom INTEGER,
#                       locTo INTEGER, Phi REAL)
#''')


#c.execute('DROP TABLE Vehicles')
#Vehicles
c.execute('''
    CREATE TABLE Vehicles(  Iteration INTEGER, 
                            vehNum INTEGER,
                            Loc INTEGER, 
                            readyTime INTEGER,
                            serviceTime INTEGER,
                            dueTime INTEGER,
                            nextLoc INTEGER,
                            distToNext REAL)
''')



#c.execute('''
#    CREATE TABLE Attraction(Iteration INTEGER PRIMARY KEY, locFrom INTEGER,
#                       locTo INTEGER, Phi REAL, Attr REAL)
#''')

conn.commit()
conn.close

print('done')

