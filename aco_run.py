
import sys
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, 
    QHBoxLayout, QVBoxLayout,QLabel,QGridLayout,QFileDialog,QPushButton)

class slide(QWidget):

    clicked = pyqtSignal()
    
    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
       
        tFont=QFont()
        tFont.setBold(True)
        
        self.lbMin=QLabel(self)
        self.lbMax=QLabel(self)
        self.lbNme=QLabel(self)
        self.lbVal=QLabel(self)

        self.lbMin.setFont(tFont)
        self.lbMax.setFont(tFont)
        self.lbNme.setFont(tFont)
        self.lbVal.setFont(tFont)

        self.lbMin.move(10,40)
        self.lbMax.move(140,40)
        self.lbNme.move(10,1)
        self.lbVal.move(10,20)

        self.sl1=QSlider(Qt.Horizontal,self)
        self.sl1.move(40,40)
        self.sl1.valueChanged[int].connect(self.changeValue)
    
    def setSlide(self,nme,tpe,dVal,minVal,maxVal):
        
        self.tpe=tpe

        if tpe =='perc':
            dVal0=round(dVal/100.,2)
            minVal0=round(minVal/100.,2)
            maxVal0=round(maxVal/100.,2)
        
        if tpe=='count':
            dVal0=dVal
            minVal0=minVal
            maxVal0=maxVal


        self.lbMin.setText(str(minVal0))
        self.lbMin.adjustSize()
    
        self.lbMax.setText(str(maxVal0))
        self.lbMax.adjustSize()
        
        self.lbNme.setText(nme)
        self.lbNme.adjustSize()
        
        self.lbVal.setText(str(dVal0))
        self.lbVal.adjustSize()
        
        self.sl1.setRange(minVal,maxVal)
        self.sl1.setSingleStep(1)
        

    def sizeHint(self):
        return QSize(180, 80)
 
    def changeValue(self,value):
        #print(value)
        if self.tpe=='perc':
            value0=round(value/100.,2)
        if self.tpe=='count':
            value0=value

        self.lbVal.setText(str(value0))
        self.lbVal.adjustSize()

class filedialog(QWidget):
   def __init__(self, parent = None):
      super(filedialog, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton('Select Input File')
      self.btn.clicked.connect(self.getfile)
		
      layout.addWidget(self.btn)
      self.inpFileLb = QLabel('File Name')	
      layout.addWidget(self.inpFileLb)
	 
      self.setLayout(layout)
		
   def getfile(self):
      inpFile = QFileDialog.getOpenFileName(self, 'Open file','C:\\Users\Lada\Documents\ACO\ACO-VRPTW\Input',"Txt Files (*.txt)")
      inpFile[0] 
      self.inpFileLb.setText(inpFile[0])
      self.inpFileLb.adjustSize()
      
      print(inpFile)
      #self.le.setPixmap(QPixmap(fname))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('ACO VRPTW')

    s1 = slide()
    s2 = slide()
    s3 = slide()
    s4 = slide()
    s5 = slide()
    

    s1.setSlide('Alpha','perc',10,5,50)
    s2.setSlide('BRSP','perc',60,0,100)
    s3.setSlide('Run Count','count',1,1,100)
    s4.setSlide('Iteration Count','count',20,1,50)
    s5.setSlide('Colony Size','count',20,1,100)

    label = QLabel('hi hi')
    
    fd = filedialog()
    
    layout=QGridLayout()
    
    layout.addWidget(s1,1,1)
    layout.addWidget(s2,1,2)
    layout.addWidget(s3,2,1)
    layout.addWidget(s4,2,2)
    layout.addWidget(s5,2,3)
    
    
    
    layout.addWidget(label,3,1)
    
    layout.addWidget(fd,5,1,1,2)
    window.setLayout(layout)
    

    

    window.show()
    sys.exit(app.exec_())
