
from aco_funs import *
from aco_vrptw import *

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

        self.slide=QSlider(Qt.Horizontal,self)
        self.slide.move(40,40)
        self.slide.valueChanged[int].connect(self.slideChangeValue)
    
        
        
    def setSlide(self,nme,tpe,dVal,minVal,maxVal):
        self.slNme=nme
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
        
        #self.lbVal.setText(str(dVal0))
        #self.lbVal.adjustSize()
        
        self.slide.setRange(minVal,maxVal)
        self.slide.setSingleStep(1)
        
        self.slideChangeValue(dVal)

    def sizeHint(self):
        return QSize(180, 80)
 
    def slideChangeValue(self,value):
        #print(value)
        if self.tpe=='perc':
            value0=round(value/100.,2)
        if self.tpe=='count':
            value0=value
        
        slideVals[self.slNme]=value
        print(slideVals)
        self.lbVal.setText(str(value0))
        self.lbVal.adjustSize()
        self.slide.setValue(value)

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
      self.inpFilePath=inpFile[0]
      self.inpFileLb.setText(self.inpFilePath)
      self.inpFileLb.adjustSize()
      
      #self.le.setPixmap(QPixmap(fname))

class resDisp(QWidget):
    def __init__(self,titleD,parent=None):
        QWidget.__init__(self, parent)
		
        tFont=QFont()
        tFont.setBold(True)
        
        
        layout = QGridLayout()
      
        self.titleD=QLabel(titleD)
        self.titleD.setFont(tFont)
        
        
        self.vehCountD = QLabel('Vehicle Count')	
        self.vehCountDv = QLabel('0')

        self.distD=QLabel('Distance')
        self.distDv=QLabel('0')
        
        layout.addWidget(self.titleD,1,1)
        
        layout.addWidget(self.vehCountD,2,1)
        layout.addWidget(self.vehCountDv,2,2)
        
        layout.addWidget(self.distD,3,1)
        layout.addWidget(self.distDv,3,2)
	 
        self.setLayout(layout)
    
    def dispRefresh(self,vehicleCount,distance):
        self.vehCountDv.setText(str(vehicleCount))
        self.vehCountDv.adjustSize()
        
        self.distDv.setText(str(distance))
        self.distDv.adjustSize()

class runDisp(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
		
        tFont=QFont()
        tFont.setBold(True)
        
        
        layout = QGridLayout()
      
        
        self.runD = QLabel('Run')	
        self.runDv = QLabel('0')
        
        self.runD.setFont(tFont)
        self.runDv.setFont(tFont)
        
        layout.addWidget(self.runD,1,1)
        layout.addWidget(self.runDv,1,2)
    
        self.setLayout(layout)

    def runRefresh(self,run):
        self.runDv.setText(str(run+1))
        self.runDv.adjustSize()
        
def run_bt_clicked(self):
    print('running')
    #QApplication.processEvents()

    alpha=0.1
    depo=0
    input_file=fd.inpFilePath
    srt=aco_setup(input_file,depo)
    dataM=srt['dataM']
    distM=srt['distM']
    locCount=srt['locCount']
    initSol=srt['initSol']
    
    alpha=round(slideVals['Alpha']/100.,2)
    BRCP=round(slideVals['BRCP']/100.,2)
    runCount=slideVals['Run Count']
    iterCount=slideVals['Iteration Count']
    colSize=slideVals['Colony Size']
    
    print('alpha',alpha)
    print('BRCP',BRCP)
    print('runCount',runCount)
    print('iterCount',iterCount)
    print('colSize',colSize)
    for run in range(runCount):
        solution=aco_run(dataM,distM,depo,locCount,initSol,alpha,BRCP,iterCount,colSize)
        if run==0:
            bestSolution=solution
        
        if solution['vehicleCount']< bestSolution['vehicleCount']:
            bestSolution=solution
       
        if solution['vehicleCount']==bestSolution['vehicleCount'] and solution['distance']==bestSolution['distance']:
            bestSolution=solution        
        
        d1.dispRefresh(solution['vehicleCount'],solution['distance'])
        d2.dispRefresh(bestSolution['vehicleCount'],bestSolution['distance'])
        rd1.runRefresh(run)

        QApplication.processEvents()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('ACO VRPTW')

       
    slideVals={}


    #label = QLabel('hi hi')
    
    fd = filedialog()
    
    run_bt=QPushButton('RUN ACO')
    run_bt.setToolTip('run')  
    run_bt.clicked.connect(run_bt_clicked)

    layout=QGridLayout()
    
    s1 = slide()
    s2 = slide()
    s3 = slide()
    s4 = slide()
    s5 = slide()
    
    
    s1.setSlide('Alpha','perc',20,5,50)
    s2.setSlide('BRCP','perc',60,0,100)
    s3.setSlide('Run Count','count',1,1,100)
    s4.setSlide('Iteration Count','count',30,1,50)
    s5.setSlide('Colony Size','count',20,1,100)
   
    d1=resDisp('Current Solution')
    d2=resDisp('Best Solution')

    rd1=runDisp()

    layout.addWidget(s1,1,1)
    layout.addWidget(s2,1,2)
    layout.addWidget(s3,2,1)
    layout.addWidget(s4,2,2)
    layout.addWidget(s5,2,3)
    
    layout.addWidget(fd,3,1,1,2)
    layout.addWidget(run_bt,4,1,1,1)
    
    layout.addWidget(rd1,4,2,1,1)

    layout.addWidget(d1,5,1,1,1)
    layout.addWidget(d2,5,2,1,1)

    window.setLayout(layout)
    

    

    window.show()
    sys.exit(app.exec_())
