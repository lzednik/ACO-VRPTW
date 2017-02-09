import sqlite3

dtb='Output/aco_dtb.sqlite'
conn=sqlite3.connect(dtb)
c=conn.cursor()

#c.execute('DROP TABLE Phi')
#c.execute('DROP TABLE Vehicles')
#c.execute('DROP TABLE Attr')
#c.execute('DROP TABLE Summary')

#c.execute('DROP TABLE FIN')
#c.execute('DROP TABLE Solutions')

c.execute('DROP TABLE Solutions')

c.execute('''
    CREATE TABLE Solutions(     idVar INTEGER,
                                run INTEGER,
                                iteration INTEGER,
                                iterCount INTEGER,
                                colony INTEGER,
                                colonySize INTEGER,
                                alpha FLOAT,
                                BRCP INTEGER,
                                vehCount INTEGER,
                                distance FLOAT)
''')


c.execute('''
    CREATE TABLE Vehicles(      idVar INTEGER,
                                vehNum INTEGER,
                                vehTour TEXT)
''')

#Solutions
#c.execute('''
#    CREATE TABLE Solutions( iter INTEGER,
#                            colony INTEGER,
#                            vehCount INTEGER,
#                            visitedCount INTEGER,
#                            visited TEXT
#                            )
#''')


##Vehicles
#c.execute('''
#    CREATE TABLE Vehicles(  iter INTEGER,
#                            colony INTEGER,
#                            vehNum INTEGER,
#                            tour TEXT)
#''')
#

#c.execute('''
#    CREATE TABLE Vehicles(  vehNum INTEGER,
#                            tour TEXT)
#''')


#Vehicles old
#c.execute('''
#    CREATE TABLE Vehicles(  iter INTEGER,
#                            colony INTEGER,
#                            vehNum INTEGER,
#                            loc INTEGER, 
#                            readyTime INTEGER,
#                            serviceTime INTEGER,
#                            dueTime INTEGER,
#                            nextLoc INTEGER,
#                            distToNext REAL)
#''')
#





##phi
#c.execute('''
#    CREATE TABLE Phi(   iter INTEGER, 
#                        locFrom INTEGER,
#                        locTo INTEGER, 
#                        phi REAL)
#''')


#fIN
#c.execute('''
#    CREATE TABLE FIN(   iter INTEGER, 
#                        locFrom INTEGER,
#                        locTo INTEGER, 
#                        finval INTEGER)
#''')






#Attr
#c.execute('''
#    CREATE TABLE Attr(  iter INTEGER, 
#                        vehNum INTEGER,
#                        currLoc INTEGER, 
#                        nextLoc INTEGER,
#                        attr0 REAL,
#                        attr1 REAL)
#''')



##sum
#c.execute('''
#    CREATE TABLE Summary(   iter INTEGER,
#                            fullSol TEXT,
#                            vehNum INTEGER,
#                            tour TEXT)
#''')





conn.commit()
conn.close

print('done')

