
#from _tkinter import *

from tkinter import *
from funs import *

root = Tk()

lb = Label(root, text='Ant Colony Optimization')
lb.pack()

canvas = Canvas(root, width=600, height=600)
canvas.pack()


#w.create_line(0, 10, 500, 400, fill="red")

dataM=readData('solomon_r101.txt')

mycolor = '#%02x%02x%02x' % (243, 34, 29)

for dt in dataM:
    canvas.create_oval(5*dt['xcoord'], 5*dt['ycoord'], 5*dt['xcoord']+5, 5*dt['ycoord']+5, outline=mycolor, fill=mycolor, width=2)


mainloop()
