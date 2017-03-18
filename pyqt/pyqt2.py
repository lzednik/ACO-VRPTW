
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot,Qt
import time

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'ACO - WRPTW'
        self.left = 10
        self.top = 30
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #font - title
        tFont=QFont()
        tFont.setBold(True)

        #label top right corner
        self.lb_tr=QLabel('ACO VRPTW',self)
        self.lb_tr.setFont(tFont)
        self.lb_tr.move(550,10) 
       
        #alpha slider
        self.sl1_min0=5
        self.sl1_max0=50
        self.sl1_v0=20
        
        self.sl1_min=round(self.sl1_min0/100.,2)
        self.sl1_max=round(self.sl1_max0/100.,2)
        self.sl1_v=round(self.sl1_v0/100.,2)
        

        self.sl1=QSlider(Qt.Horizontal,self)
        self.sl1.move(40,100)
        self.sl1.setRange(self.sl1_min0,self.sl1_max0)
        self.sl1.setSingleStep(1)
        self.sl1.valueChanged[int].connect(self.sl1_cv)


        #alpha slider labels
        self.lb_sl1_min=QLabel(str(self.sl1_min),self)
        self.lb_sl1_min.setFont(tFont)
        self.lb_sl1_min.move(10,100)
        
        self.lb_sl1_max=QLabel(str(self.sl1_max),self)
        self.lb_sl1_max.setFont(tFont)
        self.lb_sl1_max.move(130,100)
        
        self.lb_sl1_v=QLabel('alpha = ' + str(self.sl1_v),self)
        self.lb_sl1_v.setFont(tFont)
        self.lb_sl1_v.move(40,80)


        self.show()


    def sl1_cv(self,value):
        self.sl1_v0=value
        self.sl1_v=round(self.sl1_v0/100.,2)
        self.lb_sl1_v.setText('alpha = ' + str(self.sl1_v))
        self.lb_sl1_v.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
