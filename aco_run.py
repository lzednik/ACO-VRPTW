import time
from aco_funs import *
from aco_vrptw import *

import sys
from PyQt5.QtCore import pyqtSignal, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, 
    QHBoxLayout, QVBoxLayout,QLabel,QGridLayout,QFileDialog,QPushButton,QCheckBox,QLineEdit)

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
        
        
        self.iterD=QLabel('Iteration')
        self.iterDv=QLabel('0')
       
        self.iterCountD=QLabel('Iteration Count')
        self.iterCountDv=QLabel('0')
        
        self.colD=QLabel('Colony')
        self.colDv=QLabel('0')
        
        self.colSizeD=QLabel('Colony Size')
        self.colSizeDv=QLabel('0')
       
        self.alphaD=QLabel('Alpha')
        self.alphaDv=QLabel('0')
       
        self.brcpD=QLabel('BiRCP')
        self.brcpDv=QLabel('0')
       
        self.vehCountD = QLabel('Vehicle Count')	
        self.vehCountDv = QLabel('0')

        self.distD=QLabel('Distance')
        self.distDv=QLabel('0')
       

        layout.addWidget(self.titleD,1,1)
        
        layout.addWidget(self.iterD,2,1)
        layout.addWidget(self.iterDv,2,2)
        layout.addWidget(self.iterCountD,3,1)
        layout.addWidget(self.iterCountDv,3,2)
        
        layout.addWidget(self.colD,4,1)
        layout.addWidget(self.colDv,4,2)
        layout.addWidget(self.colSizeD,5,1)
        layout.addWidget(self.colSizeDv,5,2)
        
        layout.addWidget(self.alphaD,6,1)
        layout.addWidget(self.alphaDv,6,2)
        
        layout.addWidget(self.brcpD,7,1)
        layout.addWidget(self.brcpDv,7,2)
        
        layout.addWidget(self.vehCountD,8,1)
        layout.addWidget(self.vehCountDv,8,2)

        layout.addWidget(self.distD,9,1)
        layout.addWidget(self.distDv,9,2)
	 
        self.setLayout(layout)
    
    def dispRefresh(self,vehicleCount,distance,iteration,iterationCount,colony,colonySize,alpha,BRCP):
        self.vehCountDv.setText(str(vehicleCount))
        self.vehCountDv.adjustSize()
        
        self.distDv.setText(str(distance))
        self.distDv.adjustSize()

        self.iterDv.setText(str(iteration))
        self.iterDv.adjustSize()
        
        self.iterCountDv.setText(str(iterationCount))
        self.iterDv.adjustSize()

        self.colDv.setText(str(colony))
        self.colDv.adjustSize()
        
        self.colSizeDv.setText(str(colonySize))
        self.colSizeDv.adjustSize()

        self.alphaDv.setText(str(alpha))
        self.alphaDv.adjustSize()
        
        self.brcpDv.setText(str(BRCP))
        self.brcpDv.adjustSize()
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
        
class researchVar(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
	    
        layout = QHBoxLayout()
        
        self.b1 = QPushButton("Alpha")
        self.b1.setCheckable(True)
        self.b1.clicked[bool].connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.b1)
		
        self.b2 = QPushButton("BRCP")
        self.b2.setCheckable(True)
        self.b2.clicked[bool].connect(lambda:self.btnstate(self.b2))
        layout.addWidget(self.b2)
    
        self.b3 = QPushButton("Colony Size")
        self.b3.setCheckable(True)
        self.b3.clicked[bool].connect(lambda:self.btnstate(self.b3))
        layout.addWidget(self.b3)
        
        self.fromL=QLabel('From')
        self.fromLv=QLineEdit()
        layout.addWidget(self.fromL)
        layout.addWidget(self.fromLv)

        self.toL=QLabel('To')
        self.toLv=QLineEdit()
        layout.addWidget(self.toL)
        layout.addWidget(self.toLv)
        
        self.stepL=QLabel('Step')
        self.stepLv=QLineEdit()
        layout.addWidget(self.stepL)
        layout.addWidget(self.stepLv)
       
        self.resVar='None'
        self.setLayout(layout)
    
    def btnstate(self,b):
        self.resVar='None'
        if b.text()=='Alpha':
            self.b2.setChecked(False)
            self.b3.setChecked(False)
            if self.b1.isChecked():
                self.resVar='Alpha'
            else:
                self.resVar='None'
        if b.text()=='BRCP':
            self.b1.setChecked(False)
            self.b3.setChecked(False)
            if self.b2.isChecked():
                self.resVar='BRCP'
            else:
                self.resVar='None'
        
        if b.text()=='Colony Size':
            self.b1.setChecked(False)
            self.b2.setChecked(False)
            if self.b3.isChecked():
                self.resVar='Colony Size'
            else:
                self.resVar='None'
        print(self.resVar)

