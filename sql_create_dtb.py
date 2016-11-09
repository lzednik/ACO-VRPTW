import sqlite3

dtb='Output/Ants.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

c.execute('DROP TABLE Phi')
c.execute('DROP TABLE Vehicles')
c.execute('DROP TABLE Attr')
c.execute('DROP TABLE Summary')


#phi
c.execute('''
    CREATE TABLE Phi(   iter INTEGER, 
                        locFrom INTEGER,
                        locTo INTEGER, 
                        phi REAL)
''')



#Vehicles
c.execute('''
    CREATE TABLE Vehicles(  iter INTEGER, 
                            vehNum INTEGER,
                            loc INTEGER, 
                            readyTime INTEGER,
                            serviceTime INTEGER,
                            dueTime INTEGER,
                            nextLoc INTEGER,
                            distToNext REAL)
''')


#Attr
c.execute('''
    CREATE TABLE Attr(  iter INTEGER, 
                        vehNum INTEGER,
                        currLoc INTEGER, 
                        nextLoc INTEGER,
                        attr0 REAL,
                        attr1 REAL)
''')



#Vehicles
#sum
c.execute('''
    CREATE TABLE Summary(   iter INTEGER,
                            fullSol TEXT,
                            vehNum INTEGER,
                            tour TEXT)
''')



conn.commit()
conn.close

print('done')

