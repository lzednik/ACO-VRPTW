from tkinter import *
from funs import *
import pickle

fileObject = open('best_solution42','rb') 
bestSolution = pickle.load(fileObject)
fileObject.close()

dataM=readData('solomon_r101.txt')


root=Tk()

lb = Label(root, text='Ant Colony Optimization')
lb.pack()

canvas = Canvas(root, width=650, height=650)
canvas.pack()

#w.create_line(0, 10, 500, 400, fill="red")

#mycolor = '#%02x%02x%02x' % (243, 34, 29)
#for dt in dataM:
#    canvas.create_oval(5*dt['xcoord'], 5*dt['ycoord'], 5*dt['xcoord']+5, 5*dt['ycoord']+5, outline=mycolor, fill=mycolor, width=2)


amount=len(bestSolution['vehicles'])+1
veh=0
for vehicle in bestSolution['vehicles']:
    veh+=1
    for index in range(0,len(vehicle['tour'])-1):
        fromLoc=vehicle['tour'][index]
        toLoc=vehicle['tour'][index+1]
        
        fromX=dataM[fromLoc]['xcoord']

        fromY=dataM[fromLoc]['ycoord']
        toX=dataM[toLoc]['xcoord']
        toY=dataM[toLoc]['ycoord']
        
        r=0
        g=0
        b=255
        mycolor = '#%02x%02x%02x' % (r,g,b,)
        canvas.create_line(8*fromX,8*fromY,8*toX,8*toY,fill=mycolor)

mainloop()



#amount = 20

#for i in range(amount):
#    y = [j-i for j in x]
#    c = [float(i)/float(amount), 0.0, float(amount-i)/float(amount)] #R,G,B
#    plot(x, y, color=c)
#show()