def run_bt_clicked(self):
    print('running')
    #QApplication.processEvents()
    #aco_dtb
    dtb='Output/aco_dtb.sqlite'
    conn=sqlite3.connect(dtb)
    c=conn.cursor()
    c.execute('DELETE FROM Solutions')
    c.execute('DELETE FROM Vehicles')

    rsv=rsv1.resVar
    if rsv == 'None':
        rsvFrom=1
        rsvTo=1
        rsvStep=1
    else:
        rsvFrom=round(float(rsv1.fromLv.text()),2)
        rsvTo=round(float(rsv1.toLv.text()),2)
        rsvStep=round(float(rsv1.stepLv.text()),2)
    
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

    id_var=1
    for run in range(runCount):
        
        rsvV=rsvFrom
        while rsvV<=rsvTo:
            if rsv=='Alpha':
                alpha=rsvV
            if rsv=='BRCP':
                BRCP=rsvV
            if rsv=='Colony Size':
                colSize=int(rsvV)

            solution=aco_run(dataM,distM,depo,locCount,initSol,alpha,BRCP,iterCount,colSize)

            c.execute('''INSERT INTO Solutions(idVar,run,iteration,iterCount,colony,colonySize,alpha,BRCP,vehCount,distance)
      VALUES(?,?,?,?,?,?,?,?,?,?)''', (id_var,run,solution['iteration'],iterCount,solution['colony'],colSize,alpha,BRCP,solution['vehicleCount'],solution['distance'])) 
           
            for veh in solution['vehicles']:
                c.execute('''INSERT INTO Vehicles(idVar,vehNum,vehTour)
                           VALUES(?,?,?)''', (id_var,veh['vehNum'],str(veh['tour']))) 
            
            id_var+=1
            conn.commit()

            bsRefresh=False
            if run==0:
                bestSolution=solution
                bsRefresh=True

            if solution['vehicleCount']< bestSolution['vehicleCount']:
                bestSolution=solution
                bsRefresh=True
            if solution['vehicleCount']==bestSolution['vehicleCount'] and solution['distance']==bestSolution['distance']:
                bestSolution=solution        
                bsRefresh=True

            d1.dispRefresh(solution['vehicleCount'],solution['distance'],solution['iteration'],iterCount,solution['colony'],colSize,alpha,BRCP)
            if bsRefresh==True:
                d2.dispRefresh(bestSolution['vehicleCount'],bestSolution['distance'],bestSolution['iteration'],iterCount,bestSolution['colony'],colSize,alpha,BRCP)
            
            rd1.runRefresh(run)
            
            rsvV+=rsvStep
            rsvV=round(rsvV,2)
            QApplication.processEvents()
    conn.close()        

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
    rsv1=researchVar()

    layout.addWidget(s1,1,1)
    layout.addWidget(s2,1,2)
    layout.addWidget(s3,2,1)
    layout.addWidget(s4,2,2)
    layout.addWidget(s5,2,3)
    
    layout.addWidget(rsv1,3,1,1,3)

    layout.addWidget(fd,4,1,1,2)
    layout.addWidget(run_bt,5,1,1,1)
    
    layout.addWidget(rd1,5,2,1,1)

    layout.addWidget(d1,6,1,1,1)
    layout.addWidget(d2,6,2,1,1)

    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())
