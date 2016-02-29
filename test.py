#just testing things here

from graphics import *
from time import *
from funs import *

win=GraphWin('Ant Output',1300,600)
win.setCoords(0,0,1300,600)
        
#ln1 = Line(Point(1, 10), Point(600, 600))
#ln1.setWidth(3)
#ln1.setFill("red")
#ln1.draw(win)

dataM=readData('solomon_r101.txt')

for dt in dataM:
    pt=Point(8*dt['xcoord'], 8*dt['ycoord'])
    cir=Circle(pt,5)
    cir.setOutline('red')
    cir.setFill('red')
    cir.draw(win)

sleep(5)
win.clear
win.getMouse()
win.close()



