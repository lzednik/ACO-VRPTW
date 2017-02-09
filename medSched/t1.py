import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def cellClick(row,col):
    print("Click on " + str(row) + " " + str(col))
 
def main():  
    app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    tableItem 	= QTableWidgetItem()
 
    # initiate table
    table.setWindowTitle("QTableWidget Example @pythonspot.com")
    table.resize(400, 250)
    table.setRowCount(14)
    table.setColumnCount(2)
 
    # set label
    #table.setHorizontalHeaderLabels(QString('First Col'),QString('Second COl'))
    #table.setVerticalHeaderLabels(QString("V1;V2;V3;V4").split(";"))
 
    # set data
    table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
    table.setItem(0,1, QTableWidgetItem("Item (1,2)"))
    table.setItem(1,0, QTableWidgetItem("Item (2,1)"))
    table.setItem(1,1, QTableWidgetItem("Item (2,2)"))
    table.setItem(2,0, QTableWidgetItem("Item (3,1)"))
    table.setItem(2,1, QTableWidgetItem("Item (3,2)"))
    table.setItem(3,0, QTableWidgetItem("Item (4,1)"))
    table.setItem(4,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(5,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(6,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(7,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(8,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(9,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(10,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(11,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(12,0, QTableWidgetItem("Item (4,2)"))
    table.setItem(13,0, QTableWidgetItem("Item (4,2)"))
 
    # on click function
    table.cellClicked.connect(cellClick)
 
    # show table
    table.show()
    return app.exec_()
 
if __name__ == '__main__':
    main()
